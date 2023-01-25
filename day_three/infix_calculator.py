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

Os resultados serão salvos em infixcalc.log
"""

__version__ = "0.1.1"
__author__ = "Thiago Beppe"

import sys

VALID_OPERATIONS = {
    "sum": lambda x,y: x+y,
    "sub": lambda x,y: x-y,
    "mul": lambda x,y: x*y,
    "div": lambda x,y: x/y,
}

def validate_inputs(arguments):
    if len(arguments) != 3 or arguments[0] not in VALID_OPERATIONS.keys() or not arguments[1].isdigit() or not arguments[2].isdigit() :
        print("Invalid inputs")
        sys.exit(1)

def write_logs(operation, n1, n2, result):
    with open("infixcalc.log", "a") as file:
        file.write(f"{operation} {n1} {n2} = {result} \n")
    return 


if __name__ == "__main__":
    arguments = sys.argv[1:]
    validate_inputs(arguments)
    if len(arguments)>=4 or len(arguments) == 0:
        operation = input("Selecione uma das operações válidas (sum,sub,mul,div): \n")
        n1 = input("adicione o primeiro valor: \n")
        n2 = input("adicione o segundo valor: \n")
        result = (VALID_OPERATIONS[operation](int(n1),int(n2)))
        write_logs(operation, n1,n2,result)
    else:
        result =(VALID_OPERATIONS[arguments[0]](int(arguments[1]),int(arguments[2])))
        write_logs(arguments[0], arguments[1],arguments[2],result)
    