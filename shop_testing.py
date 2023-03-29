from unittest import TestCase, main, mock

# import the functions
from .shop import basket_total, my_budget, in_budget, integer_validation


# define test data
my_basket = {"apple": 0.50, "persian cat": 800, "orange": 0.50}


class TestBasket(TestCase):
    # test the basket_total function
    def test_basket_total(self):
        expected_total = 801.0
        assert basket_total(my_basket) == expected_total


class TestMyBudget(TestCase):
    # test the basket_total function
    def test_my_budget(self):
        self.assertTrue(my_budget() == 1000)

    def test_positive_budget(self):
        self.assertFalse(my_budget() < 0)


class TestInBudget(TestCase):
    # test the in_budget function with enough money
    def test_in_budget_enough_money(self):
        self.assertIsNone(in_budget(my_basket))


class TestIntegerValidation(TestCase):
    # Test integer_validation function with a string
    def test_integer_validation(self):
        with self.assertRaises(ValueError) as context:
            integer_validation("string")
        self.assertEqual(str(context.exception), "You must enter an integer")

