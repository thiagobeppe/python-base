""" Bloco de Notas

$ notes.py add "Minha Nota"
tag: tech
text: Anotação geral sobre carreita de tecnologia

$ notes.py read --tag=tech
"""

__version__ = "0.1.0"
__author__ = "Thiago Beppe"  

import os
import sys

CURRENT_DIR = os.curdir
PATH = os.path.join(CURRENT_DIR, "notepad.txt")

CLI_COMMANDS ={
    "read": lambda x: read_file_by_tag(x),
    "add": lambda x,y,z: add_registry_on_file(x,y,z),
}

def add_registry_on_file(title, tag, text):
    with open(PATH,"a") as f:
        f.write(f"Tag: {tag} \n")
        f.write(f"Title: {title}\n")
        f.write(f"Text: {text} \n")
    return


def read_file_by_tag(tag):
    with open(PATH, "r") as f:
        lines = f.readlines()
        posts = []
        is_tagged_valid = False
        for line in lines:
            if "Tag:" in line and line.split(":")[1].strip() == tag:
                is_tagged_valid=True
            if "Title:" in line and is_tagged_valid:
                posts.append(_split_type(line))
            elif "Text:" in line and is_tagged_valid:
                posts.append(_split_type(line))
                is_tagged_valid = False
        f.close()
    for index in range(0,len(posts),2):
        print(f"Title: {posts[index]}Text: {posts[index+1]}")
        print("-"*30)
    return


def _split_type(line):
    return (line.split(":"))[1]

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments[0] == "add":
        tag = input("Add your tag: \n")
        text = input("Add your text: \n" )
        CLI_COMMANDS["add"](arguments[1], tag, text)
    elif arguments[0] == "read":
        CLI_COMMANDS["read"]((arguments[1].split("="))[1])
    else:
        print("Invalid command")
        sys.exit(1)