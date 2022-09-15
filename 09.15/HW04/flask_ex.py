from flask import Flask

app = Flask(__name__)

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
def k2c(k):
    k= float(k)
    c= float(k - 273.15)
    resp_c= f"{k} K => { c:.2f} C"
    return resp_c



app.run(host="0.0.0.0", debug=True)