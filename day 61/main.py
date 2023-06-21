from flask import Flask, render_template
from forms import Forms
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "abcdef"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Forms()
    if form.validate_on_submit():
        if form.username.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
