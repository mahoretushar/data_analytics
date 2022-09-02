MENU_PROMPT = "\nEnter 'a' to add a movie, '1' to see your movie, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for m in movies:
        print_movie(m)


def print_movie(m):
    # m = {
    #     title: v1,
    #     director: dn,
    #     year: 2000
    #  }
    print(f"Title: {m['title']}")
    print(f"Director: {m['director']}")
    print(f"Year: {m['year']}")
    print()


def find_movie():
    search_title = input("Enter Movie Title you're looking for: ")

    for m in movies:
        if m["title"] == search_title:
            print_movie(m)


user_options = {
    "a": add_movie,
    "1": show_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown Command. Please try again...")

        selection = input(MENU_PROMPT)


menu()
