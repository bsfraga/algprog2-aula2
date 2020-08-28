import unittest

from list_core import List


class TestList(unittest.TestCase):

    def test_remove_method_from_product_list(self):
        product_list = List()

        product_list.insert('Gift Card')
        product_list.insert('Fita Crepe')
        product_list.insert('Palheta')

        product_list.delete('Palheta')

        with self.assertRaises(ValueError):
            product_list.search('Palheta')

    def test_remove_method_from_price_list(self):
        price_list = List()

        price_list.insert(30.0)
        price_list.insert(0.05)
        price_list.insert(2.0)

        price_list.delete(0.05)

        with self.assertRaises(ValueError):
            price_list.search(0.05)

    def test_remove_method_from_quantity_list(self):
        quantity_list = List()

        quantity_list.insert(5)
        quantity_list.insert(50)
        quantity_list.insert(30)

        quantity_list.delete(30)

        with self.assertRaises(ValueError):
            quantity_list.search(30)

    def test_search_method_on_product_list(self):
        product_list = List()

        product_list.insert('Gift Card')
        product_list.insert('Fita Crepe')
        product_list.insert('Palheta')

        self.assertEqual('Gift Card', product_list.search('Gift Card'))

    def test_search_method_on_price_list(self):
        price_list = List()

        price_list.insert(7.0)
        price_list.insert(10.0)
        price_list.insert(25.0)

        self.assertEqual(25.0, price_list.search(25.0))

    def test_search_method_on_quantity_list(self):
        quantity_list = List()

        quantity_list.insert(30)
        quantity_list.insert(15)
        quantity_list.insert(200)

        self.assertEqual(200, quantity_list.search(200))


if __name__ == '__main__':
    unittest.main()
