from flask import Flask

app = Flask(__name__)

@app.route('/')             # 경로를 생성
def hello():                # 유일한 함수명 하나 설정한다.
    return 'Hello, My Fist Flask!'

if __name__ == '__main__':
    app.run(debug=True)