import requests
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


# Function to fetch movies based on a search query
def get_movies(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query,
        "language": "en"
    }


    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])[:18]


# Fetch list of movie genres
def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        "api_key": API_KEY,
        "language": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("genres", [])


def get_recommendations(genre_id=None, year=None, recToggle=None):
    url = f"{BASE_URL}/discover/movie"

    params = {
        "api_key": API_KEY,
        "language": "en",
    }

    if recToggle is not None:
        params["sort_by"] = "popularity.desc"
    else:
        params["sort_by"] = "revenue.desc"
    

    
    


    if genre_id:
            params["with_genres"] = genre_id

    if year:
            params["primary_release_year"] = year
    


    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])[:18]



@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data











@app.route("/", methods=["GET", "POST"])
def index_title():
    
    query = request.args.get("query")
    genre_id = request.args.get("genre_id")
    year = request.args.get("year")
    recToggle = request.args.get("recToggle")


    genres = get_genres()

    if  genre_id or year or recToggle:
        movies = get_recommendations(genre_id, year, recToggle)
    elif query:
        movies = get_movies(query)
    else:
        movies = get_recommendations()
    

    return render_template("index.html", movies=movies, genres=genres)








# Run the Flask app
if __name__ == "__main__":
    app.run()