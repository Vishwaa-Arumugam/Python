from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
all_books = []
app.config['SECRET_KEY'] = 'MYNAME'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String, unique=True, nullable=True)
    authorname = db.Column(db.String(30), unique=True, nullable=False)
    rating = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f"User('{self.id}' , '{self.bookname}', '{self.authorname}', '{self.rating}')"


app.app_context().push()
db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(User).all()
    print(all_books)
    return render_template("index.html", book=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = User(
            bookname=request.form["bookname"],
            authorname=request.form["authorname"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = User.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = User.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = User.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
