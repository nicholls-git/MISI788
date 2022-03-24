import os
import config

#Function: lowercase words
def lowercase(lower_list):
    with open(config.wordlist, 'a') as f:
        for item in lower_list:
            string = item.lower()
            print("writing: ", string)
            f.write(string)
            f.write('\n')
        f.close()
        
#Function: lowercase words with special characters (SC) 
def lowercase_SC(lower_list, special_characters):
    with open(config.wordlist, 'a') as f:
        for word in lower_list:
            for sc in special_characters:
                string = word.lower()
                combined = string + sc
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close()
            
#Function: lowercase words with numbers 0-9999
def lowercase_numbers(lower_list):
    with open(config.wordlist, 'a') as f:
        for word in lower_list:
            for x in range(10000):
                string = word.lower()
                xstr = str(x)
                combined = (string + xstr)
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close()             
    
#Function: lowercase words with special numbers list
def lowercase_SN(lower_list, special_numbers):
    with open(config.wordlist, 'a') as f:
        for word in lower_list:
            for number in special_numbers:
                string = word.lower()
                nmb = str(number)
                combined = (string + nmb)
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close() 
        
#Function: lowercase words with special numbers and special characters
def lowercase_SN_SC(lower_list, special_numbers, special_characters):
    with open(config.wordlist, 'a') as f:
        for word in lower_list:
            for x in range (10000):
                for sc in special_characters:
                    string = word.lower()
                    xstr = str(x)
                    combined = (string + xstr + sc)
                    print ("writing: ", combined)
                    f.write(combined)
                    f.write('\n')
                    config.counter += 1
        f.close() 
        
#Function: Uppercase words
def uppercase(upper_list):
    with open(config.wordlist, 'a') as f:
        for item in upper_list:
            string = item.capitalize()
            print("writing: ", string)
            f.write(string)
            f.write('\n')
            config.counter += 1
        f.close()
        
#Function: Uppercase words with special characters (SC) 
def uppercase_SC(upper_list, special_characters):
    with open(config.wordlist, 'a') as f:
        for word in upper_list:
            for sc in special_characters:
                string = word.capitalize()
                combined = string + sc
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close()
#Function: Uppercase words with numbers 0-9999
def uppercase_numbers(upper_list):
    with open(config.wordlist, 'a') as f:
        for word in upper_list:
            for x in range(10000):
                string = word.capitalize()
                xstr = str(x)
                combined = (string + xstr)
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close()    
        
#Function: Uppercase words with special numbers and special characters
def uppercase_SN(upper_list, special_numbers):
    with open(config.wordlist, 'a') as f:
        for word in upper_list:
            for number in special_numbers:
                string = word.capitalize()
                nmb = str(number)
                combined = (string + nmb)
                print ("writing: ", combined)
                f.write(combined)
                f.write('\n')
                config.counter += 1
        f.close() 
        
#Function: Uppercase words with special numbers and special characters
def uppercase_SN_SC(upper_list, special_numbers, special_characters):
    with open(config.wordlist, 'a') as f:
        for word in upper_list:
            for x in range (10000):
                for sc in special_characters:
                
                    string = word.capitalize()
                    xstr = str(x)
                    combined = (string + xstr + sc)
                    print ("writing: ", combined)
                    f.write(combined)
                    f.write('\n')
                    config.counter += 1
        f.close() 