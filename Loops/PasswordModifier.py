'''
Many user-created passwords are simple and easy to guess.
 Write a program that takes a simple password and makes it stronger by replacing characters using the key below,
 and by appending "q*s" to the end of the input string.

    i becomes !
    a becomes @
    m becomes M
    B becomes 8
    o becomes .

Ex: If the input is:
-> mypassword
the output is:
-> Myp@ssw.rdq*s

Hint: Python strings are immutable, but support string concatenation.
Store and build the stronger password in the given password variable.

'''

if __name__ == '__main__':
    word = input()
    password = ''

    ''' 
        i becomes !
        a becomes @
        m becomes M
        B becomes 8
        o becomes .
    '''

    passwordDir = {
        "i": "!",
        "a": "@",
        "m": "M",
        "B": "8",
        "o": "."
    }

    for item in word:
        if item in passwordDir:
            word = word.replace(item, passwordDir[item])
        else:
            continue

    word = word + "q*s"
    print(word)