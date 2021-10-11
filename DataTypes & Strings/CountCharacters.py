
'''
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of
times the character appears in the phrase.

Ex: If the input is:
-> n Monday
the output is:
-> 1

Ex: If the input is:
-> z Today is Monday
the output is:
-> 0

Ex: If the input is:
-> n It's a sunny day
the output is:
-> 2

Case matters.

Ex: If the input is:
-> n Nobody
the output is:
->0

n is different than N.
'''



if __name__ == '__main__':
    ''' Type your code here. '''
    phrase = str(input())
    count = 0

    myChar = phrase[0]
    theRealPhrase = phrase[1:]

    num_occurrences = theRealPhrase.count(myChar)

    print(num_occurrences)