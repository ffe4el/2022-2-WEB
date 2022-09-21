from flask import Flask, render_template, redirect, url_for, session, escape, request
from flask_cors import cross_origin

app = Flask(__name__)

# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'

# #로그인 페이지
# @app.route('/')
# def homepage():
#     return render_template('homepage.html')


#로그인 후 나타나는 페이지
# @app.route('/homepage/<name>')
@app.route('/homepage', methods=['GET'])
@cross_origin(origin='*')
def homepage(name=None):
    if request.method =='GET':
        name = request.args.get('name')
        age = request.args.get('age')
        major = request.args.get('major')
        university = request.args.get('university')

    name = str(escape(name))
    color1 = 'orange'

    age = int(escape(age))
    color2 = 'yellow'

    major = str(escape(major))
    color3 = 'MediumSeaGreen'

    university = str(escape(university))
    color4 = 'red'

    resp1 = ''
    resp1 +=  '''<p>\n'''
    resp1 += f'안녕하세요. <font color={color1}>{name}</font>입니다.'
    resp1 += '''</p>\n
    \n  
'''
    resp2 = ''
    resp2 +=  '''<p>\n'''
    resp2 += f"나이는 <font color={color2}>{age}</font>살 입니다."
    resp2 += '''</p>\n
    \n
'''
    resp3 = ''
    resp3 += '''<p>\n'''
    resp3 += f"<font color={color4}>{university}</font>에서 <font color={color3}>{major}</font>에 대해 공부하고 있습니다"
    resp3 += '''</p>\n
    \n
'''
    resp = f"<font color=white>{resp1} {resp2} {resp3}</font>"
    return resp


# #내 소개글
# @app.route('/admin')
# def hello():
#     return render_template('introduce.html')
#
# #내가 아닌 다른사람이 들어왔을때
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     guest = str(guest)
#     color = 'MediumSeaGreen'
#     resp = f"Hello <font color='{color}'>{guest}</font> as Guest"
#     return resp
#
#
# #유튜브 동영상 올리기(블랙핑크- 핑크베놈)
# @app.route('/blackpink')
# def blackpink():
#     return render_template('pink venom.html')
#
#
# @app.route("/gugudan/<dan>")
# def gugu(dan):
#     dan = int(dan)
#     # return "<p>Hello, World!</p>"
#     resp_text=""
#     color = "red"
#     resp_text += "<html>\n"
#     resp_text += "<body>\n"
#     for i in range(9):
#         resp_text += f"{dan} * {i + 1} = <font color='{color}'> {dan * (i + 1)}</font><br>\n"
#     return resp_text
#     resp_text += "</body>\n"
#     resp_text += "</html>\n"
#
#
# @app.route("/k2c/<k>")
# @app.route("/k2c", methods=['GET','POST'])
# def k2c(k=None):
#     if request.method=='GET':
#         k = request.args.get('k')
#     k = float(escape(k))
#     # c= float(k - 273.15)
#     # resp_c= f"{k} K => { c:.2f} C"
#     return f'{k}K -> {k - 273.15:.6f} C'
#

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)