import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWJhMWI0MzFhNjY2ZjQ5Mzg4OGNhYzRkYTc4MDQ2MyIsInN1YiI6IjY0MWFmOWQxOTVjMGFmMDBmNzA3YzE0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DXd5aHVZNydzEVc-wrA_XlWgl2FMZ1ZvdyMqYeXEeQY"

    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"



