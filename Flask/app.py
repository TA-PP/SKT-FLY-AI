from flask import Flask, render_template, request, redirect        # 모듈 추가
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')             # 경로를 생성
def index():                # 유일한 함수명 하나 설정한다.
    # return 'Hello, My Fist Flask!'
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        if userid == 'admin' and userpw == '1234':
            return redirect('/')
        else:
            return render_template('login.html', alertMsg='아이디 또는 비밀번호가 틀립니다.')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        name = request.form['username']
        f = request.files['img1']
        f.save('./upload/' + secure_filename(f.filename))

        # DB 인젝션 공격이 있는 지 검토
        # 이미 가입되어 있는 지 확인
        # DB에 회원정보 저장하기
        return redirect('/login?join=y')
        

if __name__ == '__main__':
    app.run(debug=True)