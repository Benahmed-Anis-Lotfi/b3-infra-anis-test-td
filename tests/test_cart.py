import unittest
from order import Order
from cart import Cart 
from product import Product

class TestDiscount(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Produit 1", 10, 10)
        

    def test_calculate_total_with_discount(self):
        cart = Cart()
        cart.add_product(self.product1, 10)
        self.assertGreater(cart.calculate_total_with_discount(), 90) 

if __name__ == "__main__":
    unittest.main(buffer=False)