# file = open( "nonexistent.txt", "r" )

from os import path


filename = "dev resources/pokusny soubor s mezerami v nazvu.txt"

print(path.exists(filename))