import json

def readGraph():
    genre_info=json.load(open("movie_info_classifier/genre_index.json"))
    genre_type=[]
    for genre in genre_info:
        genre_type.append(genre)

    spoken_languages_info=json.load(open("movie_info_classifier/spoken_languages_index.json"))
    spoken_languages_type=[]
    for spoken_language in spoken_languages_info:
        spoken_languages_type.append(spoken_language)

    runtime_info=json.load(open("movie_info_classifier/runtime_index.json"))
    runtime_type=[]
    for runtime in runtime_info:
        runtime_type.append(runtime)

    release_date_info=json.load(open("movie_info_classifier/release_date_index.json"))
    release_date_type=[]
    for release_date in release_date_info:
        release_date_type.append(release_date)
    
    return genre_type, spoken_languages_type, runtime_type, release_date_type


if __name__ == "__main__":
    readGraph()