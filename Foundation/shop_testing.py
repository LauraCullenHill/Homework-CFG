from unittest import TestCase, mock

# import the functions
from shop import my_basket, my_items, basket_total, if_exit, in_budget, checkout


class TestItems(TestCase):
    def test_items(self):
        self.assertEqual({"apple": 0.50, "persian cat": 800, "orange": 0.50})


class TestBasket(TestCase):
    # test the basket_total function
    def test_basket_total(self):
        expected_total = 801.0
        self.assertTrue(basket_total(my_basket) == expected_total)

    def test_my_budget(self):
        self.assertTrue(in_budget(my_basket) > basket_total())

    def test_positive_budget(self):
        self.assertFalse(in_budget(my_basket) > 0)


class TestIfExit(TestCase):
    @mock.patch('builtins.input', side_effect=['y'])
    def test_if_continue(self, param):
        result = if_exit()
        self.assertTrue(result)





