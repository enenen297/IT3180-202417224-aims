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


class TestCartSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99))
        self.cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        titles = [d.title for d in self.cart.items]
        self.assertEqual(titles, ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        costs = [d.cost for d in self.cart.items]
        self.assertEqual(costs, [24.95, 19.95, 18.99])

    def test_sort_empty_cart(self):
        empty = Cart()
        empty.sort_by_title()
        empty.sort_by_cost()
        self.assertEqual(empty.items, [])


if __name__ == "__main__":
    unittest.main()