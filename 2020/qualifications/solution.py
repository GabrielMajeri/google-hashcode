import argparse
from collections import namedtuple


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
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
