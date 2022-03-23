from Algorithms import *

wordlist = r'D:\MISI788\PROGRAM\PasswordList.txt'
def generate(special_words, special_numbers, special_characters):
    with open(wordlist, 'w') as f:
        lowercase(special_words);
        uppercase(special_words);