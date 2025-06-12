# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Python's built-in operations
#                They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"name: {self.title} || author: {self.author} || pages: {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

book1 = Book("I love God", "Emmanuel", 220)
book2 = Book("Trusting in him", "Oiza", 156)
book3 = Book("Obedience", "Chuks", 367)
book4 = Book("Understanding", "Praise", 123)

print(Book.__str__(book1))
print(book1 == book2)