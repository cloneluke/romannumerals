import unittest
import sys
from bin.RomanNumerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    
    def setUp(self):
        self.romanInstance = RomanNumerals()
        pass
    
    def testReturnNumeralIFromNumberOne(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")
    
    def testReturnNumeralIFromNumberOneString(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral("1"), "I", "I (string) not returned") 
     
    def testReturnNumeralIFromNumberOneStringWithChar(self):
        try:
            self.romanInstance.convert_number_to_numeral("1.a")
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Non-number passed in, please re-try with whole number", "Non-number allowed through")
            print(e.args[0])
     
    def testReturnNumeralIFromNumberOneStringDecimalWhole(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral("1.0"), "I", "I (string) not returned")         
        
    def testReturnMessageIfInputLetter(self):
        try:
            self.romanInstance.convert_number_to_numeral("a")
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Non-number passed in, please re-try with whole number", "Non-number allowed through")
            print(e.args[0])
     
    def testReturnMessageIfInputSymbol(self):
        try:
            self.romanInstance.convert_number_to_numeral("~")
        except RuntimeError as e: 
            self.assertEqual(e.args[0], "Non-number passed in, please re-try with whole number", "Non-number allowed through") 
            print(e.args[0])
    
    def testReturnMessageIfInputDecimal(self):
        try:
            self.romanInstance.convert_number_to_numeral(20.03)  
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Decimal passed in, please re-try with whole number", "Decimal allowed through")
            print(e.args[0])
    
    def testReturnMessageIfInputDecimalString(self):
        try:
            self.romanInstance.convert_number_to_numeral("20.03")
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Decimal passed in, please re-try with whole number", "Decimal allowed through")
            print(e.args[0])    
    
    def testReturnMessageIfInputNegativeWhole(self):
        try:
            self.romanInstance.convert_number_to_numeral(-2)
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Input number has to be greater than or equal to one", "Zero or negative allowed through")  
            print(e.args[0])
     
    def testReturnMessageIfInputNegativeWholeString(self):
        try:
            self.romanInstance.convert_number_to_numeral("-2")
        except RuntimeError as e:   
            self.assertEqual(e.args[0], "Input number has to be greater than or equal to one", "Zero or negative allowed through")
            print(e.args[0])                   
        
    def testReturnNumeralFromSingleDigitsNumber(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")        


if __name__ == "__main__":
    unittest.main()
    
    