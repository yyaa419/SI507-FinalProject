from flask import Flask, render_template, request
import json
from bs4 import BeautifulSoup
import requests

def test(genre, language, runtime, release_date):
    print("Welcpme to the movie recommendation system!")
    print(f"{genre}, {language}, {runtime}, {release_date}")

def getFinalMovieList(user_genre, user_spoken_languages, user_runtime, user_release_date):
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

    genre_filtered_movie=genre_info[user_genre]
    spoken_languages_filtered_movie=spoken_languages_info[user_spoken_languages]
    runtime_filtered_movie=runtime_info[user_runtime]
    release_date_filtered_movie=release_date_info[user_release_date]

    final_movie_list=[]
    for movie in genre_filtered_movie:
        if movie in spoken_languages_filtered_movie and movie in runtime_filtered_movie and movie in release_date_filtered_movie:
            final_movie_list.append(movie)
    
    with open("final_movie_list.json", "w") as f:
        json.dump(final_movie_list, f, indent=4)
        print("final_movie_list has been saved.")
    
    return final_movie_list
    
def getFinalMovieListWithScore():
    final_movie_list=json.load(open("final_movie_list.json"))
    sorted_movie_list=sorted(final_movie_list, key=lambda k: k['popularity'], reverse=True)
    movie_count=0
    for movie in sorted_movie_list:
        movie_name=movie["title"]
        movie_name_processed=movie_name.replace(" ","%20")
        rotten_tomatoes_url=f"https://www.rottentomatoes.com/search?search={movie_name_processed}"
        response = requests.get(rotten_tomatoes_url)
        soup = BeautifulSoup(response.text, "html.parser")
        movie_divs=soup.find("div", { "id" :"search-results"})
        movie_div=movie_divs.find("search-page-result",{"type":"movie"})
        movie_info=movie_div.find("search-page-media-row")
        score=movie_info["tomatometerscore"]
        movie_count+=1
        movie["tomato_score"]=score
        print(movie_name, ":", movie["popularity"], score)

    output_file_path="final_movie_list_with_score.json"
    with open(output_file_path, "w") as f:
        json.dump(sorted_movie_list, f, indent=4)
        print("final_movie_list_with_score has been saved.")

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def load():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    genre = request.form.get("genre")
    language = request.form.get("spoken_languages")
    runtime = request.form.get("length")
    release_date = request.form.get("release_date")
    print(f"{genre}, {language}, {runtime}, {release_date}")
    getFinalMovieList(genre, language, runtime, release_date)
    getFinalMovieListWithScore()
    movie_list = json.load(open("final_movie_list_with_score.json"))
    return render_template("result.html", movies=movie_list)

@app.route('/other')
def other():
    # Redirect to the root page
    return load()


if __name__ == "__main__":
    print('starting Flask app', app.name)
    app.run(debug=True)