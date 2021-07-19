"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case)

to_camel_case("the-stealth-warrior") // returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") // returns "TheStealthWarrior"
"""

#  simple method
def to_camel_case(text):
    new_text = text.replace("-", " ").replace("_", " ")
    new_text = new_text.split()
    if len(text) == 0:
        return text
    return new_text[0] + "".join(i.capitalize() for i in new_text[1:])


input_ = "The_Stealth_Warrior"
result = to_camel_case(input_)
print(result)

# more slick method
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace("_", "").replace("-", "")


result = to_camel_case(input_)
print(result)
