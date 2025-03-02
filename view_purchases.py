from data_handler import DataHandler

PURCHASE_FIELDNAMES = ['username', 'isbn', 'title', 'quantity', 'total_amount', 'payment_method', 'purchase_date']

def view_purchases(purchase_handler):
    print("\n=== View All Purchases ===")

    purchases = purchase_handler.load_data()
    if not purchases:
        print("No purchase records available.")
        return

    print(f"Found {len(purchases)} purchase(s):")
    for purchase in purchases:
        print(f"Username: {purchase['username']}, "
              f"Book: {purchase['title']} (ISBN: {purchase['isbn']}), "
              f"Quantity: {purchase['quantity']}, "
              f"Total Amount: ${float(purchase['total_amount']):.2f}, "
              f"Payment Method: {purchase['payment_method']}, "
              f"Date: {purchase['purchase_date']}")