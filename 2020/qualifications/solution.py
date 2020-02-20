import matplotlib.pyplot as plt
import argparse
from collections import namedtuple
import sys


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()


class lib:
    books = []
    singup_time = 0
    books_per_day = 0
    id = 0

    def __init__(self, books, singup_time, books_per_day, id):
        self.books = books
        self.singup_time = singup_time
        self.books_per_day = books_per_day
        self.id = id

    def __repr__(self):
        return '( books: ' + str(self.books) + ' singup_time: ' + str(self.singup_time) + ' books_per_day: ' + str(self.books_per_day) + ' )'

    def __str__(self):
        return '( books: ' + str(self.books) + ' singup_time: ' + str(self.singup_time) + ' books_per_day: ' + str(self.books_per_day) + ' )'


next_id = 0
with open(args.input_file) as fin:
    # num_books - number of unique books
    # num_libraries - number of unique libraries
    # num_days - number of available days
    num_books, num_libraries, num_days = map(int, next(fin).split())
    print(f"Total of {num_books} books in {num_libraries} libraries")
    print(f"Available time: {num_days} days")

    scores = [int(x) for x in next(fin).split()]

    libraries = []
    for i in range(num_libraries):
        n, signup_time, books_per_day = map(int, next(fin).split())

        books = [int(x) for x in next(fin).split()]
        libraries.append((lib(books, signup_time, books_per_day, next_id)))
        next_id += 1


libraries.sort(key=lambda x: x.books_per_day)

with open(args.output_file, "w") as fout:
    print(num_libraries, file=fout)
    for idx, lib in enumerate(libraries):
        print(lib.id, len(lib.books), file=fout)
        print(*lib.books, file=fout)
