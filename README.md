
# Библиотека — консольное приложение для управления книгами

## Описание

Это консольное приложение предназначено для управления библиотекой книг. Оно позволяет пользователям добавлять книги, удалять их, искать, изменять статус и просматривать все книги, содержащиеся в библиотеке. Каждая книга имеет уникальный идентификатор и может иметь два возможных статуса: "в наличии" или "выдана".

Программа хранит данные о книгах в JSON файле, что позволяет сохранять информацию между запусками приложения.

---

## Функционал

### 1. **Добавление книги**

Пользователи могут добавлять книги в библиотеку, вводя следующие данные:
- **Название книги (title)**
- **Автор книги (author)**
- **Год издания книги (year)**

После добавления книги в библиотеку ей будет автоматически присвоен уникальный идентификатор (ID), а статус книги будет установлен как **"в наличии"**.

### 2. **Удаление книги**

Пользователи могут удалить книгу из библиотеки, указав её уникальный идентификатор (ID). Если книга с таким ID не существует, приложение выведет ошибку.

### 3. **Поиск книги**

Пользователи могут искать книги в библиотеке по одному или нескольким параметрам:
- **Название книги (title)**
- **Автор книги (author)**
- **Год издания книги (year)**

Поиск будет выполнен по одному или нескольким критериям, в зависимости от введенных данных.


### 4. **Изменение статуса книги**

Пользователи могут изменить статус книги по её уникальному идентификатору (ID). Статус может быть установлен как **"в наличии"** или **"выдана"**.


### 5. **Отображение всех книг**

Приложение может вывести список всех книг в библиотеке, отображая для каждой книги:
- **ID** — уникальный идентификатор книги
- **Название** — название книги
- **Автор** — автор книги
- **Год издания** — год издания книги
- **Статус** — текущий статус книги ("в наличии" или "выдана")

---

## Установка и запуск

Для работы с приложением вам необходимо иметь установленный Python версии 3.x.

### 1. Клонирование репозитория:

```bash
git clone https://your-repository-url.git
cd your-project-directory
```

### 2. Установка зависимостей:

Для работы приложения не требуются сторонние библиотеки, все необходимое уже включено в стандартную библиотеку Python.

### 3. Запуск:

Для запуска приложения используйте команду:

```bash
python main.py
```

Программа начнёт работать и предложит выбрать действие из списка доступных опций.

---

## Пример работы приложения

**1. Добавление книги:**

```
Введите название книги: Война и мир
Введите автора книги: Лев Толстой
Введите год издания книги: 1869
Книга 'Война и мир' успешно добавлена с ID 1.
```

**2. Удаление книги:**

```
Введите ID книги для удаления: 1
Книга с ID 1 успешно удалена.
```

**3. Отображение всех книг:**

```
Список книг:
[ID: 1] Война и мир — Лев Толстой (1869), Статус: в наличии
[ID: 2] Преступление и наказание — Фёдор Достоевский (1866), Статус: выдана
```

---

## Структура проекта

```
main.py            # Основной файл с меню приложения
librery_manager    # Файл с логикой приложения
data.json          # Файл для хранения данных о книгах
README.md          # Этот файл с описанием проекта
```

---

## Разработчик

Это приложение было разработано как тестовое задание для проверки навыков программирования на языке Python.

---

### Дополнительные функции 

- Аннотирование типов в коде
- Подробная документация
- Написание тестов для проверки функционала
- Реализация объектно-ориентированного подхода в коде