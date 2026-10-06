from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_books_collector_init(self):
            collector = BooksCollector()
            assert collector.books_genre == {}
            assert collector.favorites == []
            assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
            assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_1book_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хроники Амбера')
        collector.set_book_genre('Хроники Амбера', 'Фантастика')

        assert collector.get_book_genre('Хроники Амбера') == 'Фантастика'

    def test_get_books_with_specific_genre_1book_detective(self):
        collector = BooksCollector()
        collector.add_new_book('Сто лет одиночества')
        collector.set_book_genre('Сто лет одиночества', 'Детективы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Сто лет одиночества']

    def test_get_books_with_specific_genre_1book_horror_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние']
        assert collector.get_books_for_children() == []


    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        #collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()