BOOK_FIELDNAMES = ['title', 'author', 'isbn', 'genre', 'price', 'quantity', 'publisher', 'year_published']

def search_book(book_handler):
    print("\n=== Search for Books ===")

    # Load existing books
    books = book_handler.load_data()
    if not books:
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
    for book in books:
        book_value = book[field_to_search].lower() if book[field_to_search] else ""
        if field_to_search in ['price', 'quantity', 'year_published']:
            try:
                book_num = float(book_value) if field_to_search == 'price' else int(book_value)
                search_num = float(search_value) if field_to_search == 'price' else int(search_value)
                if book_num == search_num:
                    matches.append(book)
            except ValueError:
                if search_value in book_value:
                    matches.append(book)
        else:
            if search_value in book_value:
                matches.append(book)

    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        for match in matches:
            print(f"Title: {match['title']}, Author: {match['author']}, ISBN: {match['isbn']}, "
                  f"Genre: {match['genre']}, Price: ${match['price']}, Quantity: {match['quantity']}, "
                  f"Publisher: {match['publisher']}, Year: {match['year_published']}")
    else:
        print(f"No books found matching '{search_value}' in '{field_to_search}'.")