
import argparse
import os
import sys

#append to sys path to find libray
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

#import class
from RomanNumerals import RomanNumerals

#handle commandline argument
parser = argparse.ArgumentParser()
parser.add_argument('--inputNumber')
#instantiate class
romanInstance = RomanNumerals()

args = parser.parse_args()
print(args.inputNumber)
#primary method call
romanInstance.convert_number_to_numeral(args.inputNumber)
