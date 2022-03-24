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
    #actors_list: str

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
                    actors_list = list(row[5].replace(", u'", ' ').split(" "))
                    #actors_list = conver_string(row[5])
                )
                print(movie)
                js_txt_line = movie.json()
                output_stream.write(js_txt_line)
                output_stream.write("\n")


#def test_list(file_name):
    from itertools import groupby
    with open(file_name, "r", newline="") as input_stream:

        csv_reader = csv.reader(input_stream)
        for stream in csv_reader:
            #print(stream[5])
            list_str = list(stream[5].split("u'"))
            list_str.remove(list_str[0])
            world = list(list_str.pop())# last world и удалили из списка это слово
            #print(world)# as  list
            world.pop()
            world.pop()
            correct_world = "".join(world)

            a = get_correct_name(list_str)
            a.append(correct_world)
            print(a)


def conver_string(str): # метод который на вход принимает строку и отдает правильный лист
    list_str = list(str.split("u'"))
    list_str.remove(list_str[0])
    world = list(list_str.pop())  # last world и удалили из списка это слово
    world.pop()
    world.pop()
    correct_world = "".join(world)

    correct_list = get_correct_name(list_str)
    correct_list.append(correct_world)
    print(correct_list)#  это лист
    return correct_list


def get_correct_name(list_world):
    correct_list_world = []
    i = 0
    while i < len(list_world):
        world = list(list_world[i])
        world.pop()
        world.pop()
        world.pop()
        correct_world = "".join(world)
        correct_list_world.append(correct_world)
        i += 1
    return correct_list_world



def test_converter():
    input_file_name = "move.csv"
    output_file_name = "newMovieJson2.json"
    #test_list(input_file_name)
    #conver_string("[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunton']")
    convert_csv_json(input_file_name, output_file_name)


if __name__ == "__main__":
    test_converter()
