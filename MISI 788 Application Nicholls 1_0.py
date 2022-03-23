import os
from csv import reader
import time
import Algorithms

"""
Noah Earl Nicholls
MISI 788 Specialty Project
APPLYING HUMAN INTELLIGENCE TO OFFENSIVE CYBER OPERATIONS AND DIGITAL FORENSICS: A PYTHON FRAMEWORK
Version 1.1
March 22, 2022
"""

inputFile = r'D:\MISI788\PROGRAM\HUMINT_TEMPLATE.csv'
wordlist = r'D:\MISI788\PROGRAM\PasswordList.txt'

def lowercase(lower_list):
    for item in lower_list:
        string = item.lower()
        print("writing: ", string)
        f.write(string)
        f.write('\n')

#Open CSV file, parse 2nd row into list
x=0
with open (inputFile) as csv_file:
    csv_reader = reader(csv_file, delimiter = '\t')
    for row in csv_reader:
        if (x == 1):
            password_factors = list(row)
        x+=1

#Print list for user
print ("The HUMINT factors that will be used to generate passwords are as follows: \n", password_factors)

#Generate lists
special_numbers = []
special_words = []
special_characters = ['!', '@', '#', '$', '%']

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
            
with open(wordlist, 'w') as f:
    lowercase(special_words)
