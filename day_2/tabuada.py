#!/usr/bin/env python
"""Imprime a tabuada de 1 a 10

----Tabuada do 1----
1x1 = 1
....
"""
__author__ = "Thiago Beppe"
__version__ = "0.0.1"

NUMBERS = [1,2,3,4,5,6,7,8,9,10]

for first_alg in NUMBERS:
    print("{:-^30}".format(f"Taboada do {first_alg}"))
    for second_alg in NUMBERS:
        print("{:^30}".format(f"{first_alg} x {second_alg} = {first_alg*second_alg}"))
    print("#"*30)
