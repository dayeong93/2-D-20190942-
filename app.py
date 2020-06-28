from flask import Flask, request, render_template, redirect, url_for, abort

import game
import json

import dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return "게임을 시작하기위해 닉네임을 정해주세요. ==> hello/사용하실 닉네임"


@app.route('/mainhtml/')
def mainhtml():
    return render_template('main.html')

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['items'])
    return "{}님 코알라가 {}능력을 이용해서 음식을 얻었습니다".format(character["name"], character["items"][0])

# 중간고사 
@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
           data = f.read()
           character = json.loads(data)
           print(character['items'])
        return " ✿ʕ·ᴥ·ʔ✿  ✧♬ʕ·ᴥ·ʔ♬✧ ❤ʕง·ᴥ·ʔง❤ ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ {}님 아기코알라가 {}능력을 이용해서 이웃들에게 음식을 받아 배부르게 먹었습니다~♬ ʕ ᵔᴥᵔ ʔ".format(character["name"], character["items"][0])
    elif num == 2:
        with open("static/save.txt", "r", encoding='utf-8') as f:
           data = f.read()
           character = json.loads(data)
           print(character['items'])
        return "{}님 아기코알라가...배고픔을 이겨내지 못하고 쓰러졌습니다 ʕ ཀᴥཀ ʔ GAME OVER 다시 접속해주세요!".format(character["name"])
   


# 12주차 과제 
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'GET':
#      return render_template('login.html')
#    else:
#        id = request.form['id']
#        pw = request.form['pw']
#        print (id,type(id))
#        print (pw,type(pw))
#        # id와 pw가 임의로 정한 값이랑 비교해서 맞으면 맞다 틀리면 틀리다
#        if id == 'abc' and pw == '1234':
#            return "안녕하세요~ {}님".format(id)
#        else:
#            return "아이디 또는 패스워드를 확인하세요."


# 12주차 과제   id/pw sqlite db에 저장 하고 로그인 세션 처리 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
      return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type(id))
        print (pw,type(pw))
        # id와 pw가 db 값이랑 비교해서 맞으면 맞다 틀리면 틀리다
        ret = dbdb.select_user(id, pw)
        print(ret[2])
        if ret != None: 
            return "안녕하세요~ {}님".format(ret[2])
        else:
            return "아이디 또는 패스워드를 확인하세요."


# 회원가입
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
      return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type(id))
        print (pw,type(pw))
        ret = dbdb.check_id(id)
        if ret != None:
            return '''
              <script>
              alert('다른 아이디를 사용하세요');
              location.href='/join';
              </script>
              '''
        dbdb.insert_user(id, pw, name)
        return redirect(url_for('login'))

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
       return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은 :{}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret[3])
    return render_template('getinfo.html', data=ret)
    #return '번호 : {}, 이름 : {}'.format(student[0], student[1])

#9주차 과제-1
@app.route('/naver/')
def naver():
    return redirect("https://www.naver.com/")
    #return render_template("naver.html")

@app.route('/kakao/')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/urltest/')
def url_test():
    return redirect(url_for('naver'))

#9주차 과제-2
@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
      return redirect(url_for('naver')) 
    elif site == 'daum':
      return redirect(url_for('daum'))
    else:
         abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/img')
def img():
    return render_template("image.html")

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)