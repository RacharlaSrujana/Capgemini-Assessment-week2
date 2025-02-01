'''You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to 
    display book details.'''

class Book:
    def __init__(self,isbn,title,author):
        self.isbn=isbn
        self.title=title
        self.author=author
    def display_book_details(self):
        print(f"isbn : {self.isbn}, title : {self.title}, author : {self.author}")
book1=Book(101,"Geetanjali","Rabindranath Tagore")
book2=Book(102,"Wings of Fire","Abdul Kalam")
book1.display_book_details()
book2.display_book_details()