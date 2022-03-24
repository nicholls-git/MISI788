import os
import time

from csv import reader
import Handler
import config

"""
Noah Earl Nicholls
MISI 788 Specialty Project
APPLYING HUMAN INTELLIGENCE TO OFFENSIVE CYBER OPERATIONS AND DIGITAL FORENSICS: A PYTHON FRAMEWORK
Version 1.3
March 22, 2022
"""

#Generate lists
special_numbers = []
special_words = []
special_characters = ['!', '@', '#', '$', '%']

#Open CSV file, parse 2nd row into list
x=0
with open (config.inputFile) as csv_file:
    csv_reader = reader(csv_file, delimiter = '\t')
    for row in csv_reader:
        if (x == 1):
            password_factors = list(row)
        x+=1

#Print list for user
print ("The HUMINT factors that will be used to generate passwords are as follows: \n", password_factors)

#Separate password_factors into two lists: special_numbers, special_words
for x in password_factors:
    try:
        word = int(x)
        special_numbers.append(word)
    except:
        try:
            number = str(x)
            special_words.append(number)
        except:
            print("Template error, ensure entries are only in second row.")

#Test Print
#print (special_numbers, special_words)          
Handler.generate(special_words, special_numbers, special_characters)

print('\n')
print("Wordlist generated.")
print(str(config.counter) + " passwords were generated.")
