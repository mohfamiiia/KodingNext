# ==============================================================
# Discount Calculator
# Version: 1.0
# ==============================================================

def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")


def get_price():
    while True:
        try:
            price_input = input("Enter the price of the item: ")

            # Remove currency symbols and separators
            clean_price = (
                price_input.replace("Rp", "")
                .replace("rp", "")
                .replace(",", "")
                .replace(".", "")
                .replace(" ", "")
            )

            price = float(clean_price)

            if price <= 0:
                print("Error: Price must be greater than zero.")
                continue
            
            return price

        except ValueError:
            print("Error: Please enter a valid number for the price.")


def get_discount():
    while True:
        try:
            discount = float(
                input("Enter the discount rate (%): ").replace(",", ".")
            )

            if discount < 0 or discount > 100:
                print("Error: Discount rate must be between 0 and 100.")
                continue

            return discount

        except ValueError:
            print("Error: Please enter a valid number for the discount rate.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity of items: "))

            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue

            return quantity

        except ValueError:
            print("Error: Please enter a valid integer for the quantity.")

def calculate_discount(price, discount, quantity):
    subtotal = price * quantity
    discount_amount = round(subtotal * (discount / 100))
    final_price = subtotal - discount_amount

    return subtotal, discount_amount, final_price

def display_result(price, discount, quantity, subtotal, discount_amount, final_price):
    print("\n" + "=" *45)
    print("DISCOUNT CALCULATION RESULTS")
    print("=" *45)

    print(f"{'Original Price':<22}: {format_rupiah(price)}")
    print(f"{'Quantity':<22}: {quantity}")
    print(f"{'Subtotal':<22}: {format_rupiah(subtotal)}")
    print(f"{'Discount Rate':<22}: {discount:g}%")
    print(f"{'Discount Amount':<22}: -{format_rupiah(discount_amount)}")

    print("-" *45)
    print(f"{'FINAL PRICE':<22}: {format_rupiah(final_price)}")
    print("=" *45)

    print(f"\nYou saved {format_rupiah(discount_amount)} on this purchase!")

def main():
    print("\nWelcome to the Discount Calculator!")
    print("=" * 40)

    price = get_price()
    discount = get_discount()
    quantity = get_quantity()

    subtotal, discount_amount, final_price = calculate_discount(
        price, discount, quantity
    )

    display_result(
        price, discount, quantity, subtotal, discount_amount, final_price
    )

if __name__ == "__main__":
    main()

input("\nPress Enter to exit...")