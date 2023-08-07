from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from test import request_section
import pandas, csv
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


request_section()


@app.route("/")
def home():
    with open("Movies.csv", "r") as movie_db:
        reader = csv.DictReader(movie_db)
        movie_list = list(reader)
    return render_template("index.html", movies=movie_list)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    with open("Movies.csv", "r") as movie_db:
        reader = csv.DictReader(movie_db)
        movie_list = list(reader)
    if request.method == "POST":
        with open("Movies.csv", "r") as movie_db:
            reader = csv.DictReader(movie_db)
            movie_details = list(reader)
            movie_id = movie_details[0]["id"]
        rating = request.form['rating']
        review = request.form['review']
        df = pandas.read_csv("Movies.csv", index_col="id")
        df.at[int(movie_id), "rating"] = rating
        df.at[int(movie_id), "review"] = review
        df = df.reset_index()
        df.to_csv("Movies.csv", index=False)
        return redirect(url_for('home'))

    return render_template("edit.html", movies=movie_list)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        movie_title = request.form["title"]

        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=6bd2260872537e8ab203df7ab99e11df"
                                f"&language=en-US&query={movie_title}&page=1&include_adult=false")
        movie_data = response.json()["results"]
        movie_id = movie_data[0]["id"]
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{str(movie_id)}?api_key=6bd2260872537e8ab203df7ab99e11df&language=en-US")
        movies = response.json()
        m = {
            "id": movie_id,
            "title": movies["title"],
            "year": movie_data[0]["release_date"],
            "description": movie_data[0]["overview"],
            "rating": str(movie_data[0]["vote_average"]),
            "ranking": str(movie_data[0]["popularity"]),
            "review": movie_data[0]["vote_count"],
            "img_url": movie_data[0]["poster_path"]

        }
        with open("Movies.csv", "a") as movie_db:
            writer = csv.writer(movie_db)
            writer.writerow(m.values())
            movie_db.close()
        return render_template("select.html", options=movie_data)

    return render_template("add.html")


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    # print(movie_id)
    df = pandas.read_csv("Movies.csv")
    # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.drop(df[df["id"] == movie_id].id, inplace=True)
    # print(df)
    df.to_csv("Movies.csv")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
