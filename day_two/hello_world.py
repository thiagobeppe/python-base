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
__version__ = "0.1.2"
__author__ = "Thiago Beppe"
__license__ = "Unlicense"

import os
LANGUAGES_DICT = {
    "pt_BR":"Olá, mundo!",
    "it_IT":"Ciao, Mondo!",
    "us_EN":"Hello, World!",
    "fr_FR":"Bonjour, Monde!",
    "es_SP": "Hola, mundo!"
}

if __name__ == "__main__":
    current_language = (os.getenv("LANG","us_EN").split("."))[0]
    print(LANGUAGES_DICT[current_language])