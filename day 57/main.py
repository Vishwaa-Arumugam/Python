from flask import Flask, render_template
from post import Post

o = Post()

app = Flask(__name__)


@app.route('/')
def home():
    all_title = o.title()
    all_subtitle = o.subtitle()
    return render_template("index.html", title=all_title, subtitle=all_subtitle)


@app.route('/post_1/')
def post():
    all_title = o.title()
    all_body = o.body()
    return render_template("post_1.html", title=all_title, body=all_body)


@app.route('/post_2/')
def post_2():
    all_title = o.title()
    all_body = o.body()
    return render_template("post_2.html", title=all_title, body=all_body)


@app.route('/post_3/')
def post_3():
    all_title = o.title()
    all_body = o.body()
    return render_template("post_3.html", title=all_title, body=all_body)


if __name__ == "__main__":
    app.run(debug=True)
