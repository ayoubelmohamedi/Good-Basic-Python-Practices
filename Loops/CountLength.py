'''
Count input length without spaces, periods, or commas:

Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

Ex: If the input is:
-> Listen, Mr. Jones, calm down.
the output is:
-> 21

'''


if __name__ == '__main__':
    user_text = input()
    counter = 0
    avoidSymbols = [" ", ".", ","]
    ''' Type your code here. '''
    tockens = list(user_text)
    for i in range(len(tockens)):
        if tockens[i] in avoidSymbols:
            continue
        else:
            counter = counter + 1
            i = i + 1
    print(counter)