import unittest
from fun_with_collections.sort_and_search_list import search_list
from fun_with_collections.sort_and_search_list import sort_list
from fun_with_collections.basic_list_exception import make_list
class MyTestCase(unittest.TestCase):
    def test_item_found(self):
        self.assertEqual(search_list(x, 1), 1)
    def test_item_not_found(self):
        self.assertEqual(search_list(x, 66), -1)


x = make_list()
if __name__ == '__main__':
    unittest.main()
