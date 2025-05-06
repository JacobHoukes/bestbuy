# 🛒 BestBuy – A Console-Based Store Simulator

**BestBuy** is a Python project simulating a basic retail store environment, allowing users to interact with a virtual product catalog, place orders, and apply promotional offers.  
> 🛑 _Note: This project is **not affiliated** with the Best Buy retail chain._

---

## 📚 Features

- 🧾 **Product Catalog** with stock management
- 🛍️ **Order Processing** with quantity validation
- 🎁 **Promotions Engine** (e.g., 30% off, second item half-price, buy 2 get 1 free)
- 📉 **Custom Product Types** like non-stocked or purchase-limited items
- 🧪 **Console-Based Interaction Menu** for listing items, checking stock, and placing orders

---

## 🧾 Example Products & Promotions
When the app starts, it initializes the following products:


- Product	Price	Quantity	Promotion
- MacBook Air M2	1450	100	Second item half-price
- Bose QuietComfort Earbuds	250	500	Buy 2 Get 1 Free
- Google Pixel 7	500	250	-
- Windows License	125	∞	30% off
- Shipping (Limited)	10	250	- (max 1 per order)
  
## 🛒 How Ordering Works
You choose products by number and specify quantities.

Promotions are applied automatically based on the product.

If stock is insufficient or the quantity is invalid, you’ll be notified.

At the end of the session, the total order price is calculated and displayed.

## 💡 Promotions Available
Implemented via subclasses of an abstract Promotion class:

PercentageDiscount: e.g., 30% off

SecondHalfPrice: Buy one at full price, second at half price

Buy2Get1Free: For every 3 items, pay for 2

## 👨‍💻 Author
Developed by Jacob Houkes as a programming exercise.
