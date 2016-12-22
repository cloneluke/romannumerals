import configparser


class RomanNumerals:
    
    finalNumeralString =""
    
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
        
        if(floatInputNumber > 3999):
            raise RuntimeError("Input number has to be less than 4000")
        
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
        inputNumber = int(strInputNumber)
#         print(strInputNumber[0])
#         print(strInputNumber[1])
#         print(strInputNumber[2])
#         print(strInputNumber[3])
#         
#         print("input length: " + str(inputNumberLength))        
        
        if(inputNumberLength == 1):
            tens_spot = self.build_tens_place(int(strInputNumber[0]))
        if(inputNumberLength == 1):
        return self.finalNumeralString
        
    def build_tens_place(self, inputTensSpotNumber):
        print(inputTensSpotNumber)
        if(inputTensSpotNumber == 4 or inputTensSpotNumber == 9):
            self.finalNumeralString = self.finalNumeralString + "I"
        if(inputTensSpotNumber > 3 and inputTensSpotNumber < 9):
            self.finalNumeralString = self.finalNumeralString + "V"
        if(inputTensSpotNumber < 4 or inputTensSpotNumber > 5 and inputTensSpotNumber % 5 != 4):
            for i in range(inputTensSpotNumber % 5):
                self.finalNumeralString = self.finalNumeralString + "I"
        if(inputTensSpotNumber == 9):
            self.finalNumeralString = self.finalNumeralString + "X"

#             if 
#             for i in range(int(strInputNumber[0])-5) 

        