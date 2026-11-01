import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD → phải thành công
        for i in range(20):
            dvd = DigitalVideoDisc(title=f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        # DVD thứ 21 → phải bị từ chối
        extra_dvd = DigitalVideoDisc(title="DVD 21")
        self.assertFalse(cart.add_dvd(extra_dvd))


if __name__ == "__main__":
    unittest.main()