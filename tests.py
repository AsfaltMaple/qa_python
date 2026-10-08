import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_books_collector_init(self):
            collector = BooksCollector()
            assert collector.books_genre == {}
            assert collector.favorites == []
            assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
            assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book_name, genre', [('Хроники Амбера', 'Фантастика'), ('Сияние', 'Ужасы'),('Сто лет одиночества', 'Детективы'), ('Смешарики', 'Мультфильмы'),('Мыши на крыше', 'Комедии')])
    def test_add_new_book_add_1book_existing_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre', [('Хроники Амбера', 'Фантастика'), ('Сияние', 'Ужасы'),('Сто лет одиночества', 'Детективы'), ('Смешарики', 'Мультфильмы'),('Мыши на крыше', 'Комедии')])
    def test_get_books_with_specific_genre_1book_in_each_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name, genre', [('Сияние', 'Ужасы'),('Сто лет одиночества', 'Детективы')])
    def test_get_books_with_specific_genre_not_for_children(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name, children_genre', [('Хроники Нарнии', 'Фантастика'), ('Смешарики', 'Мультфильмы'), ('Вредные советы', 'Комедии')])
    def test_get_books_for_children_fantasy_cartoon_comedy_for_children(self, book_name, children_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, children_genre)
        assert collector.books_genre == {book_name: children_genre}
        assert collector.get_books_for_children() == [book_name]
    
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

    @pytest.mark.parametrize('book_name', ['Чай для чайников', 'Мыши на крыше'])
    def test_get_list_of_favorites_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]
    
    def test_add_new_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Чай для чайников')
        assert collector.books_genre == {'Чай для чайников': ''}

