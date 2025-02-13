# In a file called twttr.py, implement a program that prompts the user for a str of text and then
# outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether 
#inputted in uppercase or lowercase.
def main():
    tweet = input("Input: ")
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]  
    new_tweet = ""  

    for char in tweet:  # Loop through each character in the input string
        if char not in vowel: 
            new_tweet += char 

    print("Output:", new_tweet)  

main()