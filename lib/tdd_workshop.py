def sum_numbers(num_1, num_2): 
    return num_1 + num_2

def count_letters(string, character):
    counter = 0

    string = string.lower()
    character = character.lower()

    for letter in string:     
        if letter == character:
            counter += 1
        
    return counter

# we will need a counter to keep track of the number of letters
# loop of some kind to go through the string - 

#Create a function that accepts a string and a single character, 
#and returns an integer of the count of occurrences the 2nd argument is found in the first one.

#If no occurrences can be found, a count of 0 should be returned.

#The first argument can be an empty string
