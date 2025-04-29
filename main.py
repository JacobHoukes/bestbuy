import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum_per_order=1)
                ]

# Create the store instance
best_buy = store.Store(product_list)

# Create promotion catalog
second_half_price = products.SecondHalfPrice("Second Half price!")
third_one_free = products.Buy2Get1Free("Third One Free!")
thirty_percent = products.PercentageDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start():
    """Displays the menu options to the user."""
    print(f"\n    Store Menu\n    ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products():
    """Lists all active products in the store."""
    print("------")
    for product in best_buy.get_all_products():
        print(product.show())
    print("------")


def show_item_amount():
    """Displays the total quantity of all products in the store."""
    total_quantity = best_buy.get_total_quantity()
    print(f"\nTotal of {total_quantity} items in store")


def make_order():
    """Allows the user to make an order by selecting products and quantities."""
    products_in_store = best_buy.get_all_products()
    if not products_in_store:
        print("No active products available for purchase.")
        return
    shopping_list = []

    print("------")
    product_number = 1
    for product in products_in_store:
        product_info = product.show()
        product_info = product_info.replace("Price:", "Price: $")
        print(f"{product_number}. {product_info}")
        product_number += 1
    print("------")

    print("When you want to finish order, enter empty text.")
    while True:
        try:
            product_choice = input("Which product # do you want? ")
            if product_choice.strip() == "":
                break
            product_index = int(product_choice)
            if product_index < 1 or product_index > len(products_in_store):
                raise ValueError
            quantity_input = input("What amount do you want? ")
            quantity = int(quantity_input)
            selected_product = products_in_store[product_index - 1]
            shopping_list.append((selected_product, quantity))
            print("Product added to list!\n")
        except ValueError:
            print("Error adding product!\n")
    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"Order made!\nTotal price of your order is: {total_price}")
        except ValueError as e:
            print(f"Error while processing your order: {e}")
    else:
        print("No items ordered.")


def main():
    """Main interaction loop for the store."""
    while True:
        start()
        user_choice = input("Please choose a number: ")

        if user_choice == "1":
            list_products()
        elif user_choice == "2":
            show_item_amount()
        elif user_choice == "3":
            make_order()
        elif user_choice == "4":
            break
        else:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    main()
