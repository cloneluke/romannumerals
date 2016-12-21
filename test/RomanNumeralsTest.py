import unittest
import romannumerals


class TestRomanNumerals(unittest.TestCase):
    
    def ReturnNumberFromString(self):
        self.assertEqual(romannumerals.convert_numeral_to_number("test"), 1, "Number not returned")


if __name__ == "__main__":
    unittest.main()
    