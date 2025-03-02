class Payment:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Payment, cls).__new__(cls)
        return cls._instance

    def process_payment(self, amount, payment_method):
        if payment_method.lower() not in ['card', 'cash']:
            print(f"Error: Invalid payment method '{payment_method}'. Use 'card' or 'cash'.")
            return False
        
        if payment_method.lower() == 'card':
            card_number = input("Enter card number (16 digits): ").strip()
            if not card_number.isdigit() or len(card_number) != 16:
                print("Error: Invalid card number. Must be 16 digits.")
                return False
            print(f"Processing card payment of ${amount:.2f}...")
            # Simulate card processing
            print("Payment successful via card!")
            return True
        
        elif payment_method.lower() == 'cash':
            while True:
                try:
                    cash_received = float(input(f"Enter cash amount received (minimum ${amount:.2f}): "))
                    if cash_received < amount:
                        print(f"Error: Amount received (${cash_received:.2f}) is less than required (${amount:.2f}).")
                    else:
                        change = cash_received - amount
                        print(f"Payment successful via cash! Change: ${change:.2f}")
                        return True
                except ValueError:
                    print("Error: Please enter a valid cash amount.")
        return False