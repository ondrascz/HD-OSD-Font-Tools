# file = open( "nonexistent.txt", "r" )

from os import path


filename = "dev resources/pokusny soubor s mcezerami v nazvu.txt"

print(path.isfile(filename))