from book.book import Book

def view_all_books(book_handler):
    """Display all books in a simple format using Book objects."""
    book_dicts = book_handler.load_data()
    if not book_dicts:
        print("No books available.")
    else:
        print("\n=== All Books ===")
        for book_dict in book_dicts:
            book = Book(
                book_dict['title'],
                book_dict['author'],
                book_dict['isbn'],
                book_dict['genre'],
                float(book_dict['price']),
                int(book_dict['quantity']),
                book_dict['publisher'] if book_dict['publisher'] else None,
                int(book_dict['year_published']) if book_dict['year_published'] else None
            )
            # Use the Book object's string representation
            print(book)