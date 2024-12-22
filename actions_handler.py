from tabulate import tabulate
from movie import Movie
from file_operations import save_movies_to_file, load_movies_from_file

# Initialize movie_list from file
movie_list = load_movies_from_file()

def add():
    print("Please enter the following information:")
    title = input("Movie's title:\n")
    director = input("Movie's director:\n")
    genre = input("Movie's genre:\n")
    release_year = input("Year of release:\n")
    new_movie = Movie(title=title, director=director, genre=genre, release_year=release_year)
    movie_list.append(new_movie.__dict__)
    save_movies_to_file(movie_list)
    print("Movie added successfully!")

def delete():
    delete_title_input = input("Please enter the title of the movie to delete:\n").lower()
    matching_movies = []
    for index, movie in enumerate(movie_list):
        if movie["title"].lower() == delete_title_input:
            matching_movies.append((index, movie))
    if not matching_movies:
        print("No movies found with that title")
        return
    display_data = [
        [index + 1, movie["title"], movie["director"], movie["genre"], movie["release_year"]]
        for index, movie in matching_movies
    ]
    headers = ["Index", "Title", "Director", "Genre", "Release Year"]
    print(tabulate(display_data, headers=headers, tablefmt="grid"))
    try:
        delete_index_input = int(input("Enter the index of the movie to delete (from the table above):\n")) - 1
        original_index = matching_movies[delete_index_input][0]
        movie_list.pop(original_index)
        save_movies_to_file(movie_list)
        print("Movie was deleted successfully")
    except (ValueError, IndexError):
        print("Invalid input, please enter a valid number")

def display():
    if not movie_list:
        print("No movies to display")
        return
    display_data = [
        [index + 1, movie["title"], movie["director"], movie["genre"], movie["release_year"]]
        for index, movie in enumerate(movie_list)
    ]
    headers = ["Index", "Title", "Director", "Genre", "Release Year"]
    print(tabulate(display_data, headers=headers, tablefmt="grid"))

def find():
    find_title_input = input("Please enter the title of the movie to find:\n")
    matching_movies = []
    for index, movie in enumerate(movie_list):
        if movie["title"].lower() == find_title_input.lower():
            matching_movies.append([
                index + 1, 
                movie["title"], 
                movie["director"], 
                movie["genre"], 
                movie["release_year"]
            ])
    if not matching_movies:
        print("No movie with given title was found")
        return
    headers = ["Index", "Title", "Director", "Genre", "Release Year"]
    print(tabulate(matching_movies, headers=headers, tablefmt="grid"))
