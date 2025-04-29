from abc import ABC


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
        self.promotion = None

    def get_quantity(self):
        """This function returns the quantity (int)"""
        return self.quantity

    def set_quantity(self, quantity):
        """This is the setter function for quantity. If the quantity reaches 0, the product is deactivated"""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("The quantity must be a non-negative whole number.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """This function returns True if the product is active, otherwise it returns False"""
        return self.active

    def activate(self):
        """This function activates the product"""
        self.active = True

    def deactivate(self):
        """This function deactivates the product"""
        self.active = False

    def show(self):
        """This function returns a string representing the product,
         e.g. 'MacBook Air M2, Price: 1450, Quantity: 100'
         including promotion if exists."""
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No Promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promo_info}"

    def get_promotion(self):
        """This function returns the promotion applied to the product."""
        return self.promotion

    def set_promotion(self, promotion):
        """This function sets a promotion on the product."""
        self.promotion = promotion

    def buy(self, quantity):
        """This function reduces the quantity by the given amount.
        It deactivates product if the quantity hits 0.
        If promotion exists, apply it to price."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("The purchase quantity must be a positive whole number.")
        if not self.active:
            raise RuntimeError("This product is inactive. You can unfortunately not purchase it.")
        if quantity > self.quantity:
            raise RuntimeError("There is not enough of this product in stock to complete the purchase.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return total_price


class NonStockedProduct(Product):
    """A product that doesn't track quantity (like digital licenses)"""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Overrides Products method set_quantity to disable quantity changes for non-stocked products"""
        pass

    def buy(self, quantity):
        """Allows buying without affecting quantity"""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("The purchase quantity must be a positive whole number.")
        if not self.active:
            raise RuntimeError("This product is inactive. You can unfortunately not purchase it.")
        total_price = self.price * quantity
        return total_price

    def show(self):
        """Show product information indicating it is non-stocked"""
        return f"{self.name} (non-stocked), Price: {self.price}"


class LimitedProduct(Product):
    """A product that can only be bought in limited quantity per order"""

    def __init__(self, name, price, quantity, maximum_per_order):
        super().__init__(name, price, quantity)
        if not isinstance(maximum_per_order, int) or maximum_per_order <= 0:
            raise ValueError("The maximum per order must be a positive whole number.")
        self.maximum_per_order = maximum_per_order

    def buy(self, quantity):
        """Buy only up to maximum_per_order"""
        if quantity > self.maximum_per_order:
            raise ValueError(f"You can only purchase up to {self.maximum_per_order} of this item per order.")
        return super().buy(quantity)

    def show(self):
        """Show product information including the purchase limit"""
        return f"{self.name} (Limited to {self.maximum_per_order} per order), Price: {self.price}, Quantity: {self.quantity}"


class Promotion(ABC):
    """Abstract base class for all promotions"""

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        """Apply the promotion and return the total discounted price"""
        pass


class PercentageDiscount(Promotion):
    """Applies a percentage discount on the product"""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount


class SecondHalfPrice(Promotion):
    """Every second item is at half price"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total


class Buy2Get1Free(Promotion):
    """For every two items bought, get a third item for free"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        payable_quantity = quantity - (quantity // 3)
        total = product.price * payable_quantity
        return total


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
