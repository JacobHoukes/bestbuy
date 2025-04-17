from tkinter.font import names


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        """Returns the quantity (int)"""
        pass

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        pass

    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        pass

    def activate(self):
        """Activates the product"""
        pass

    def deactivate(self):
        """Deactivates the product"""
        pass

    def show(self):
        """Returns a string that represents the product, e.g. 'MacBook Air M2, Price: 1450, Quantity: 100'"""
        pass

    def buy(self, quantity):
        """Buys a given quantity of the product; returns the total price (float) of the purchase;
        and updates the quantity of the product"""
        pass


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
