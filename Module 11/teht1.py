class Release:
    def __init__(self,name):
        self.name = name
class Paper(Release):
    def __init__(self, name, publisher):
        self.publisher = publisher
        super().__init__(name)

    def print_info(self):
        print(f"Paper {self.name} by {self.publisher}")

class Book(Release):
    def __init__(self, name, writher, pages):
        super().__init__(name)
        self.writher = writher
        self.pages = pages

    def print_info(self):
        print(f"Book {self.name}, {self.pages} pages by {self.writher}")


b = Book("Hytti n:o 6","Rosa Liksom", "200")

p = Paper("Aku Ankka", "Aki Hyyppä")

p.print_info()
b.print_info()