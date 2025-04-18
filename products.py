class Product:
    """
    This function initializes a new Product instance with the given name, price, and quantity.
    It validates that the name is a non-empty string, the price is a non-negative number,
    and the quantity is a non-negative integer. If any of the inputs are invalid, it raises a ValueError.
    The product is set as active by default.
    """

    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("The name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("The price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity must be a non-negative number.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """This function returns the quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity):
        """This is the setter function for quantity. If the quantity reaches 0, the product is deactivated."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity must be a non-negative whole number.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """This function returns True if the product is active, otherwise it returns False."""
        return self.active

    def activate(self):
        """This function activates the product."""
        self.active = True

    def deactivate(self):
        """This function deactivates the product."""
        self.active = False

    def show(self):
        """This function returns a string representing the product,
        e.g. 'MacBook Air M2, Price: 1450, Quantity: 100'"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """This function reduces the quantity by the given amount. It deactivates product if the quantity hits 0."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("The purchase quantity must be a positive whole number.")
        if not self.active:
            raise Exception("This product is inactive. You can unfortunately not purchase it.")
        if quantity > self.quantity:
            raise Exception("There is not enough of this product in stock to complete the purchase.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        total_price = self.price * quantity
        return total_price


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
