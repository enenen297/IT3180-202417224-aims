import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearchByCategory(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Aladdin", "Animation", "John Musker", 90, 18.99),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
        ]

    def test_match(self):
        result = search_by_category(self.items, "Animation")
        self.assertEqual([d.title for d in result], ["The Lion King", "Aladdin"])

    def test_case_insensitive(self):
        result = search_by_category(self.items, "animation")
        self.assertEqual(len(result), 2)

    def test_no_match(self):
        self.assertEqual(search_by_category(self.items, "Horror"), [])

    def test_empty_list(self):
        self.assertEqual(search_by_category([], "Animation"), [])


class TestSearchByTitleTrim(unittest.TestCase):
    def test_keyword_with_spaces(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(len(search_by_title(items, "  lion ")), 1)

    def test_no_match(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(search_by_title(items, "xyz"), [])


if __name__ == "__main__":
    unittest.main()