
import argparse
import os
import sys

#append to sys path to find libray
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from RomanNumerals import RomanNumerals


parser = argparse.ArgumentParser()
parser.add_argument('--inputNumber')

romanInstance = RomanNumerals()

args = parser.parse_args()
print(args.inputNumber)
romanInstance.convert_number_to_numeral(args.inputNumber)
