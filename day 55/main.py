from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph tag</p>' \
           '<img src="https://media4.giphy.com/media/YRVP7mapl24G6RNkwJ/200w.webp?cid=ecf05e47benlcxpt2k5029czo9y750mvkysuasau5eoqye13&rid=200w.webp&ct=g" width=200px>'


def make_bold(function):
    def inner_function():
        return f"<b>{function()}</b>"

    return inner_function


def make_emphasis(function):
    def inner_function():
        return f"<em>{function()}</em>"
    return inner_function


def make_underlined(function):
    def inner_function():
        return f"<u>{function()}</u>"
    return inner_function


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route('/username/<name>/<string:number>')
def greet(name, number):
    return f"Hello {name} + {number}"


if __name__ == "__main__":
    app.run(debug=True)
