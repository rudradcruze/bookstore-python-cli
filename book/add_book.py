from book.book import Book

def add_book(book_handler):
    print("\n=== Add a New Book ===")

    existing_books = book_handler.load_data()
    existing_isbns = {book['isbn'] for book in existing_books}

    title = None
    while title is None:
        title_input = input("Enter book title: ").strip()
        if not title_input:
            print("Error: Title cannot be empty.")
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in title_input):
            print("Error: Title must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            title = title_input

    author = None
    while author is None:
        author_input = input("Enter author name: ").strip()
        if not author_input:
            print("Error: Author cannot be empty.")
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in author_input):
            print("Error: Author must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            author = author_input

    isbn = None
    while isbn is None:
        isbn_input = input("Enter ISBN (e.g., 978-0-123456-47-2): ").strip()
        if not isbn_input:
            print("Error: ISBN cannot be empty.")
        elif isbn_input in existing_isbns:
            print("Error: This ISBN is already in use. Each book must have a unique ISBN.")
        else:
            isbn = isbn_input

    genre = None
    while genre is None:
        genre_input = input("Enter genre: ").strip()
        if not genre_input:
            print("Error: Genre cannot be empty.")
        elif not all(c.isalpha() or c.isspace() for c in genre_input):
            print("Error: Genre must contain only letters or spaces.")
        else:
            genre = genre_input

    price = None
    while price is None:
        try:
            price_input = float(input("Enter price (e.g., 12.99): "))
            if price_input <= 0:
                print("Error: Price must be a positive number.")
            else:
                price = price_input
        except ValueError:
            print("Error: Price must be a valid number.")

    quantity = None
    while quantity is None:
        try:
            quantity_input = int(input("Enter quantity in stock: "))
            if quantity_input < 0:
                print("Error: Quantity must be a non-negative integer.")
            else:
                quantity = quantity_input
        except ValueError:
            print("Error: Quantity must be a valid integer.")

    publisher = input("Enter publisher (optional, press Enter to skip): ").strip() or None

    year_published = None
    while year_published is None:
        year_input = input("Enter year published (optional, press Enter to skip): ").strip()
        if not year_input:
            year_published = None
        else:
            try:
                year_published_temp = int(year_input)
                if 1000 <= year_published_temp <= 2025:
                    year_published = year_published_temp
                else:
                    print("Error: Year must be between 1000 and 2025.")
            except ValueError:
                print("Error: Year must be a valid integer.")

    new_book = Book(title, author, isbn, genre, price, quantity, publisher, year_published)

    book_dict = {
        'title': new_book.title,
        'author': new_book.author,
        'isbn': new_book.isbn,
        'genre': new_book.genre,
        'price': str(new_book.price),
        'quantity': str(new_book.quantity),
        'publisher': new_book.publisher if new_book.publisher else '',
        'year_published': str(new_book.year_published) if new_book.year_published else ''
    }

    book_handler.append_data(book_dict)
    print(f"\nBook '{title}' added successfully!")