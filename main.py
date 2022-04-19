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
Version 2.0
April 18, 2022
"""

#Generate lists
special_numbers = []
special_words = []
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']
password_factors = []

def main():

    #Call function to gather user input on selection 1, 2, or 3
    config.user_selection = Userinput.gather_info()
    
    #Open CSV file, parse 2nd column into list
    x=0
    
    #Open .csv file user selected
    with open (config.inputFile, newline='') as csv_file:
        data = csv.DictReader(csv_file)
        
        #For each row in .csv file
        for row in data:
            if (x >= 0):
                base_string=str(row['Input'])
                
                #Add each word in column to base_string
                password_factors.append(base_string)
                
                #Replace 'o' or 'O' with '0' and 'a' or 'A' with '@' (i.e. Password -> Passw0rd). Only if option '3' is selected
                if config.user_selection == 3:
                    print ("Test succesful")
                    if 'o' in base_string:
                        lowero = base_string.replace('o','0')
                        password_factors.append(lowero)
                    if 'O' in base_string:
                        uppero = base_string.replace('O','0')
                        password_factors.append(uppero)
                    if 'a' in base_string:
                        lowera = base_string.replace('a', '@')
                        password_factors.append(lowera)
                    if 'A' in base_string:
                        uppera = base_string.replace('a', '@')
                        password_factor.append(uppera)              
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
    print("Wordlist generated. Filepath: " + str(config.wordlist))
    print(str(config.counter) + " passwords were generated.")
    print(f"Passwords were generated in {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()