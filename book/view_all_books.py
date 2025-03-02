def view_all_books(book_handler):
    """Display all books in a simple format."""
    books = book_handler.load_data()
    if not books:
        print("No books available.")
    else:
        print("\n=== All Books ===")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, "
                  f"Genre: {book['genre']}, Price: ${book['price']}, Quantity: {book['quantity']}")