from flask import Flask, render_template
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# posts = [
#     {
#         'author': {
#             'username': 'test-user'
#         },
#         'title': '첫 번째 포스트',
#         'content': '첫 번째 포스트 내용입니다.',
#         'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
#     },
#     {
#         'author': {
#             'username': 'test-user'
#         },
#         'title': '두 번째 포스트',
#         'content': '두 번째 포스트 내용입니다.',
#         'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
#     },
# ]

# posts = []


@app.route('/')
@app.route('/home')
def home():
    return render_template("index_content.html")

@app.route('/blog')
def blog():
    df = pd.read_csv("blog_content.csv")
    posts =[]
    for idx, row in df.iterrows():
        posts.append(
            {
                'author': {
                    'username': row["username"]
                },
                'title': row["title"],
                'content': row["content"],
                'date_posted': datetime.strptime(row["date_posted"], '%Y-%m-%d')
            },
        )
    return render_template("blog_content.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about_content.html")

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
