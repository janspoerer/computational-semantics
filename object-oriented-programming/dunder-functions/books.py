class Book:
    def __init__(self, name, authors, isbn, no_of_pages):
        self.name = name
        self.authors = [authors]
        self.isbn = isbn
        self.no_of_pages = no_of_pages

    def __str__(self):
        res = "Name: " + self.name
        res = res + " // ISBN: " + self.isbn
        for author in self.authors:
            res = res + " // " + str(author)
        res = res + "// number of pages: " + str(self.no_of_pages)
        return res

    def __ge__(self, other):
        return self.no_of_pages >= other.no_of_pages

    def __le__(self, other):
        return self.no_of_pages <= other.no_of_pages

    def __gt__(self, other):
        return self.no_of_pages > other.no_of_pages

    def __eq__(self, other):
        return self.no_of_pages == other.no_of_pages
