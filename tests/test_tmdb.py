import sys, requests
sys.path.append(r'C:\Kodilla\Kurs\Movies\movies_catalogue')
import tmdb_client
from unittest.mock import Mock


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWJhMWI0MzFhNjY2ZjQ5Mzg4OGNhYzRkYTc4MDQ2MyIsInN1YiI6IjY0MWFmOWQxOTVjMGFmMDBmNzA3YzE0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DXd5aHVZNydzEVc-wrA_XlWgl2FMZ1ZvdyMqYeXEeQY"

def test_get_poster_url_uses_default_size():
   # Przygotowanie danyc
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_single_movie():
   single_movie = tmdb_client.get_single_movie(movie_id="238")
   assert single_movie["title"] == 'The Godfather'

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie_cast():
   # użyłem movie_id o numerze 238 (The Godfather) dla przykładowego wywołania funkcji
   endpoint = f"https://api.themoviedb.org/3/movie/238/credits"
   api_token = API_TOKEN
   headers = {
        "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(endpoint, headers=headers)
   assert response.status_code == 200
   

