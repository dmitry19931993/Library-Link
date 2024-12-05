from library_manager import Library

def main():
    library = Library()

    while True:
        print("\nДобро пожаловать в систему управления библиотекой!\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Изменить статус книги")
        print("5. Показать все книги")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания (1800-2024): "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: Год должен быть числом.")
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)
        elif choice == "3":
            field = input("По какому полю искать (title, author, year): ")
            query = input("Введите строку поиска: ")
            library.search_books(query, field)
        elif choice == "4":
            book_id = input("Введите ID книги: ")
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.change_status(book_id, new_status)
        elif choice == "5":
            library.display_books()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Некорректный выбор.")

if __name__ == "__main__":
    main()