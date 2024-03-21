import special_palindrome as palindrome
import unittest


class TestSpecialPalindrome(unittest.TestCase):

    def test_substrCount(self):
        result = palindrome.substrCount(5, "asasd")
        self.assertEqual(result, 7)

        result = palindrome.substrCount(7, "abcbaba")
        self.assertEqual(result, 10)

        result = palindrome.substrCount(4, "aaaa")
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
