class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book(name={self.name}, author={self.author})"

    def __repr__(self):
        return f"Book(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"PaperBook(name={self.name}, author={self.author}, pages={self.pages})"

    def __repr__(self):
        return f"PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"AudioBook(name={self.name}, author={self.author}, duration={self.duration})"

    def __repr__(self):
        return f"AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


# Примеры использования
try:
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)
    print(audio_book)

    # Попробуем установить некорректные значения
    paper_book.pages = -100  # Это вызовет ValueError
except ValueError as e:
    print(e)