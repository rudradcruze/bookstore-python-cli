from book.book import Book
from payment import Payment
from data_handler import DataHandler
import datetime

PURCHASE_FIELDNAMES = ['username', 'isbn', 'title', 'quantity', 'total_amount', 'payment_method', 'purchase_date']

def buy_book(book_handler, purchase_handler, current_user):
    print("\n=== Buy a Book ===")

    books = book_handler.load_data()
    if not books:
        print("No books available to buy.")
        return

    isbn_to_buy = None
    while isbn_to_buy is None:
        isbn_input = input("Enter the ISBN of the book to buy: ").strip()
        if not isbn_input:
            print("Error: ISBN cannot be empty.")
        else:
            isbn_to_buy = isbn_input

    book_to_buy = None
    for book in books:
        if book['isbn'] == isbn_to_buy:
            book_to_buy = book
            break

    if not book_to_buy:
        print(f"Error: No book found with ISBN '{isbn_to_buy}'.")
        return

    if int(book_to_buy['quantity']) <= 0:
        print(f"Error: '{book_to_buy['title']}' is out of stock.")
        return

    print(f"\nBook found: {book_to_buy['title']} by {book_to_buy['author']}")
    print(f"Price: ${float(book_to_buy['price']):.2f}")
    print(f"Available Quantity: {book_to_buy['quantity']}")

    quantity_to_buy = None
    while quantity_to_buy is None:
        try:
            qty_input = int(input("Enter quantity to buy: "))
            if qty_input <= 0:
                print("Error: Quantity must be a positive integer.")
            elif qty_input > int(book_to_buy['quantity']):
                print(f"Error: Only {book_to_buy['quantity']} available in stock.")
            else:
                quantity_to_buy = qty_input
        except ValueError:
            print("Error: Quantity must be a valid integer.")

    total_amount = float(book_to_buy['price']) * quantity_to_buy
    print(f"Total amount to pay: ${total_amount:.2f}")

    payment_method = None
    while payment_method is None:
        method_input = input("Enter payment method (card/cash): ").strip().lower()
        if method_input not in ['card', 'cash']:
            print("Error: Please choose 'card' or 'cash'.")
        else:
            payment_method = method_input

    payment_processor = Payment()
    if payment_processor.process_payment(total_amount, payment_method):
        updated_books = []
        for book in books:
            if book['isbn'] == isbn_to_buy:
                updated_quantity = int(book['quantity']) - quantity_to_buy
                book['quantity'] = str(updated_quantity)
                print(f"Updated stock for '{book['title']}': {updated_quantity}")
            updated_books.append(book)
        
        book_handler.save_data(updated_books)

        # Save purchase record
        purchase_record = {
            'username': current_user.username,
            'isbn': isbn_to_buy,
            'title': book_to_buy['title'],
            'quantity': str(quantity_to_buy),
            'total_amount': str(total_amount),
            'payment_method': payment_method,
            'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        purchase_handler.append_data(purchase_record)

        print(f"\nPurchase successful! You bought {quantity_to_buy} copy(ies) of '{book_to_buy['title']}'.")
    else:
        print("Payment failed. Purchase cancelled.")