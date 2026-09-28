class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 5

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.get_total()

        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n==================== BILL ====================")
        print(f"{'Product':<20}{'Price':<10}{'Qty':<8}{'Total':<10}")
        print("-" * 48)

        for product in self.products:
            total = product.get_total()

            print(
                f"{product.name:<20}"
                f"{product.price:<10.2f}"
                f"{product.quantity:<8}"
                f"{total:<10.2f}"
            )

        print("-" * 48)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax (5%): ₹{tax:.2f}")
        print(f"Final Total: ₹{total:.2f}")
        print("==============================================")


bill = Bill()

print("===== BILLING SYSTEM =====")

while True:
    name = input("\nEnter product name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product = Product(name, price, quantity)
        bill.add_product(product)

        print("Product added successfully.")

    except ValueError:
        print("Please enter valid price and quantity.")

if bill.products:
    bill.display_bill()
else:
    print("No products were added.")