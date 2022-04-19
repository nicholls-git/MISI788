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