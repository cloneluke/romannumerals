import unittest
import bin.RomanNumerals
from bin.RomanNumerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    
    def setUp(self):
        self.romanInstance = RomanNumerals()
        pass
    
    def testReturnNumeralIFromNumberOne(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")
        
    def testReturnMessageIfInputLetter(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral("a"), "Non-number or non-whole number passed in, please re-try with whole number", "Non-number allowed through") 
     
    def testReturnMessageIfInputSymbol(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral("~"), "Non-number or non-whole number passed in, please re-try with whole number", "Non-number allowed through")           
        
    def testReturnNumeralFromSingleDigitsNumber(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")        


if __name__ == "__main__":
    unittest.main()
    
    