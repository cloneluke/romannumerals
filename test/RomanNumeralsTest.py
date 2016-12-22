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
     
    def testReturnMessageIfGreaterThanMaximumAllowableNumeral(self):
        try:
            self.romanInstance.convert_number_to_numeral(4000)
        except RuntimeError as e:
            self.assertEqual(e.args[0], "Input number has to be less than 4000", "Number greater than 3999 allowed through")  
            print(e.args[0])    
#     
#     def testReturnMessageIfEqualMaximumAllowableNumeral(self):
#         self.assertEqual(self.romanInstance.convert_number_to_numeral(3999), "I", "I (string) not returned")     
    
#     def testHundredsPosition(self):
#         self.assertEqual(self.romanInstance.convert_number_to_numeral(720), "I", "I (string) not returned") 
    
#     def testTensPosition(self):
#         self.assertEqual(self.romanInstance.convert_number_to_numeral(68), "VIII", "Not expected Numeral String") 

    def testOnesPositionThree(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(3), "III", "Not expected Numeral String")                  
 
    def testOnesPositionTwo(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(2), "II", "Not expected Numeral String")
    
    def testOnesPositionNine(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(9), "IX", "I (string) not returned") 
    
    def testOnesPositionEight(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(8), "VIII", "I (string) not returned")
    
    def testOnesPositionSix(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(6), "VI", "I (string) not returned")  
    
    def testOnesPositionFour(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral("4"), "IV", "Not expected Numeral String")                    
        
    def testReturnNumeralFromSingleDigitsNumber(self):
        self.assertEqual(self.romanInstance.convert_number_to_numeral(1), "I", "I (string) not returned")        


if __name__ == "__main__":
    unittest.main()
    
    