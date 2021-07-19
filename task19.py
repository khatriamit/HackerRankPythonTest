"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a 
function that determines whether a string that contains only letters is an isogram. Assume the 
empty string is an isogram. Ignore letter case.

Test cases:
isIsogram("Dermatoglyphics") == true
isIsogram("aba") == false
isIsogram("moOse") == false  
"""

# simplest method
def is_isogram(string):
    s = string.lower()
    return len(set(s)) == len(s)


# letter counts
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True


# lambda function
is_isogram_lam = lambda s: len(set(s.lower())) == len(s)

s = "Dermatoglyphics"
print(is_isogram_lam(s))
