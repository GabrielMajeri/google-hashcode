import argparse
from collections import defaultdict, namedtuple
import sys


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()


Library = namedtuple("Library", ("books", "signup_time", "books_per_day"))


print(">> Processing", args.input_file, "to", args.output_file)

with open(args.input_file) as fin:
    # num_books - number of unique books
    # num_libraries - number of unique libraries
    # num_days - number of available days
    num_books, num_libraries, num_days = map(int, next(fin).split())
    print(f"Total of {num_books} books in {num_libraries} libraries")
    print(f"Available time: {num_days} days")

    scores = [int(x) for x in next(fin).split()]
    print("Max possible score:", sum(scores))

    libraries = [None] * num_libraries
    libraries_by_book = defaultdict(list)

    for library_index in range(num_libraries):
        n, signup_time, books_per_day = map(int, next(fin).split())

        books = [int(x) for x in next(fin).split()]
        for book in books:
            libraries_by_book[book].append(library_index)

        libraries[library_index] = Library(books, signup_time, books_per_day)

max_by_score = sorted(range(num_books), key=lambda book: scores[book], reverse=True)

chosen_libraries = []
chosen_books = defaultdict(list)
current_last_time = 0
start_time = {}
queue_time = defaultdict(float)

# Try taking as many books as possible, decreasing by score
for book in max_by_score:
    if not libraries_by_book[book]:
        continue

    possible_libraries = libraries_by_book[book]
    best_library = possible_libraries[0]
    best_time = possible_libraries[0]

    # See from which library we will take it
    for possible_library in possible_libraries[1:]:
        if possible_library in chosen_libraries:
            lib_time = start_time[possible_library] + queue_time[possible_library]
        else:
            lib_time = current_last_time + libraries[possible_library].signup_time

        if lib_time < best_time:
            best_time = lib_time
            best_library = possible_library

    if best_library not in chosen_libraries:
        chosen_libraries.append(best_library)
        start_time[best_library] = current_last_time
        current_last_time += libraries[best_library].signup_time

    chosen_books[best_library].append(book)
    queue_time[best_library] += 1 / libraries[best_library].books_per_day


with open(args.output_file, "w") as fout:
    print(len(chosen_libraries), file=fout)
    for idx in chosen_libraries:
        print(idx, len(chosen_books[idx]), file=fout)
        print(*chosen_books[idx], file=fout)
