"""Hello world with multiple languages.
It get the LANG variable from your system to define which language we will use
to print.

Usage:
You need to have the LANG variable configure at your environment
    
    export LANG=pt_BR

Running:

    python3 first_script.py
    or
    ./first_script.py
"""
__version__ = "0.0.1"
__author__ = "Thiago Beppe"
__license__ = "Unlicense"

import os

if __name__ == "__main__":
    msg = "Hello, World!"
    current_language = (os.getenv("LANG","us_EN").split("."))[0]
    if current_language == "pt_BR":
        print("Olá, mundo!")
    elif current_language == "it_IT":
        print("Ciao, Mondo")
    elif current_language == "us_EN":
        print("Hello, Word!")