class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        print(f"Книга {self.title} от {self.author}")


fav_book = Book('1984', 'Orwell')
fav_book.description()