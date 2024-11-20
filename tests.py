from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверка установки жанра книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        # добавляю книггу
        collector.add_new_book('1984')
        # устанавливаю жанр
        collector.set_book_genre('1984', 'Фантастика')

        # проверка что жанр установился
        assert collector.get_book_genre('1984') == 'Фантастика'

    # проверка установки жанра для книги котроой нет
    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()

        # устанавливаем жанр для несуществующей книги
        collector.set_book_genre('Несуществующая книга', 'Фантастика')

        # проверка что ничего не изменилось
        assert collector.get_books_genre() == {}

    # проверка получения книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем жанры
        collector.add_new_book('1984')
        collector.add_new_book('Мир Дикого Запада')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Мир Дикого Запада', 'Фантастика')

        # проверка списка книг с жанром "Фантастика"
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['1984', 'Мир Дикого Запада']

    # проверка получения книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()

        # Добавляем книги с разными жанрами
        collector.add_new_book('1984')
        collector.add_new_book('Мир Дикого Запада')
        collector.add_new_book('Детские сказки')
        collector.set_book_genre('1984', 'Ужасы')
        collector.set_book_genre('Мир Дикого Запада', 'Фантастика')
        collector.set_book_genre('Детские сказки', 'Мультфильмы')

        # проверка, что вернулись только книги без возрастного ограничения
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Мир Дикого Запада', 'Детские сказки']

    # проверка добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        # добавляем книгу и заносим в избранное
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        # проверка, что книга в избранном
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['1984']

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        # добавляем книгу в избранное, а затем удаляем
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')

        # проверка что избранное пустое
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    # проверка получения жанра книги
    def test_get_book_genre(self):
        collector = BooksCollector()

        # добавляю книгу с жанром
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        # проверяю жанр
        genre = collector.get_book_genre('1984')
        assert genre == 'Фантастика'

    # проверка получения всех книг с жанрами
    def test_get_books_genre(self):
        collector = BooksCollector()

        # добавляю книги
        collector.add_new_book('1984')
        collector.add_new_book('Мир Дикого Запада')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Мир Дикого Запада', 'Ужасы')

        # проверяю словарь книг и жанров
        books_genre = collector.get_books_genre()
        assert books_genre == {
            '1984': 'Фантастика',
            'Мир Дикого Запада': 'Ужасы'
        }