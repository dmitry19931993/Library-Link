import unittest
from library_manager import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        """Тестирование добавления книги"""
        count_library_books = len(self.library.books)
        self.library.add_book(title="Анна Каренина", author="Лев Толстой", year=1877)
        self.assertEqual(len(self.library.books), count_library_books + 1)
        self.assertEqual(self.library.books[-1].title, "Анна Каренина")


    def test_invalid_status_change(self):
        """Тестирование ошибки при попытке изменить статус на некорректный"""
        self.library.change_status(self.library.books[-1].id, "не существует")
        self.assertEqual(self.library.books[-1].status, "выдана")

    def test_change_status(self):
        """Тестирование изменения статуса книги"""
        self.library.change_status(self.library.books[-1].id, "выдана")
        self.assertEqual(self.library.books[-1].status, "выдана")


    def test_remove_book(self):
        """Тестирование удаления книги"""

        count_library_books = len(self.library.books)
        self.library.remove_book(self.library.books[-1].id)
        self.assertEqual(len(self.library.books), count_library_books - 1)

    def test_remove_nonexistent_book(self):
        """Тестирование удаления несуществующей книги"""

        count_library_books = len(self.library.books)
        self.library.remove_book(999)
        self.assertEqual(len(self.library.books), count_library_books)

if __name__ == '__main__':
    unittest.main()
