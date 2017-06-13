import unittest
from prime import list_primes


class primeNumberGenerator(unittest.TestCase):
    def test_if_n_is_an_integer(self):
        self.assertEqual(True, type(100) is int, 'number is an integer')

    def test_values_if_they_are_string(self):
        self.assertEqual(True, type('samuel') is str, TypeError)

    def test_value_if_less_zero(self):
        self.assertEqual(list_primes(-1), 'Positive numbers only')

    def test_smallest_prime(self):
        actual=list_primes(10)
        expected=[2, 3, 5, 7]
        self.assertEqual(actual, expected, 'only 2 is the prime')

    def test_prime_numbers_of_ten(self):
        self.assertTrue(list_primes(10),(2,3,5,7))


if __name__ == '__main__':
    unittest.main()
