def checkConsonants(inputword):
    """Check starting consonants up to three, return int."""
    cc = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for letter in inputword:
        if letter not in vowels:
            cc += 1
        elif letter == vowels[5] and cc == 0:
            cc = 1
            break
        else:
            break

    return cc


def Piggify(inputString):
    """Translates simple sentences into pig-latin."""
    inputString.lower()
    words = inputString.split()
    i = 0
    returnString = ""
    for word in words:
        x = checkConsonants(word)
        if x > 0:
            temp_word = word[:x]
            word = word[x:]
            word += temp_word + 'ay'
        elif x == 0:
            word += 'yay'

        # Concatenation
        if returnString == "":
            returnString += word
        else:
            returnString += " " + word
    return returnString

y = ""
while y != 'q' or 'Q':
    y = input('Gimme some words, brah.')
    print(Piggify(y))