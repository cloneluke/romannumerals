import configparser


class RomanNumerals:
    
    def __init__(self):
        numeralConfig = configparser.ConfigParser()
        numeralConfig.read("../conf/NumeralMapping.conf")
        print(numeralConfig['NUMERAL_MAPPING']["1"])
        
    
    def convert_number_to_numeral(self, inputNumber):
      
        try: 
            testval = int(inputNumber)
            strInputNumber = str(inputNumber)
        except ValueError:
            return "Non-number or non-whole number passed in, please re-try with whole number"
        
        inputNumberLength = len(strInputNumber)
        
        print(inputNumberLength)        
        
        if(inputNumberLength == 1):
            print("single digit")
        
        return "I"