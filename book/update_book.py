from book.book import Book

def update_book(book_handler):
    print("\n=== Update a Book ===")

    books = book_handler.load_data()
    if not books:
        print("No books available to update.")
        return

    isbn_to_update = None
    while isbn_to_update is None:
        isbn_input = input("Enter the ISBN of the book to update: ").strip()
        if not isbn_input:
            print("Error: ISBN cannot be empty.")
        else:
            isbn_to_update = isbn_input

    book_to_update = None
    for book in books:
        if book['isbn'] == isbn_to_update:
            book_to_update = book
            break 

    if not book_to_update:
        print(f"Error: No book found with ISBN '{isbn_to_update}'.")
        return

    print(f"\nFound book: {book_to_update['title']} by {book_to_update['author']}")
    print("Enter new values (or press Enter to keep the current value).")

    title = None
    while title is None:
        title_input = input(f"Enter new title [{book_to_update['title']}]: ").strip()
        if not title_input:
            title = book_to_update['title']  # Keep existing value
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in title_input):
            print("Error: Title must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            title = title_input

    author = None
    while author is None:
        author_input = input(f"Enter new author [{book_to_update['author']}]: ").strip()
        if not author_input:
            author = book_to_update['author']
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in author_input):
            print("Error: Author must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            author = author_input

    genre = None
    while genre is None:
        genre_input = input(f"Enter new genre [{book_to_update['genre']}]: ").strip()
        if not genre_input:
            genre = book_to_update['genre']
        elif not all(c.isalpha() or c.isspace() for c in genre_input):
            print("Error: Genre must contain only letters or spaces.")
        else:
            genre = genre_input

    price = None
    while price is None:
        price_input = input(f"Enter new price [{book_to_update['price']}]: ").strip()
        if not price_input:
            price = float(book_to_update['price'])
        else:
            try:
                price_value = float(price_input)
                if price_value <= 0:
                    print("Error: Price must be a positive number.")
                else:
                    price = price_value
            except ValueError:
                print("Error: Price must be a valid number.")

    quantity = None
    while quantity is None:
        quantity_input = input(f"Enter new quantity [{book_to_update['quantity']}]: ").strip()
        if not quantity_input:
            quantity = int(book_to_update['quantity'])
        else:
            try:
                quantity_value = int(quantity_input)
                if quantity_value < 0:
                    print("Error: Quantity must be a non-negative integer.")
                else:
                    quantity = quantity_value
            except ValueError:
                print("Error: Quantity must be a valid integer.")

    publisher = None
    while publisher is None:
        publisher_input = input(f"Enter new publisher [{book_to_update['publisher']}]: ").strip()
        if not publisher_input and not book_to_update['publisher']:
            publisher = None
        else:
            publisher = publisher_input if publisher_input else book_to_update['publisher']

    year_published = None
    while year_published is None:
        year_input = input(f"Enter new year published [{book_to_update['year_published']}]: ").strip()
        if not year_input:
            year_published = int(book_to_update['year_published']) if book_to_update['year_published'] else None
        else:
            try:
                year_value = int(year_input)
                if 1000 <= year_value <= 2025:
                    year_published = year_value
                else:
                    print("Error: Year must be between 1000 and 2025.")
            except ValueError:
                print("Error: Year must be a valid integer.")

    updated_book = Book(title, author, isbn_to_update, genre, price, quantity, publisher, year_published)

    updated_books = []
    for book in books:
        if book['isbn'] == isbn_to_update:
            updated_books.append({
                'title': updated_book.title,
                'author': updated_book.author,
                'isbn': updated_book.isbn,
                'genre': updated_book.genre,
                'price': str(updated_book.price),
                'quantity': str(updated_book.quantity),
                'publisher': updated_book.publisher if updated_book.publisher else '',
                'year_published': str(updated_book.year_published) if updated_book.year_published else ''
            })
        else:
            updated_books.append(book)

    book_handler.save_data(updated_books)
    print(f"\nBook with ISBN '{isbn_to_update}' has been successfully updated.")