import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(
            DigitalVideoDisc("Test DVD", cost=100)
        )

    def test_discount_20_percent(self):
        """Giỏ 100$, giảm 20% thì còn 80$."""
        result = self.cart.total_cost_with_discount(20)

        self.assertEqual(result, 80)

    def test_invalid_discount_percent(self):
        """Phần trăm giảm giá không hợp lệ phải báo lỗi."""
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()