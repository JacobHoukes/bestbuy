import products


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """Adds an active product to the store (if not already added)."""
        if product.is_active() and product not in self.product_list:
            self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Returns all products in the store that are active"""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order
        """
        total_price = 0
        for product, quantity in shopping_list:
            if quantity > product.quantity:
                raise ValueError(f"Not enough '{product.name}' in stock.")
            else:
                total_price += product.buy(quantity)
        return total_price


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]


def main():
    best_buy = Store(product_list)
    available_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(available_products[0], 1), (available_products[1], 2)]))


if __name__ == "__main__":
    main()
