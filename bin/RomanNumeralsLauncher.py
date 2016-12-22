from bin.RomanNumerals import RomanNumerals
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputNumber')

romanInstance = RomanNumerals()

args = parser.parse_args()
print(args.inputNumber)
romanInstance.convert_number_to_numeral(args.inputNumber)