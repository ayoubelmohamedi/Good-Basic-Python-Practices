
'''
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:
-> 7
-> 15
-> 3

the output is:
-> 3

'''



if __name__ == '__main__':
    numbers = []
    i = 0
    while i < 3:
        userNumbers = int(input())
        numbers.append(userNumbers)
        i += 1
    print(min(numbers))