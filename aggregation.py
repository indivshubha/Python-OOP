
class Library:
    def __init__(self, name):
        self.name = name
        self.books=[]

    def addBook(self, book):
        self.books.append(book)

    def listBooks(self):
        return [f"{book.title} by {book.author}"for book in self.books]

class Books():
    def __init__(self,title,author):
        self.title=title
        self.author=author

library=Library("New York Public")

book1=Books("Harry Potter...","JK Rowling")
book2=Books("The Hobbit","J. R. R. Toklein")
book3=Books("The Colour of Magic","Terry Pratchet")

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

print(library.name)

for book in library.listBooks():
    print(book)
