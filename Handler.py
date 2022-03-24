import Algorithms

def generate(special_words, special_numbers, special_characters):
    #Lowercase algorithms
    Algorithms.lowercase(special_words);
    Algorithms.lowercase_SC(special_words, special_characters)
    Algorithms.lowercase_numbers(special_words)
    Algorithms.lowercase_SN(special_words, special_numbers)
    Algorithms.lowercase_SN_SC(special_words, special_numbers, special_characters)
        
    #Uppercase algorithms
    Algorithms.uppercase(special_words)
    Algorithms.uppercase_SC(special_words, special_characters)
    Algorithms.uppercase_numbers(special_words)
    Algorithms.uppercase_SN(special_words, special_numbers)
    Algorithms.uppercase_SN_SC(special_words, special_numbers, special_characters)