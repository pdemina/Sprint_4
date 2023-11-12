import pytest

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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre.keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['', 'эта строка должна состоять более чем из 41 символов'])
    def test_add_new_book_without_name_and_with_long_name_is_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre.keys()) == 0

    def test_set_book_genre_existing_genre_is_added(self):
        collector = BooksCollector()
        name='Гордость и предубеждение'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.books_genre[name] == 'Фантастика'

    def test_set_book_genre_not_existing_genre_is_not_added(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'AФантастика')
        assert collector.books_genre[name] == ''

    def test_get_book_genre_returns_genre_of_existing_book_with_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'

    #def test_get_books_with_specific_genre_returns_books_with_selected_genre




