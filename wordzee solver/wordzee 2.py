def findWords():
    inputLetters = list(input('Input your letters with no spaces, all lowercaps: '))
    wordList = getWordlist()
    #wordList = ['cat', 'dog', 'tiger', 'cast', 'catt']
    possibleWords = []

    for word in wordList:
        letterBank = []
        found = False
        for n in range(len(inputLetters)):
            letterBank.append(inputLetters[n - 1])
            
        
        for letter in word:
            if letter in letterBank:
                found = True
                letterBank.remove(letter)
                continue
            else:
                found = False
                break
        else:
            if found:
                possibleWords.append(word)

    return possibleWords

        
        

def getWordlist():
    with open('wordList.txt') as f:
        wordList = f.readlines()
    
    wordList = [word.replace('\n', '') for word in wordList]
    wordList = [word.lower() for word in wordList]

    return wordList

def valueWords(listToValue):
    letterValues = {
        'a': 1,
        'b': 4,
        'c': 4,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 3,
        'h': 4,
        'i': 1,
        'j': 10,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 4,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 2,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10
    }
    wordValues = {}
    for word in listToValue:
        wordValues.update({word: 0})

        for letter in word:
            wordValues.update({word: wordValues[word] + letterValues[letter]})
    
    #returns the dictionaries sorted by values
    return sorted(wordValues.items(), key = lambda item:item[1])


if __name__ == '__main__':
    while True:
        words = findWords()
        valuedWords = valueWords(words)
        print(valuedWords)

        if input('Would you like to continue? Enter y/n: ') == 'y':
            continue
        else:
            break