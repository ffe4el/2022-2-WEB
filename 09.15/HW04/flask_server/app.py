<<<<<<< Updated upstream
from flask import Flask, render_template, redirect, url_for, session, escape, request

=======
from flask import Flask, render_template, redirect, url_for, session, request
import webbrowser
>>>>>>> Stashed changes
app = Flask(__name__)

# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'

#로그인 페이지
@app.route('/')
def login_form_get():
    return render_template('login/login_form_get.html')


#로그인 후 나타나는 페이지
@app.route('/login_get_proc', methods=['GET'])
def log_get_proc():
    user_id = request.args.get('user_id')
    user_pwd = request.args.get('user_pwd')
    if len(user_id) == 0 or len(user_pwd) ==0:
        return f"{user_id} or {user_pwd} 존재하지 않습니다."
    elif (user_id) == "sola":
        return redirect(url_for('hello'))
    else :
        return redirect(url_for('hello_guest', guest = f"{user_id}"))

#내 소개글
@app.route('/admin')
def hello():
    return render_template('introduce.html')

#내가 아닌 다른사람이 들어왔을때
@app.route('/guest/<guest>')
def hello_guest(guest):
    guest = str(guest)
    color = 'MediumSeaGreen'
    resp = f"Hello <font color='{color}'>{guest}</font> as Guest"
    return resp

#내 깃로그로 연결하기전 고먐미
@app.route('/git_log')
def git_log():
    return render_template('git_log.html')


#내 깃로그로 연결
@app.route('/sol_log')
def sol_log():
    url = "https://ffe4el.github.io/"
    webbrowser.open(url)
    res ="Thank you for Click my log"
    return res



#유튜브 동영상 올리기(블랙핑크- 핑크베놈)
@app.route('/blackpink')
def blackpink():
    return render_template('pink venom.html')


@app.route("/gugudan/<dan>")
def gugu(dan):
    dan = int(dan)
    # return "<p>Hello, World!</p>"
    resp_text=""
    color = "red"
    resp_text += "<html>\n"
    resp_text += "<body>\n"
    for i in range(9):
        resp_text += f"{dan} * {i + 1} = <font color='{color}'> {dan * (i + 1)}</font><br>\n"
    return resp_text
    resp_text += "</body>\n"
    resp_text += "</html>\n"


@app.route("/k2c/<k>")
@app.route("/k2c", methods=['GET','POST'])
def k2c(k=None):
    if request.method=='GET':
        k = request.args.get('k')
    k = float(escape(k))
    # c= float(k - 273.15)
    # resp_c= f"{k} K => { c:.2f} C"
    return f'{k}K -> {k - 273.15:.6f} C'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)