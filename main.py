# This is a sample Python script.
from pydantic import BaseModel
import csv
import json

class Movie(BaseModel):
    star_rating: float
    title: str
    content_rating: str
    genre: str
    duration: int
    actors_list: list[str]

def convert_csv_json(file_name, out_path):
    with open(file_name, "r", newline="") as input_stream:
        reader = csv.reader(input_stream)
        with open(out_path, 'w') as output_stream:
            for row in reader:  # row - list

                #print(movie.star_rating, movie.title, movie.content_rating,movie.genre,movie.duration)
                movie: Movie = Movie(
                    star_rating=row[0],
                    title = row[1],
                    content_rating = row[2],
                    genre = row[3],
                    duration = row[4],
                    #actors_list = list(row[5].replace(", u'", ' ').split(" "))
                    actors_list = eval(row[5])
                )
                print(row[5])
                print(movie)

                js_txt_line = movie.json()
                output_stream.write(js_txt_line)
                output_stream.write("\n")


def test_converter():
    input_file_name = "move.csv"
    input_file_name = "imdb_1000.csv"
    output_file_name = "newMovieJson2.json"

    convert_csv_json(input_file_name, output_file_name)


if __name__ == "__main__":
    test_converter()
