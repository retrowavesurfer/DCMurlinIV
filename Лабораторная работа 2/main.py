class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

# Примеры использования
book = Book(1, 'test_name_1', 200)
print(book)          # Вывод: Книга "test_name_1"
print(repr(book))    # Вывод: Book(id_=1, name='test_name_1', pages=200)
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# Примеры использования
library = Library()
print(library.get_next_book_id())  # Вывод: 1

book1 = Book(1, 'test_name_1', 200)
library.books.append(book1)

print(library.get_next_book_id())  # Вывод: 2

book2 = Book(2, 'test_name_2', 300)
library.books.append(book2)

print(library.get_index_by_book_id(1))  # Вывод: 0
print(library.get_index_by_book_id(2))  # Вывод: 1

# Попытка получить индекс несуществующей книги
try:
    print(library.get_index_by_book_id(3))  # Вывод: ValueError
except ValueError as e:
    print(e)  # Вывод: Книги с запрашиваемым id не существует