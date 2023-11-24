import requests
import json

language_list=["English","Japanese","Chinese","Korean","German","French","Thai"]

movie_count = 0
movie_error = 0

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzE5NGNkM2M0MzBhNWM4MTM3NDhkZTFjZGM1YzUwNSIsInN1YiI6IjY1NWNmYTQ4N2YwNTQwMThkNzkxOTFjOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ciNYVjzmcXvuSKnt-TkO9TeKmS3rU-38q9LtnAVs2rM"
}

for page_number in range(5,30):
    merge_data = []
    movie_list_url = f"https://api.themoviedb.org/3/movie/changes?page={page_number}&api_key=5911577d644ad0ee6a1c0711acb2f773"
    response = requests.get(movie_list_url, headers=headers)
    movie_list_json=response.json()["results"]



    for movie_list in movie_list_json:
        if movie_list['adult'] == False:
            movie_ID = movie_list['id']
            
            movie_info_url = f"https://api.themoviedb.org/3/movie/{movie_ID}?language=en-US"
            response = requests.get(movie_info_url, headers=headers)
            movie_info_json = response.json()

            if response.status_code != 200:
                print(f"error in page {page_number}")
                movie_error += 1
                continue


            #since the movie data is too large, we have to do some preprocessing
            # ***filter movies without generes***
            # ***filter movies without spoken_languages***
            # ***filter movies with small amount of runtime***
            # ***filter movies with small amount of vote_count***
            if movie_info_json["genres"] == [] or movie_info_json["spoken_languages"]==[]:
                continue
            elif movie_info_json["spoken_languages"][0]["english_name"] not in language_list:
                continue
            elif movie_info_json["runtime"] < 10:
                continue
            elif movie_info_json["vote_count"] < 10:
                continue
            else:
                movie_count += 1
                merge_data.append(response.json())

    with open(f"movie_info/movie_info_page{page_number}.json", "w") as f:
        json.dump(merge_data, f, indent=4)
        print(f"movies in page {page_number} has been saved.")

print(f"we have collected {movie_count} movies.")