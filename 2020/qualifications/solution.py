import argparse
from collections import namedtuple
import sys
from heapq import heappush, heappop



parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()


Library = namedtuple("Library", ("books", "signup_time", "books_per_day"))

with open(args.input_file) as fin:
    # num_books - number of unique books
    # num_libraries - number of unique libraries
    # num_days - number of available days
    num_books, num_libraries, num_days = map(int, next(fin).split())
    print(f"Total of {num_books} books in {num_libraries} libraries")
    print(f"Available time: {num_days} days")

    scores = [int(x) for x in next(fin).split()]

    libraries = [None] * num_libraries
    for i in range(num_libraries):
        n, signup_time, books_per_day = map(int, next(fin).split())

        books = [int(x) for x in next(fin).split()]

        libraries[i] = Library(books, signup_time, books_per_day)


lib_by_max_score = []


def calculating_sums_library(index_library):
    suma = 0
    for i in range(len(libraries[index_library].books)):
        suma += scores[libraries[index_library].books[i]]
    lib_by_max_score.append((suma, index_library))


#Apeluri functii
for i in range(num_libraries):
    calculating_sums_library(i)

lib_by_max_score.sort(reverse=True)

#print(lib_by_max_score)

print("Oficial output")

def printing_solution():
    with open(args.output_file) as fou:
        print(num_libraries,file=fou)

        for i in range(len(lib_by_max_score)):
            print(lib_by_max_score[i][1] , len(libraries[lib_by_max_score[i][1]].books), file = fou)
            print(libraries[lib_by_max_score[i][1]].books, file=fou)

printing_solution()
