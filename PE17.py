# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 15:31:36 2017

@author: Julia
"""

units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
exception = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
dezenas = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

soma = 0

# from 1 to 19

for element in (units + exception):
    soma += len(element)

# from 20 to 99

for dezena in dezenas:
    for unit in units:
        soma = soma + len(dezena) + len(unit)

from1to99 = soma

# hundreds

for unit in units[1:]:
    soma = soma + 100*(len(unit) + len("hundred")) + 99*len("and") + from1to99

soma += len("onethousand")



print (soma)