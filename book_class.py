import os
import shutil
import uuid
from pathlib import Path

from chapter_class import Chapter


class Book:

    def __init__(self, name):
        self.name = name
        self.id = None
        self.chapters_list = []

    def create_book_id(self):
        book_id = uuid.uuid4()
        return book_id

    def create(self):
        os.mkdir(f'data/{self.name}')
        filename = f'data/{self.name}/info.txt'
        self.id = self.create_book_id()
        book_id = f'ID книги - {self.id}\n'
        book_name = f'Название книги - {self.name}\n'
        chapters = f'Количество глав - {len(self.chapters_list)}'
        with open(filename, 'wt', encoding='utf-8') as book:
            book.write(book_id)
            book.write(book_name)
            book.write(chapters)

    def change_name(self, new_name):
        os.rename(self.name, new_name)
        self.name = new_name

    def delete(self):
        shutil.rmtree(self.name)

    def add_chapter(self, chapter_name):
        old_chapters_qty = f"Количество глав - {len(self.chapters_list)}"
        chapter = Chapter(chapter_name)
        self.chapters_list.append(chapter)
        file_chapter = f'data/{self.name}/{chapter_name}.txt'
        with open(file_chapter, 'wt', encoding='utf-8') as chapter:
            chapter.write(chapter_name)
        file_info = f"data/{self.name}/info.txt"
        with open(file_info, 'r', encoding='utf-8') as f:
            old_data = f.read()
        new_chapters_qty = f"Количество глав - {len(self.chapters_list)}"
        new_data = old_data.replace(old_chapters_qty, new_chapters_qty)
        with open(file_info, 'w', encoding='utf-8') as f:
            f.write(new_data)

    def delete_chapter(self, name):
        for i in self.chapters_list:
            if i.chapter_name == name:
                self.chapters_list.remove(i)

    def get_chapters_names_list(self):
        chapters_list = []
        for c in self.chapters_list:
            chapters_list.append(c.chapter_name)
        return chapters_list

    def get_book_list(self):
        folder = 'data'
        books_list = os.listdir(folder)
        for b in books_list:
            file = f'data/{b}/info.txt'
            with open(file, 'rt', encoding='utf-8') as f:
                content = f.read()
                print(content)

