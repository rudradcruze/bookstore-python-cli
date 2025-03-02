from book.book import Book

BOOK_FIELDNAMES = ['title', 'author', 'isbn', 'genre', 'price', 'quantity', 'publisher', 'year_published']

def search_book(book_handler):
    print("\n=== Search for Books ===")

    # Load existing books
    book_dicts = book_handler.load_data()
    if not book_dicts:
        print("No books available to search.")
        return

    print("Available fields to search: title, author, isbn, genre, price, quantity, publisher, year_published")
    field_to_search = None
    valid_fields = set(BOOK_FIELDNAMES)
    while field_to_search is None:
        field_input = input("Enter the field to search by: ").strip().lower()
        if not field_input:
            print("Error: Field cannot be empty.")
        elif field_input not in valid_fields:
            print(f"Error: '{field_input}' is not a valid field. Choose from: {', '.join(valid_fields)}")
        else:
            field_to_search = field_input

    search_value = None
    while search_value is None:
        search_input = input(f"Enter the value to search for in '{field_to_search}': ").strip()
        if not search_input:
            print("Error: Search value cannot be empty.")
        else:
            search_value = search_input.lower()

    matches = []
    for book_dict in book_dicts:
        book_value = book_dict[field_to_search].lower() if book_dict[field_to_search] else ""
        if field_to_search in ['price', 'quantity', 'year_published']:
            try:
                book_num = float(book_value) if field_to_search == 'price' else int(book_value)
                search_num = float(search_value) if field_to_search == 'price' else int(search_value)
                if book_num == search_num:
                    matches.append(book_dict)
            except ValueError:
                if search_value in book_value:
                    matches.append(book_dict)
        else:
            if search_value in book_value:
                matches.append(book_dict)

    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        for book_dict in matches:
            # Create Book object and use its string representation
            book = Book(
                book_dict['title'],
                book_dict['author'],
                book_dict['isbn'],
                book_dict['genre'],
                float(book_dict['price']),
                int(book_dict['quantity']),
                book_dict['publisher'] if book_dict['publisher'] else None,
                int(book_dict['year_published']) if book_dict['year_published'] else None,
                'Bangla'  # Default language value
            )
            print(book)
    else:
        print(f"No books found matching '{search_value}' in '{field_to_search}'.")