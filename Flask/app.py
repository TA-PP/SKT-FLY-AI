from flask import Flask, render_template, request, redirect, session, send_file        # 모듈 추가
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text


app = Flask(__name__)
app.config['SECRET_KEY'] = 'winincow'           # session을 암호화 해주는 키 값 지정


# config.py를 불러오는 코드
app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database


# 인덱스
@app.route('/')             # 경로를 생성
def index():                # 유일한 함수명 하나 설정한다.
    if 'ss_name' in session:
        ss_name = session['ss_name']
        ss_img = session['ss_img']
    else:
        ss_name = ""  
        ss_img = ""          
    return render_template('index.html', ss_name=ss_name, ss_img=ss_img)

# 로그인
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        # 회원가입하는 부분
        sql = f"""select num, name, img from mem where 
        userid = '{userid}' and 
        userpw = SHA2('{userpw}', 256);"""
        user = app.database.execute(text(sql)).fetchone()

        if user:
            session['ss_id'] = user['num']
            session['ss_userid'] = userid
            session['ss_name'] = user['name']
            session['ss_img'] = user['img']
            return redirect('/')            
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

# 로그아웃
@app.route('/logout')
def logout():
    session['ss_id'] = False
    session['ss_userid'] = False
    session["ss_name"] = False
    session["ss_img"] = False
    return redirect('/')
    
# 회원가입    
@app.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else: # POST
        userid = request.form['userid']
        userpw = request.form['userpw']
        name = request.form['name']
        sex = request.form['sex']
        post_num = request.form['post_num']
        address = request.form['address']
        tel = request.form['tel']
        age = request.form['age']

        f = request.files['img1']
        f.save("Flask/static/" + secure_filename(f.filename))
        img = f.filename

        # DB 인젝션 공격이 있는 검토
        # 이미 가입 되어 있는지 확인
        # DB에 회원정보 저장하기
        app.database.execute(text("""
        insert into mem (
            userid, userpw, name, sex, post_num, address, tel, age, img
        ) values (
            :userid, SHA2(:userpw, 256), :name, :sex, :post_num, :address, :tel, :age, :img);"""), {
                'userid' : userid,
                'userpw' : userpw,
                'name' : name,
                'sex' : sex,
                'post_num' : post_num,
                'address' : address,
                'tel' : tel,
                'age' : age,
                'img' : img,
            }).lastrowid
        return redirect('/login?join=y')

# 리스트
@app.route('/list')
def list_members():
    sql = """select num, userid, name, sex, address, age, img from mem;"""
    user_list = app.database.execute(text(sql)).all()

    print(session)
    return render_template('list.html', user_list=user_list, session_id=session['ss_id'])

# 리스트 수정
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    return redirect('/list')

# 리스트 삭제
@app.route('/delete', methods=['GET'])
def delete():
    num = request.args.get('num')
    sql = "delete from mem where num = %s and userid='%s'" % (num, 
    session['ss_userid'])

    print(sql)
    app.database.execute(text(sql)).lastrowid    
    # 사진파일 삭제 (세션)
    return redirect('/logout')

@app.route('/cdn/<path:filename>')
def get_img(filename):
    if filename == 'default_profile.png':
        return send_file('static/default_profile.png')
    else:
        return send_file('upload/' + secure_filename(filename))

@app.route("/insert")
def insertdb():
    app.database.execute(text("""
    insert into mem set
    id = 'abc',
    name = 'HogGilDong',
    sex = 'M',
    post_num = '12345',
    address = 'Seoul',
    tel = '010-1111-2222',
    age = 50;""")).lastrowid
    return "Insert DB OK"
        

if __name__ == '__main__':
    app.run(debug=True)