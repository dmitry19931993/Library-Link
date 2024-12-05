import json
from typing import List, Dict

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """
        Преобразует объект книги в словарь.
        :return: Словарь, содержащий поля объекта книги:
                 - id: уникальный идентификатор книги (int)
                 - title: название книги (str)
                 - author: автор книги (str)
                 - year: год издания книги (int)
                 - status: статус книги, например, "в наличии" или "выдана" (str)
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

class Library:
    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.books = self._load_books()

    def _load_books(self) -> List[Book]:
        """
        Загружает книги из файла data.json.
        Если файл отсутствует или содержит некорректные данные, возвращает пустой список.
        """
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("Формат данных в файле некорректен.")
                return [Book(
                    book_id=book["id"],
                    title=book["title"],
                    author=book["author"],
                    year=book["year"],
                    status=book["status"]
                ) for book in data]
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)
            return []

    def _save_books(self):
        """
        Сохраняет книги в файл data.json.
        """
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def is_book_exists(self, title: str, author: str, year: int) -> bool:
        """
        Проверяет, существует ли книга с таким же названием, автором и годом издания в библиотеке.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :return: True, если книга существует; False, если нет.
        """
        return any(
            book.title.lower() == title.lower() and
            book.author.lower() == author.lower() and
            book.year == year
            for book in self.books
        )

    def validate_id(self, book_id: str) -> int | None:
        """
        Проверяет, что переданный ID является числом.
        :param book_id: ID книги в виде строки.
        :return: Корректный ID в виде целого числа или None, если проверка не прошла.
        """
        try:
            return int(book_id)
        except ValueError:
            print("Ошибка: ID книги должен быть числом.")
            return None

    def add_book(self, title: str, author: str, year: int):
        """
        Добавляет новую книгу в библиотеку.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        if not (1800 <= year <= 2024):
            print("Ошибка: Год книги должен быть в диапазоне от 1800 до 2024.")
            return

        if self.is_book_exists(title, author, year):
            print("Ошибка: Книга с таким названием, автором и годом уже существует в библиотеке.")
            return

        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self._save_books()
        print(f"Книга '{title}' успешно добавлена с ID {new_id}.")

    def remove_book(self, book_id: int):
        """
        Удаляет книгу по ID из библиотеки.
        :param book_id: ID книги.
        """

        validated_id = self.validate_id(book_id)
        if validated_id is None:
            return

        for book in self.books:
            if book.id == validated_id:
                self.books.remove(book)
                self._save_books()
                print(f"Книга с ID {validated_id} успешно удалена.")
                return

        print("Ошибка: Книга с таким ID не найдена.")

    def search_books(self, query: str, field: str):
        """
        Ищет книги по указанному полю.
        :param query: строка для поиска.
        :param field: поле для поиска ('title', 'author', 'year').
        """

        valid_fields = {'title', 'author', 'year'}
        if field not in valid_fields:
            print("Ошибка: Некорректное поле для поиска.")
            return
        found_books = [book for book in self.books if query.lower() in str(getattr(book, field)).lower()]
        if not found_books:
            print("Книги по вашему запросу не найдены.")
        else:
            for book in found_books:
                print(f"[ID: {book.id}] {book.title} — {book.author} ({book.year}), Статус: {book.status}")

    def change_status(self, book_id: int, new_status: str):
        """
        Изменяет статус книги в библиотеке по её уникальному идентификатору (ID).
        :param book_id: Уникальный идентификатор книги (int).
        :param new_status: Новый статус книги (str). Допустимые значения: "в наличии" или "выдана".
        :return: None. Выводит сообщение об успешной операции или об ошибке.
        Логика работы:
        - Проверяет, что ID книги является числом (используется метод validate_id).
        - Проверяет, что переданный статус является допустимым значением.
        - Если книга с указанным ID найдена, её статус изменяется на новый, данные сохраняются.
        - Если книга с указанным ID не найдена или статус некорректен, выводится сообщение об ошибке.
        """

        validated_id = self.validate_id(book_id)
        if validated_id is None:
            return
        if new_status not in {'в наличии', 'выдана'}:
            print("Ошибка: Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
            return
        for book in self.books:
            if book.id == validated_id:
                book.status = new_status
                self._save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print("Ошибка: Книга с таким ID не найдена.")

    def display_books(self):
        """
        Отображает список всех книг в библиотеке.
        Если библиотека пуста, выводит соответствующее сообщение. В противном случае,
        выводит список всех книг с их ID, названием, автором, годом издания и статусом.
        :return: None. Выводит информацию о книгах на экран.
        """
        if not self.books:
            print("Библиотека пуста.")
            return

        print("Список книг:")
        for book in self.books:
            print(f"[ID: {book.id}] {book.title} — {book.author} ({book.year}), Статус: {book.status}")