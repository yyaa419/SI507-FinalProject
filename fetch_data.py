import os
from request import request_movie_info
from data_preprocess import process_movie_info

MOVIE_PAGE_NUMBER = 29

def count_files(directory_path):
    try:
        # List all files in the specified directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        
        # Return the count of files
        return len(files)

    except FileNotFoundError:
        print(f"The specified directory '{directory_path}' does not exist.")
        return None

if __name__ == "__main__":
    directory_path = "movie_info/"
    files_count = count_files(directory_path)

    if files_count is not None and files_count >= MOVIE_PAGE_NUMBER:
        print(f"There are {files_count} files in the directory '{directory_path}'.")
        print("There already existed enough cache files for the relavent movie information.")
        print("Requst part is done, now starting to process the data...")
    elif files_count is not None and files_count < MOVIE_PAGE_NUMBER:
        print(f"There are {files_count} files in the directory '{directory_path}'.")
        print("There are not enough cache files for the relavent movie information.")
        print("Starting requesting data from the API...")
        request_movie_info()
        print("Requst part is done, now starting to process the data...")
    else:
        print("The directory is not found.")
        print("Starting requesting data from the API...")
        request_movie_info()
        print("Requst part is done, now starting to process the data...")
    
    process_movie_info()
    print("Preprocessing is done!")
    print("Now you can run the main.py to start the web application.")