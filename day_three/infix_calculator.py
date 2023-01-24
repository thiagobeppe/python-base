#!/usr/bin/env python
"""Infix Calculator
Python implementation of a polish notation.

[operação] [n1] [n2]

Operações
sum -> +
sub -> -
mul -> *
div -> /

Usage:
infix_calculator.py sum 5 2
7
"""

__version__ = "0.1.0"
__author__ = "Thiago Beppe"

import sys

VALID_OPERATIONS = {
    "sum": lambda x,y: x+y,
    "sub": lambda x,y: x-y,
    "mul": lambda x,y: x*y,
    "div": lambda x,y: x/y,
}

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments)>=4 or len(arguments) == 0:
        operation = input("Selecione uma das operações válidas (sum,sub,mul,div): \n")
        n1 = input("adicione o primeiro valor: \n")
        n2 = input("adicione o segundo valor: \n")
        print(VALID_OPERATIONS[operation](int(n1),int(n2)))
    else:
        print(VALID_OPERATIONS[arguments[0]](int(arguments[1]),int(arguments[2])))


