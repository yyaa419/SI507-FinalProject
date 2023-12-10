import json

import matplotlib.pyplot as plt
import numpy as np

# jsonFile={
#         "adult": False,
#         "backdrop_path": None,
#         "belongs_to_collection": None,
#         "budget": 0,
#         "genres": [
#             {
#                 "id": 18,
#                 "name": "Drama"
#             }
#         ],
#         "homepage": "",
#         "id": 499376,
#         "imdb_id": "tt5909292",
#         "original_language": "ja",
#         "original_title": "\u30a2\u30cb\u30d0\u30fc\u30b5\u30ea\u30fc",
#         "overview": "",
#         "popularity": 2.358,
#         "poster_path": "/cekZGSxdazM874fy5LJyvnNdrE4.jpg",
#         "production_companies": [
#             {
#                 "id": 529,
#                 "logo_path": "/rwB6w2aPENQbx756pBWSw44Ouk.png",
#                 "name": "Production I.G",
#                 "origin_country": "JP"
#             },
#             {
#                 "id": 130168,
#                 "logo_path": None,
#                 "name": "atmovie",
#                 "origin_country": "JP"
#             },
#             {
#                 "id": 17228,
#                 "logo_path": "/7agfWcZa25AD8QKvSf9IbLlsQzA.png",
#                 "name": "T-JOY",
#                 "origin_country": "JP"
#             }
#         ],
#         "production_countries": [
#             {
#                 "iso_3166_1": "JP",
#                 "name": "Japan"
#             }
#         ],
#         "release_date": "2016-10-22",
#         "revenue": 0,
#         "runtime": 109,
#         "spoken_languages": [
#             {
#                 "english_name": "Japanese",
#                 "iso_639_1": "ja",
#                 "name": "\u65e5\u672c\u8a9e"
#             }
#         ],
#         "status": "Released",
#         "tagline": "",
#         "title": "Anniversary",
#         "video": False,
#         "vote_average": 0.0,
#         "vote_count": 0
#     }

# language_list=["English","Japanese","Chinese","Korean","German","French","Thai"]
# movie_language=jsonFile["spoken_languages"][0]["english_name"]

# if movie_language not in language_list:
#     print("no")
# else:  
#     print("yes")

score_list=[]
movie_count=0

for page_number in range(1, 30):
    movie_json = json.load(open(f"movie_info/movie_info_page{page_number}.json"))
    for movie in movie_json:
        movie_count += 1
        if movie["popularity"] > 100:
            continue
        score_list.append(movie["popularity"])

plt.hist(score_list, bins=20, color='blue', edgecolor='black')
plt.title('Popularity Score Histogram')
plt.xlabel('Popularity Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
print(movie_count)
plt.show()

