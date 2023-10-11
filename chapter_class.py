import os


class Chapter:

    def __init__(self, chapter_name):
        self.chapter_name = chapter_name

    def __str__(self):
        return self.chapter_name

    def rename_chapter(self, book_name, new_name):
        os.rename(f'data/{book_name}/{self.chapter_name}.txt', f'data/{book_name}/{new_name}.txt')
        self.chapter_name = new_name
        file_chapter = f'data/{book_name}/{self.chapter_name}.txt'
        with open(file_chapter, 'wt', encoding='utf-8') as chapter:
            chapter.write(self.chapter_name)



