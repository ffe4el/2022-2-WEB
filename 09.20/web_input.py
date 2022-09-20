from flask import Flask, escape, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('flask_home.html')


@app.route("/gugudan/<dan>")
@app.route("/gugudan", methods=['GET'])
@cross_origin(origin='*')
def gugudan(dan=None):
    if request.method == 'GET':
        dan = request.args.get('dan')

    dan = int(escape(dan))
    color = 'red'

    resp_text = ''
    resp_text += '''<p>\n'''

    for i in range(1, 10):
        resp_text += f'{dan} × {i} ＝ <font color={color}>{dan * i}</font><br>\n'

    resp_text += '''</p>\n
    \n
'''

    return resp_text


@app.route("/k2c/<k>")
@app.route("/k2c", methods=['GET'])
def k2c(k=None):
    if request.method == 'GET':
        k = request.args.get('k')

    k = float(escape(k))
    return f'{k}K -> {k - 273.15:.6f}C'


@app.route("/c2k/<c>")
@app.route("/c2k", methods=['GET', 'POST'])
def c2k(c=None):
    if request.method == 'GET':
        c = request.args.get('c')
    else:
        c = request.form.get('c')

    c = float(escape(c))
    return f'{c}C -> {c + 273.15:.6f}K'


def main():
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
