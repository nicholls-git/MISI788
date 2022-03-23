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
#def lowercase_SC(lower_list, special_characters):
    
#Function: lowercase words with numbers 0-9999
#def lowercase_numbers(lower_list):
    
#Function: lowercase words with special numbers list
#def lowercase_SN(lower_words, special_numbers):
    
#Function: lowercase words with special numbers and special characters
#def lowercase_SN_SC(lower_SN_SC_list, special_numbers, special_characters):
    
#Function: Uppercase words
def uppercase(upper_list):
    with open(config.wordlist, 'a') as f:
        for item in upper_list:
            string = item.capitalize()
            print("writing: ", string)
            f.write(string)
            f.write('\n')
        f.close()
#Function: Uppercase words with special characters (SC) 
#def uppercase_SC(upper_list, special_characters):
    
#Function: Uppercase words with numbers 0-9999
#def uppercase_numbers(upper_list):
    
#Function: Uppercase words with special numbers and special characters
#def uppercase_SN(upper_list, special_numbers):
    
#Function: Uppercase words with special numbers and special characters
#def uppercase_SN_SC(upper_list, special_numbers, special_characters):
