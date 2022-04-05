import os
import time

from csv import reader

import csv
import Handler
import config
import Userinput
"""
Noah Earl Nicholls
MISI 788 Specialty Project
APPLYING HUMAN INTELLIGENCE TO OFFENSIVE CYBER OPERATIONS AND DIGITAL FORENSICS: A PYTHON FRAMEWORK
Version 1.4
March 31, 2022
"""

#Generate lists
special_numbers = []
special_words = []
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']
password_factors = []

def main():
    Userinput.gather_info()
    #Open CSV file, parse 2nd column into list
    x=0
    with open (config.inputFile, newline='') as csv_file:
        #csv_reader = reader(csv_file, delimiter = ',')
        data = csv.DictReader(csv_file)
        for row in data:
            if (x >= 0):
                base_string=str(row['Input'])
                
                #Add each word in column to base_string
                password_factors.append(base_string)
                
                #Replace 'o' or 'O' with '0' (i.e. Password -> Passw0rd)
                # if 'o' in base_string:
                    # lower = base_string.replace('o','0')
                    # password_factors.append(lower)
                # if 'O' in base_string:
                    # upper = base_string.replace('O','0')
                    # password_factors.append(upper)
                
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
    tic = time.perf_counter()
    Handler.generate(special_words, special_numbers, special_characters)
    toc = time.perf_counter()

    print('\n')
    print("Wordlist generated.")
    print(str(config.counter) + " passwords were generated.")
    print(f"Passwords were generated in {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()