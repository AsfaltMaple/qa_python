import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

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

    @pytest.mark.parametrize('book_name, adult_genre', [('Сияние', 'Ужасы'), ('Сто лет одиночества', 'Детективы')])
    def test_get_books_for_children_horror_and_detective_not_for_children(self, book_name, adult_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, adult_genre)
       
        assert collector.books_genre == {book_name: adult_genre}
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_1book(self):
        collector = BooksCollector()
        collector.add_new_book('Чай для чайников')
        collector.add_book_in_favorites('Чай для чайников')

        assert collector.get_list_of_favorites_books() == ['Чай для чайников']

    def test_delete_book_from_favorites_add_2books_remove_1book_1book_left(self):
        collector = BooksCollector()
        collector.add_new_book('Чай для чайников')
        collector.add_new_book('Мыши на крыше')
        collector.add_book_in_favorites('Чай для чайников')
        collector.add_book_in_favorites('Мыши на крыше')
        collector.delete_book_from_favorites('Чай для чайников')

        assert collector.get_list_of_favorites_books() == ['Мыши на крыше']

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Чай для чайников')
        collector.add_new_book('Мыши на крыше')
        collector.add_book_in_favorites('Чай для чайников')
        collector.add_book_in_favorites('Мыши на крыше')

        assert collector.get_list_of_favorites_books() == ['Чай для чайников', 'Мыши на крыше']
    
   