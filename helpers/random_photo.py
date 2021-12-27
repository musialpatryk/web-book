from random import choice

book_placeholders = [
    'default_book_1.jpg',
    'default_book_2.jpg',
    'default_book_3.jpg',
    'default_book_4.jpg',
    'default_book_5.jpg',
]

authors_placeholders = [
    'default_author_1.jpg',
    'default_author_2.jpg',
    'default_author_3.jpg',
]

def get_random_photo(path, books=True):
    placeholders = book_placeholders if books else authors_placeholders
    return path + choice(placeholders)