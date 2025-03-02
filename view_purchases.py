from data_handler import DataHandler
from book.book import Book
from user.user import User

def view_purchases(purchase_handler, book_handler=None, user_handler=None, username=None):
    purchases = purchase_handler.load_data()

    if username:
        purchases = [p for p in purchases if p['username'] == username]
    
    books = book_handler.load_data() if book_handler else []
    users = user_handler.load_data() if user_handler else []
    
    # Create dictionaries for quick lookup
    book_dict = {book['isbn']: book for book in books}
    user_dict = {user['username']: user for user in users}
    
    print("\n" + "=" * 70)
    print("💰 PURCHASE RECORDS 💰".center(70))
    print("=" * 70)
    
    if not purchases:
        print("\n❌ No purchase records available.")
        return
    
    print(f"\n✅ Found {len(purchases)} purchase record(s)")
    
    # Calculate total revenue
    total_revenue = sum(float(purchase['total_amount']) for purchase in purchases)
    print(f"💵 Total Revenue: ${total_revenue:.2f}")
    
    # Print each purchase with details
    for i, purchase in enumerate(purchases):
        print("\n" + "─" * 70)
        print(f"🧾 PURCHASE #{i+1} - {purchase['purchase_date']}".center(70))
        print("─" * 70)
        
        print(f"\n🛒 TRANSACTION DETAILS:")
        print(f"   📝 Quantity: {purchase['quantity']}")
        print(f"   💰 Total Amount: ${float(purchase['total_amount']):.2f}")
        print(f"   💳 Payment Method: {purchase['payment_method']}")
        print(f"   📅 Date: {purchase['purchase_date']}")
        
        print(f"\n👤 CUSTOMER INFORMATION:")
        if username or user_dict.get(purchase['username']):
            user_data = user_dict.get(purchase['username'], {})
            print(f"   🆔 Username: {purchase['username']}")
            if user_data:
                print(f"   👤 Full Name: {user_data.get('full_name', 'N/A')}")
                print(f"   📧 Email: {user_data.get('email', 'N/A')}")
                print(f"   🔑 Role: {user_data.get('role', 'N/A')}")
            else:
                print(f"   ℹ️ No additional customer details available")
        else:
            print(f"   🆔 Username: {purchase['username']}")
            print(f"   ℹ️ No additional customer details available")
        
        print(f"\n📚 BOOK INFORMATION:")
        print(f"   📕 Title: {purchase['title']}")
        print(f"   🔢 ISBN: {purchase['isbn']}")
        
        if book_dict.get(purchase['isbn']):
            book_data = book_dict.get(purchase['isbn'])
            print(f"   ✍️ Author: {book_data.get('author', 'N/A')}")
            print(f"   📚 Genre: {book_data.get('genre', 'N/A')}")
            print(f"   💰 Current Price: ${float(book_data.get('price', 0)):.2f}")
            print(f"   🏢 Publisher: {book_data.get('publisher', 'N/A')}")
            print(f"   📅 Year Published: {book_data.get('year_published', 'N/A')}")
        else:
            print(f"   ℹ️ No additional book details available")