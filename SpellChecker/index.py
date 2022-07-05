from spellchecker import SpellChecker

spell = SpellChecker()

word = input("Enter your Word : ")

if word in spell:
    print("Correct Spelling")
else:
    print("Incorrect Spelling")
