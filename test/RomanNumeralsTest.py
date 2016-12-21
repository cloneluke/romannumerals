import unittest
import bin.RomanNumerals
from bin.RomanNumerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    
    def setUp(self):
        print("setup")
        pass
    
    def testReturnNumberFromString(self):
        print("test 1")
        romanInstance = RomanNumerals()
        self.assertEqual(romanInstance.convert_numeral_to_number("test"), 1, "Number not returned")


if __name__ == "__main__":
    print("main")
    unittest.main()
    