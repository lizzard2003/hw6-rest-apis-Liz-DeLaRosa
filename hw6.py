import requests
from dotenv import load_dotenv , find_dotenv
from os import getenv 

load_dotenv(find_dotenv())

def get_top_10_weekly_trending_movies():
    TMDB_BASE_URL = "https://api.themoviedb.org/3"
    TMDB_TRENDING_WEEKLY_MOVIES_PATH= "/trending/movie/week"

    trending_movies_response = requests.get(
        TMDB_BASE_URL + TMDB_TRENDING_WEEKLY_MOVIES_PATH,
        params = {
            "api_key": getenv("TMDB_API_KEY"),
        },
    )

    trending_movies_list = trending_movies_response.json()["results"]

    for i in range(10):
        print(trending_movies_list[i]["title"])

get_top_10_weekly_trending_movies()   