from collections import namedtuple


Library = namedtuple("Library", ("books", "signup_time", "books_per_day"))


num_books, num_libraries, num_days = map(int, input().split())
print(f"Total of {num_books} books in {num_libraries} libraries")
print(f"Available time: {num_days} days")

scores = [int(x) for x in input().split()]

libraries = [None] * num_libraries
for i in range(num_libraries):
    n, signup_time, books_per_day = map(int, input().split())

    books = [int(x) for x in input().split()]

    libraries[i] = Library(books, signup_time, books_per_day)
