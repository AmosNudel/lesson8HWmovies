import json
import os

FILE_NAME = "movies.json"

def save_movies_to_file(movie_list):
    with open(FILE_NAME, "w+") as f:
        json.dump(movie_list, f, indent=4)

def load_movies_from_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return []
