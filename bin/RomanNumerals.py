import configparser


class RomanNumerals:
    
    def __init__(self):
        numeralConfig = configparser.ConfigParser()
        numeralConfig.read("../conf/NumeralMapping.conf")
        print(numeralConfig['NUMERAL_MAPPING']["1"])
        
    
    def error_handle_input_postive_whole_numbers_only(self, inputNumber):
        #Handle if input is string, we will allow if its a postive whole number
        #any other strings not allowed      
        if(isinstance(inputNumber, str)):
            try:
                floatInputNumber = float(inputNumber)
                strInputNumber = str(floatInputNumber)
                print("converted input:" + strInputNumber)
            except ValueError:
                raise RuntimeError("Non-number passed in, please re-try with whole number")
         
        floatInputNumber = float(inputNumber)
        #after string handling check if its a whole number         
        if(floatInputNumber % 1 != 0):
            raise RuntimeError("Decimal passed in, please re-try with whole number")
        #after whole number handling, check if its greater than zero
        if(floatInputNumber < 1):
            raise RuntimeError("Input number has to be greater than or equal to one")
        
        strInputNumber = str(int(floatInputNumber))          
        return strInputNumber
           
    def convert_number_to_numeral(self, inputNumber):
        
        #call method to validate input
#         print("raw input: ")
#         print(inputNumber)
        strInputNumber = self.error_handle_input_postive_whole_numbers_only(inputNumber)   
#         print("ready input: ")
#         print(strInputNumber) 
        inputNumberLength = len(strInputNumber)
#         
#         print("input length: " + str(inputNumberLength))        
        
        if(inputNumberLength == 1):
            print("single digit")
        
        return "I"