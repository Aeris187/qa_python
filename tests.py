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
        assert len(collector.get_books_rating()) == 2


class TestBooksCollector:

    # добавление книги в избранное

        def test_add_book_in_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Властелин колец')
            collector.add_book_in_favorites('Властелин колец')
            assert 'Властелин колец' in collector.get_list_of_favorites_books()



     # удаление книги из избранного

        def test_delete_book_from_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Девушка с татуировкой дракона')
            collector.add_book_in_favorites('Девушка с татуировкой дракона')
            collector.delete_book_from_favorites('Девушка с татуировкой дракона')
            assert [] == collector.get_list_of_favorites_books()


     # получаем список Избранных книг

        def test_get_list_of_favorites_books(self):
            collector = BooksCollector()
            collector.add_new_book('Девушка с татуировкой дракона')
            collector.add_new_book('Властелин колец')
            collector.add_book_in_favorites('Властелин колец')
            collector.add_book_in_favorites('Девушка с татуировкой дракона')
            assert 'Властелин колец' in collector.get_list_of_favorites_books() and 'Девушка с татуировкой дракона' in collector.get_list_of_favorites_books()

    #   проверка на удаление несуществующей книги из избранного

        def test_delete_book_from_favorites_delete_nonexist_book_from_list(self):
            collector = BooksCollector()
            collector.delete_book_from_favorites('Три товарища')
            assert len(collector.get_list_of_favorites_books()) == 0

    # проверка на установку книге жанра

        def test_set_book_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Звездные войны')
            collector.set_book_genre('Звездные войны', 'Фантастика')
            assert collector.get_book_genre('Звездные войны') == 'Фантастика'

    # проверка на вывод списка книг с определённым жанром

        def test_get_books_with_specific_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Дюна')
            collector.add_new_book('Трон')
            collector.set_book_genre('Трон', 'Фантастика')
            collector.set_book_genre('Дюна', 'Фантастика')
            assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    # проверка на получение словаря books_genre

        def test_get_books_genre(self):
            collector = BooksCollector()
            genre = 'Фантастика'
            collector.add_new_book('Дюна')
            collector.set_book_genre('Дюна', genre)
            assert collector.get_book_genre('Дюна') == genre

    # проверка на получение книг для детей

        def test_get_books_for_children(self):
            collector = BooksCollector()
            collector.add_new_book('Алиса в стране чудес')
            collector.add_new_book('Dune')
            collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
            collector.set_book_genre('Dune', 'Детектив')
            assert len(collector.get_books_for_children()) == 1

     # добавление новой книги

        def test_add_new_book_two_items_with_similar_name(self):
            collector = BooksCollector()

            collector.add_new_book('Мастер и Маргарита')
            collector.add_new_book('Мастер и Маргарита')

            assert len(collector.get_books_genre()) == 1

