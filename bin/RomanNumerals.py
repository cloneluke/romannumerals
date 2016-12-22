import configparser


class RomanNumerals:
    
    finalNumeralString =""
    numeralConfig = None
    
    def __init__(self):
        self.numeralConfig = configparser.ConfigParser()
        self.numeralConfig.read("../conf/NumeralMapping.conf")
        print(self.numeralConfig['NUMERAL_MAPPING_ONES']["1"])
        
    
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
        self.finalNumeralString = ""
        strInputNumber = self.error_handle_input_postive_whole_numbers_only(inputNumber)   
        inputNumberLength = len(strInputNumber)
        inputNumber = int(strInputNumber)
        if(inputNumberLength == 1):
            self.build_place(int(strInputNumber[0]), "NUMERAL_MAPPING_ONES")
        elif(inputNumberLength == 2):
            self.build_place(int(strInputNumber[0]), "NUMERAL_MAPPING_TENS")
            self.build_place(int(strInputNumber[1]), "NUMERAL_MAPPING_ONES")
        elif(inputNumberLength == 3):
            self.build_place(int(strInputNumber[0]), "NUMERAL_MAPPING_HUNDREDS")
            self.build_place(int(strInputNumber[1]), "NUMERAL_MAPPING_TENS")
            self.build_place(int(strInputNumber[2]), "NUMERAL_MAPPING_ONES")
        elif(inputNumberLength == 4):
            self.build_place(int(strInputNumber[0]), "NUMERAL_MAPPING_THOUSANDS")
            self.build_place(int(strInputNumber[1]), "NUMERAL_MAPPING_HUNDREDS")
            self.build_place(int(strInputNumber[2]), "NUMERAL_MAPPING_TENS")
            self.build_place(int(strInputNumber[3]), "NUMERAL_MAPPING_ONES")           
            
        return self.finalNumeralString
        
    def build_place(self, inputOnesSpotNumber, place_config_string):
        #build prefix I for 4 and 9
        if(inputOnesSpotNumber == 4 or inputOnesSpotNumber == 9):
            self.finalNumeralString = self.finalNumeralString + self.numeralConfig[place_config_string]["1"]
        #build out V for 4 thru 8
        if(inputOnesSpotNumber > 3 and inputOnesSpotNumber < 9):
            self.finalNumeralString = self.finalNumeralString + self.numeralConfig[place_config_string]["5"]
        #build out I's for 1-3, 6-8, excluding 4 and 9
        if(inputOnesSpotNumber < 4 or inputOnesSpotNumber > 5 and inputOnesSpotNumber % 5 != 4):
            for i in range(inputOnesSpotNumber % 5):
                self.finalNumeralString = self.finalNumeralString + self.numeralConfig[place_config_string]["1"]
        #if it's 9 put the X on the end
        if(inputOnesSpotNumber == 9):
            self.finalNumeralString = self.finalNumeralString + self.numeralConfig[place_config_string]["10"]
        return
    
    
    #TODO - add calling from command line