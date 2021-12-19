from random import choice


def get_random_photo():
    placeholders = [
        'default_book_1.jpg',
        'default_book_2.jpg',
        'default_book_3.jpg',
        'default_book_4.jpg',
        'default_book_5.jpg',
    ]

    return 'book_images/' + choice(placeholders)