import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import pymysql

db = pymysql.connect(host='172.23.242.22',user='root',password='winincow',db='flyai',charset='utf8')


@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('감정쓰레기통')
st.markdown("응애 나 아기 개발자")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')

    # 과거 채팅 대화 내용 가져오기
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = f"select * from chatbot;"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        if row['type'] == 'user':
            message(row['msg'], is_user=True, key=row['num'])
        else:
            message(row['msg'], key=row['num'])


if submitted and user_input:
    embedding = model.encode(user_input)
    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])
    
    #유저와 챗봇의 대화 내용 저장
    cursor = db.cursor()

    # 유저의 대화 DB 기록
    cursor = db.cursor()
    sql = "insert into chatbot set type = 'user', msg = '%s', gubun='%s', indate = now();" % (user_input, answer['구분'])
    cursor.execute(sql)
    db.commit()

    # 챗봇의 대화 DB 기록
    cursor = db.cursor()
    sql = "insert into chatbot set type = 'bot', msg = '%s', gubun='%s', indate = now();" % (answer['챗봇'], answer['구분'])
    cursor.execute(sql)
    db.commit()

for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot')
