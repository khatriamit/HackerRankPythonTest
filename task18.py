"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known 
for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, 
check out how contractions are expected to be in the example below.

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

"How can mirrors be real if our eyes aren't real" should equal
"How Can Mirrors Be Real If Our Eyes Aren't Real"
"""
import string

value = "How Can Mirrors Be Real If Our Eyes Aren't Real"

# method 1 using python's string package
def to_jaden_case(tweet):
    return string.capwords(tweet)


output = to_jaden_case("How can mirrors be real if our eyes aren't real")
print(output)

# method 2 using comprehension
def toJadenCase(tweet):
    return " ".join(w.capitalize() for w in tweet.split())


output = toJadenCase("How can mirrors be real if our eyes aren't real")
print(output)
