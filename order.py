# order.py

from cart import Cart


class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total_with_discount()
        self.cart = cart

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€"
    
    def print_items_list(self):
        total_items = self.cart.calculate_total_items()
        print(f"Le nombre total d'articles dans le panier est : {total_items}")
        return total_items
