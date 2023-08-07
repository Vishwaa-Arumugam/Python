import csv
import requests

API_KEY = "6bd2260872537e8ab203df7ab99e11df"


def request_section():
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key=6bd2260872537e8ab203df7ab99e11df&language=en-US&query=fight club&page=1&include_adult=false")
    movie_data = response.json()["results"][0]
    fields = ["id", "title", "year", "description", "rating", "ranking", "review",
              "img_url"]
    m = [{
        "id": movie_data["id"],
        "title": movie_data["title"],
        "year": movie_data["release_date"],
        "description": movie_data["overview"],
        "rating": str(movie_data["vote_average"]),
        "ranking": str(movie_data["popularity"]),
        "review": movie_data["vote_count"],
        "img_url": movie_data["poster_path"]

    }]


    with open("Movies.csv", "w") as movie_db:
        writer = csv.DictWriter(movie_db, fieldnames=fields)
        writer.writeheader()
        writer.writerows(m)


request_section()
