from flask import request
import requests
from main import add_movie

API_KEY = "6bd2260872537e8ab203df7ab99e11df"

movie_title = add_movie
print(str(movie_title))

# def request_section():
#     response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=6bd2260872537e8ab203df7ab99e11df"
#                             f"&language=en-US&query={movie_title}&page=1&include_adult=false")
#     movie_data = response.json()["results"]
#     print(movie_data)
#     movie_id = movie_data[0]["id"]
#     print(movie_id)
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{str(movie_id)}?api_key=6bd2260872537e8ab203df7ab99e11df&language=en-US")
#     movies = response.json()
#     print(movies)


# request_section()
