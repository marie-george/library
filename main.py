from book_class import Book

print("Привет! Мы тут пишем книги! Хотите поучаствовать?")
take_part = input("Если да, нажмите 'y', если хотите завершить программу нажмите 'n' ")


if take_part == 'y':
    book_name = input("Придумай название книги ")
    book = Book(book_name)
    book.create()
    print(f'Отлично! Вы создали книгу с названием {book_name}')
    while True:
        action = input("Если вы хотите изменить название книги, нажмите 'c'\n"
                       "Если вы хотите удалить книгу, нажмите 'd'\n"
                       "Если вы хотите добавить к книге главу, нажмите '+'\n"
                       "Если вы хотите вывести весь список книг, нажмите 'a'\n"
                       "Если вы хотите завершить программу нажмите 'n'")
        if action == 'c':
            new_name = input('Введите новое название книги ')
            print(f"Отлично! Название книги изменено на {new_name}")
            book.change_name(new_name)
        if action == 'd':
            book.delete()
            print('Книга удалена')
            print("Нам очень жаль, что вы не захотели стать писателем! Удачи в других профессиях!")
            break
        if action == '+':
            chapter_name = input('Введите название главы ')
            print(f"Отлично! Вы создали главу {chapter_name}")
            book.add_chapter(chapter_name)
            chapters_list = book.get_chapters_names_list()
            print(f'Список глав: {chapters_list}')
            while True:
                chapter_action = input("Если вы хотите переименовать какую-то главу, нажмите 'r'\n"
                                       "Если вы хотите удалить какую-то главу, нажмите 'o'\n"
                                       "Если вы хотите выйти в предыдущее меню (работа с книгой), нажмите 'f'")
                if chapter_action == 'r':
                    old_name = input('Введите название главы, которую вы хотите переименовать ')
                    new_name = input('Введите новое наименование главы ')
                    for i in book.chapters_list:
                        if i.chapter_name == old_name:
                            i.rename_chapter(book.name, new_name)
                    print(f"Отлично! Глава переименована в {new_name}")
                    chapters_list = book.get_chapters_names_list()
                    print(f'Список глав: {chapters_list}')
                if chapter_action == 'o':
                    to_delete = input('Введите название главы, которую вы хотите удалить ')
                    book.delete_chapter(to_delete)
                    print(f"Отлично! Глава {to_delete} удалена")
                    chapters_list = book.get_chapters_names_list()
                    print(f'Список глав: {chapters_list}')
                if chapter_action == 'f':
                    break
        if action == 'a':
            book.get_book_list()
        if action == 'n':
            print("Нам очень жаль, что вы не захотели стать писателем! Удачи в других профессиях!")
            break

else:
    print("Нам очень жаль, что вы не захотели стать писателем! Удачи в других профессиях!")
