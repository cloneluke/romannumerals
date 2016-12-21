import unittest
import bin.RomanNumerals
from bin.RomanNumerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    
    def setUp(self):
        print("setup")
        self.romanInstance = RomanNumerals()
        pass
    
    def testReturnNumeralIFromNumberOne(self):
        print("test 1")
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")
        
    def testReturnNumeralFromSingleDigitsNumber(self):
        print("test 1")
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")        


if __name__ == "__main__":
    print("main")
    unittest.main()
    