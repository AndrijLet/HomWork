class Book:
    def __init__(self, title, author, page_content):
        self.title = title
        self.author = author
        self.page_content = page_content

    def get_content(self):
        return self.page_content

class Printer:
    def print_page(selfself, book):
            print(f"Printing... {book.get_content()}")
# Логіка виводу на пристрій відокремлена від моделі даних
my_book = Book("Clean code", "Robert Martin", "Chapter 1: Simplicity")
my_printer = Printer()
my_printer.print_page(my_book)

