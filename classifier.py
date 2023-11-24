import json

genre_info=json.load(open("genre_index.json"))
genre_type=[]
for genre in genre_info:
    genre_type.append(genre)

spoken_languages_info=json.load(open("spoken_languages_index.json"))
spoken_languages_type=[]
for spoken_language in spoken_languages_info:
    spoken_languages_type.append(spoken_language)

runtime_info=json.load(open("runtime_index.json"))
runtime_type=[]
for runtime in runtime_info:
    runtime_type.append(runtime)

release_date_info=json.load(open("release_date_index.json"))
release_date_type=[]
for release_date in release_date_info:
    release_date_type.append(release_date)


if __name__ == "__main__":
    print("Welcpme to the movie recommendation system!")

    print("We offer genres like: ")
    print(genre_type)
    user_genre=input("Please enter your favorite genre: ")
    genre_filtered_movie=genre_info[user_genre]

    print("We offer spoken languages like: ")
    print(spoken_languages_type)
    user_spoken_languages=input("Please enter your favorite spoken language: ")
    spoken_languages_filtered_movie=spoken_languages_info[user_spoken_languages]

    print("We offer runtime like: ")
    print(runtime_type)
    user_runtime=input("Please enter your favorite runtime: ")
    runtime_filtered_movie=runtime_info[user_runtime]

    print("We offer release date like: ")
    print(release_date_type)
    user_release_date=input("Please enter your favorite release date: ")
    release_date_filtered_movie=release_date_info[user_release_date]


    final_movie_list=[]
    for movie in genre_filtered_movie:
        if movie in spoken_languages_filtered_movie and movie in runtime_filtered_movie and movie in release_date_filtered_movie:
            final_movie_list.append(movie)
    
    # final_movie_list.unique()
    print(final_movie_list)
    print(len(final_movie_list))
    with open("final_movie_list.json", "w") as f:
        json.dump(final_movie_list, f, indent=4)
        print("final_movie_list has been saved.")
    
    with open("test.json", "w") as f:
        json.dump(genre_filtered_movie, f, indent=4)
