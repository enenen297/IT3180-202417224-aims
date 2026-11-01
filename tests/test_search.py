import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title



class TestSearchByTitleTrim(unittest.TestCase):
    def test_keyword_with_spaces(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(len(search_by_title(items, "  lion ")), 1)

    def test_no_match(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(search_by_title(items, "xyz"), [])


if __name__ == "__main__":
    unittest.main()