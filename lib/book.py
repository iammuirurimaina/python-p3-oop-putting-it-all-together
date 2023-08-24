#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
    def get_page_count(self):
        print ("Getting page count")
        return self._page_count
    def set_page_count(self, page_count):
        if type(page_count)!= int:
            print("page_count must be an integer") 
        else:
            print("setting page count")
            self._page_count = page_count
        
    page_count = property(get_page_count, set_page_count, 'page_count property')
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
      
book1 = Book("harry", 123)
print(book1.page_count)
book1.page_count = 345
print(book1.page_count)
        