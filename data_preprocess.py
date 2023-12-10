import json

genre_index={}
spoken_languages_index={}
runtime_index={}
popularity_index={}
release_date_index={}

for page_number in range(1, 30):
    movie__info = json.load(open(f"movie_info/movie_info_page{page_number}.json"))

    for movie in movie__info:
        # get the basic info of the movie
        movie_basic_info={
            "id":movie["id"],
            "title":movie["title"],
            "popularity":movie["popularity"],
            "homepage":movie["homepage"]
        }

        # split the movie into different genres
        for genre in movie["genres"]:
            genre_index.setdefault(genre["name"], []).append(movie_basic_info)

        # split the movie into different spoken_languages
        spoken_language=movie["spoken_languages"]
        spoken_languages_index.setdefault(spoken_language[0]["english_name"], []).append(movie_basic_info)

        # split the movie into different runtime
        runtime=movie["runtime"]
        if runtime <= 90:
            length_type="short"
        elif runtime <= 120:
            length_type="medium"
        else:
            length_type="long"
    
        runtime_index.setdefault(length_type, []).append(movie_basic_info)

        # split the movie into different popularity
        popularity=movie["popularity"]
        if popularity <= 20:
            popularity_type="0-20"
        elif popularity <= 40:
            popularity_type="20-40"
        elif popularity <= 60:
            popularity_type="40-60"
        elif popularity <= 80:
            popularity_type="60-80"
        elif popularity <= 100:
            popularity_type="80-100"
        else:
            popularity_type="100+"
    
        popularity_index.setdefault(popularity_type, []).append(movie_basic_info)

        # split the movie into different release_date
        release_date=movie["release_date"]
        if release_date <= "1980-01-01":
            release_date_type="1980-"
        elif release_date <= "1990-01-01":
            release_date_type="1990-"
        elif release_date <= "2000-01-01":
            release_date_type="2000-"
        elif release_date <= "2010-01-01":
            release_date_type="2010-"
        elif release_date <= "2020-01-01":
            release_date_type="2020-"
        else:
            release_date_type="2020+"
        
        release_date_index.setdefault(release_date_type, []).append(movie_basic_info)
        


with open("movie_info_classifier/genre_index.json", "w") as f:
    json.dump(genre_index, f, indent=4)

with open("movie_info_classifier/spoken_languages_index.json", "w") as f:
    json.dump(spoken_languages_index, f, indent=4)


print("movie number of short:",len(runtime_index["short"]))
print("movie number of medium:",len(runtime_index["medium"]))
print("movie number of long:",len(runtime_index["long"]))
with open("movie_info_classifier/runtime_index.json", "w") as f:
    json.dump(runtime_index, f, indent=4)


print("movie number of popularity 0-20:",len(popularity_index["0-20"]))
print("movie number of popularity 20-40:",len(popularity_index["20-40"]))
print("movie number of popularity 40-60:",len(popularity_index["40-60"]))
print("movie number of popularity 60-80:",len(popularity_index["60-80"]))
print("movie number of popularity 80-100:",len(popularity_index["80-100"]))
print("movie number of popularity 100+:",len(popularity_index["100+"]))
with open("movie_info_classifier/popularity_index.json", "w") as f:
    json.dump(popularity_index, f, indent=4)

with open("movie_info_classifier/release_date_index.json", "w") as f:
    json.dump(release_date_index, f, indent=4)
# genre_movie={}
# print(movie__info[1]["genres"])


