from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        # self.__class__.__name__ вместо явного указания названия класса
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __int__(self, books: Book, count_book: int, id_: int):
        self.books = books
        self.count_book = count_book
        self.id_ = id_
        count_book: Optional[int]
        books = list

    def get_next_book_id(self, book: None, count_book: int):
        if book is not None:
            return 1
        else:
            return count_book + 1

    def get_index_by_book_id(self, book: int, id_: int, books: list):
        books = list
        for id_, book in enumerate(books):
            if book in books:
                return id_
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id)  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id)  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
