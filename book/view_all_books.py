from book.book import Book

def view_all_books(book_handler):
    book_dicts = book_handler.load_data()
    
    if not book_dicts:
        print("\n❌ No books available in the inventory.")
        return
    
    print("\n" + "=" * 60)
    print("📚 BOOK INVENTORY 📚".center(60))
    print("=" * 60)
    
    for i, book_dict in enumerate(book_dicts):
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
        
        price_formatted = f"${book.price:.2f}"
        
        publisher = book.publisher if book.publisher else "N/A"
        year = str(book.year_published) if book.year_published else "N/A"
        
        print(f"\n─────────── Book #{i+1} ───────────")
        print(f"📕 Title: {book.title}")
        print(f"✍️  Author: {book.author}")
        print(f"🔢 ISBN: {book.isbn}")
        print(f"📚 Genre: {book.genre}")
        print(f"💰 Price: {price_formatted}")
        print(f"🔢 Quantity: {book.quantity}")
        print(f"🏢 Publisher: {publisher}")
        print(f"📅 Year: {year}")
        print("─" * 30)
    
    print(f"\n✅ Total Books: {len(book_dicts)}")
    
    total_value = sum(float(book['price']) * int(book['quantity']) for book in book_dicts)
    print(f"💵 Total Inventory Value: ${total_value:.2f}")