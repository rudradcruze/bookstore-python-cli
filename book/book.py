class Book:
    def __init__(self, title, author, isbn, genre, price, quantity, publisher=None, year_published=None, language='Bangla'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.publisher = publisher
        self.year_published = year_published
        self.language = language

    def __str__(self):
        base_info = f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, " \
                    f"Genre: {self.genre}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
        if self.publisher or self.year_published:
            extra_info = []
            if self.publisher:
                extra_info.append(f"Publisher: {self.publisher}")
            if self.year_published:
                extra_info.append(f"Year: {self.year_published}")
            return f"{base_info}, {' '.join(extra_info)}"
        return base_info