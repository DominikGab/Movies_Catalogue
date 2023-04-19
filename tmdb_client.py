import requests

API_TOKEN =  "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWJhMWI0MzFhNjY2ZjQ5Mzg4OGNhYzRkYTc4MDQ2MyIsInN1YiI6IjY0MWFmOWQxOTVjMGFmMDBmNzA3YzE0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DXd5aHVZNydzEVc-wrA_XlWgl2FMZ1ZvdyMqYeXEeQY"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_movies_list(list_type):
    valid_list_types = ['now_playing', 'popular', 'top_rated', 'upcoming']
    if list_type not in valid_list_types:
        list_type = 'popular'
    return call_tmdb_api(f"movie/{list_type}")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


