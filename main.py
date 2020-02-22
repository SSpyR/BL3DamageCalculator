# main.py
# Creator: SSpyR

# make a proper GUI
# actually allow gear and augments

import sys
from sys import argv
from utils import calcMain as calc

def main():
    print(argv)
    mods=[]
    for i in range(2, 6):
        mods.append(eval(argv[i]))
    gear=[]
    for i in range(6, len(argv)):
        gear.append(eval(argv[i]))
    while len(gear)<7: gear.append(0)
    response=calc.unpack(argv[1], mods, gear)
    return response

if __name__ == '__main__':
    main()