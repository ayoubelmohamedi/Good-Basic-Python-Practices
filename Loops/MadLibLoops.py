'''
Mad Libs are activities that have a person provide various words,
which are then used to complete a short story in unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input,
and outputs a sentence using the input values as shown in the example below.
The program repeats until the input string is quit and disregards the integer input that follows.

Ex: If the input is:
-> apples 5
-> shoes 2
-> quit 0

the output is:

-> Eating 5 apples a day keeps the doctor away.
-> Eating 2 shoes a day keeps the doctor away.

'''

if __name__ == '__main__':
    while True:
        value = str(input())
        words = value.split(" ")

        if words[0] != "quit":
            displayText = "Eating {} {} a day keeps the doctor away.".format(words[1], words[0])
            print(displayText)
        else:
            break
