import os
import config
import tkinter
from tkinter import filedialog
import os


#tkinter file documentation: https://docs.python.org/3/library/dialog.html
def search_for_file_path ():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window        
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Select where the input CSV file is located')
    if len(tempdir) > 0:
        print ("\n")
    return tempdir
        
def search_for_folder_path ():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window        
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Select folder where password list will generate')
    if len(tempdir) > 0:
        print ("\n")
    return tempdir   
    
def gather_info():
    #Intro
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
    print("Welcome to Noah Nicholls' MISI 788 Submission")
    print("Select Where the Input CSV File is Located")
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")

    config.inputFile = (str(search_for_file_path()))
    print("Select Folder Where Password List Will Generate")
    config.passwordFolderPath = (str(search_for_folder_path()))
    config.wordlist = str(config.passwordFolderPath) + '/passwordlist.txt'
    print("File path is of .csv file is: " + str(config.inputFile))
    print("Folder where password list will generate is: " + str(config.wordlist))
    print ("\n")
    print("Select 1-3 to generate a short, medium, or long password list")
    print("1. Short. Uppercase and lowercase with numbers. No special Characters")
    print("2. Medium. Uppercase and lowercase with numbers and special characters")
    print("3. Long. Uppercase and lowercase with numbers, special characters, and word manipulation ('i.e. Password -> Passw0rd")

    #Gather user input for how complicated user wants password generation
    userChoice = input("Enter option (1-3): ")
    while userChoice not in ['1', '2', '3']:
        userChoice = input("You must enter 1, 2, or 3: ")
    return int(userChoice)
    
    print("Enter how many numbers you would like added to end of password (i.e. Password1111)")
    numberChoice = input("Enter option (1-4): (1 = passwordX, 2 = passwordXX, etc. ")
    while numberChoice not in ['1', '2', '3', '4']:
        numberChoise = input("You must enter 1, 2, 3, or 4: ")
    return int(numberChoice)

def number_gather():

    print("Enter how many numbers you would like added to end of password (i.e. Password1111)")
    numberChoiceStr = input("Enter option (1-4)(1 = 0-9, 2 = 0-99, 3 = 0-999, 4 = 9999): ")
    while numberChoiceStr not in ['1', '2', '3', '4']:
        numberChoiceStr = input("You must enter 1, 2, 3, or 4: ")    

    numberChoice = int(numberChoiceStr)
    #Configur config.py number_length parameter. This changes how many numbers (0-9, 0-99, 0-999, or 0-9999) to append to the end of each password)
    if numberChoice == 1:
        config.number_length = 10
    elif numberChoice == 2: 
        config.number_length = 100
    elif numberChoice == 3: 
        config.number_length = 1000
    elif numberChoice == 4:
        config.number_length = 10000
    