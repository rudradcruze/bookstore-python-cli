def delete_book(book_handler):
    print("\n=== Remove a Book ===")

    books = book_handler.load_data()
    if not books:
        print("No books available to delete.")
        return

    isbn_to_delete = None
    while isbn_to_delete is None:
        isbn_input = input("Enter the ISBN of the book to delete: ").strip()
        if not isbn_input:
            print("Error: ISBN cannot be empty.")
        else:
            isbn_to_delete = isbn_input

    book_found = False
    updated_books = []
    for book in books:
        if book['isbn'] == isbn_to_delete:
            book_found = True
            print(f"Deleting book: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
        else:
            updated_books.append(book)

    if book_found:
        book_handler.save_data(updated_books)
        print(f"Book with ISBN '{isbn_to_delete}' has been successfully removed.")
    else:
        print(f"Error: No book found with ISBN '{isbn_to_delete}'.")