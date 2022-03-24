import Algorithms

def generate(special_words, special_numbers, special_characters):
    #Lower
    Algorithms.lowercase(special_words);
    Algorithms.uppercase(special_words);
    Algorithms.lowercase_SC(special_words, special_characters)
    Algorithms.lowercase_numbers(special_words)
    Algorithms.lowercase_SN(special_words, special_numbers)
    Algorithms.lowercase_SN_SC(special_words, special_numbers, special_characters)
        
        