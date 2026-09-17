print("Hello World")

with open("text.txt") as soubor:
    obsah = soubor.read()
    print(obsah)

import os
with open(os.sep.join(["text.txt"])) as soubor:
    obsah = soubor.read()
    print(obsah)

import os
with open(os.sep.join(["text.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)