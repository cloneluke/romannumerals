# RomanNumerals

This module takes in an arabic number and produces/returns a Roman Numerals

There are 4 files as part of this project: 

1. bin/RomanNumerals.py - core functionality and RomanNumerals Class
2. bin/RomanNumeralsLauncher.py - command line runnable launcher
3. test/RomanNumeralsTest.py - runnable test suite
4. conf/NumeralMapping.conf - config to drive RomanNumerals class

You are required to have base python 3.x installed
If the path to python.exe is not on your OS.PATH, you will have to give full path when launching


###bin/RomanNumeralsLauncher.py - Commandline launcher takes a single positive whole number as input:

```
example:
C:\Users\lbodeen\workspace\romannumerals>c:\Users\lbodeen\AppData\Local\Programs\Python\Python35-32\python bin\RomanNumeralsLauncher.py --inputNumber 3
3
converted input:3.0
III
```

###test/RomanNumeralsTest.py - Python executable that will run test suite, also runnable via commandline

```

C:\Users\lbodeen\workspace\romannumerals>c:\Users\lbodeen\AppData\Local\Programs\Python\Python35-32\python test\RomanNumeralsTest.py
DCCXX
.converted input:379.0
CCCLXXIX
.CCX
.VIII
.converted input:4.0
IV
.IX
.VI
.III
.II
.MMMCMXCIX
.Input number has to be less than 4000 due to Roman Numeral limitations
.Decimal passed in, please re-try with whole number
.converted input:20.03
Decimal passed in, please re-try with whole number
.Non-number passed in, please re-try with whole number
.Input number has to be greater than or equal to one
.converted input:-2.0
Input number has to be greater than or equal to one
.Non-number passed in, please re-try with whole number
.I
.I
.converted input:1.0
I
.converted input:1.0
I
.Non-number passed in, please re-try with whole number
.LXVIII
.converted input:25.0
XXV
.MMDCCCXLVIII
.
----------------------------------------------------------------------
Ran 25 tests in 0.055s

OK

```