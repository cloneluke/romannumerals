import configparser


class RomanNumerals:
    
    def __init__(self):
        numeralConfig = configparser.ConfigParser()
        numeralConfig.read("../conf/NumeralMapping.conf")
        print(numeralConfig['NUMERAL_MAPPING']["1"])
        
    
    def convert_number_to_numeral(self, inputNumber):

        #Handle if input is string, we will allow if its a postive whole number
        #any other strings not allowed      
        if(isinstance(inputNumber, str)):
            try:
                inputNumber = float(inputNumber)
                strInputNumber = str(inputNumber)
                print("converted input:" + strInputNumber)
            except ValueError:
                return "Non-number passed in, please re-try with whole number"
         
        #after string handling check if its a whole number         
        if(inputNumber % 1 != 0):
            return "Decimal passed in, please re-try with whole number"
        #after whole number handling, check if its greater than zero
        if(inputNumber < 1):
            return "Input number has to be greater than or equal to one"
              
        strInputNumber = str(inputNumber)   
        
        inputNumberLength = len(strInputNumber)
        
        print("input length: " + str(inputNumberLength))        
        
        if(inputNumberLength == 1):
            print("single digit")
        
        return "I"