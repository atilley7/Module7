import unittest
import array as arr
from fun_with_collections.sort_and_search_array import search_array
from fun_with_collections.sort_and_search_array import sort_array
from fun_with_collections.basic_list_exception import make_list


class MyTestCase(unittest.TestCase):
    def test_item_found(self):
        self.assertEqual(search_array(x, 1), 0)

    def test_item_not_found(self):
        self.assertEqual(search_array(x, 66), -1)

    def test_sort_list(self):
        self.assertEqual(sort_array(x), [1, 4, 6])


x = make_list()
if __name__ == '__main__':
    unittest.main()
