# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe \
#  and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

text = input("What is the Answer to the Great Question of Life, the Universe, and Everything?:")

if text in ("forty-two" , "42" , "Forty Two") :
    print ("yes")
else:
    print ("No")
