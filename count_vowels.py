"""
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5
count_vowels("Palm") ➞ 1
count_vowels("Prediction") ➞ 4
"""

def count_vowels(txt):
    textlist = list(txt)
    vowelcount = 0
    vowels = ["a","e","i","o","u"]
    for a in textlist:
        if a in vowels:
            vowelcount += 1
    return vowelcount

print(count_vowels("Celelbration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))
print(count_vowels("Suite"))
print(count_vowels("Quote"))
print(count_vowels("Portrait"))

