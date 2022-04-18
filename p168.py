class Book:
    def __init__(self,bookname,author,price,published):
        self.book_name = bookname
        self.book_author = author
        self.book_price = price
        self.book_published = published
        
    def add_citizen(self):
        print("Book Name: "+self.book_name)
        print("Author: "+self.book_author)
        print("Price: "+str(self.book_price))
        print("Publish Date: "+self.book_published)
        print("Book Added")
        
        
        
book1 = Book("Harry Potter","J. K. Kennedy",198, "1997")
book1.add_citizen()
