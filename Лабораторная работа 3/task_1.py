class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, pages_: int) -> None:
        if not isinstance(pages_, int):
            raise TypeError("Значение должно быть типа int")
        if pages_ <= 0:
            raise ValueError("Значение быть положительным числом")
        self.pages = pages_


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, {self.duration!r})"

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration_check: float) -> None:
        if not isinstance(duration_check, float):
            raise TypeError("Значение должно быть типа float")
        if duration_check <= 0:
            raise ValueError("Значение быть положительным числом")
        self.duration = duration_check
