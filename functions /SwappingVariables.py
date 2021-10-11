
'''
Write a program whose input is two integers and whose output is the two integers swapped.

Ex: If the input is:
-> 3
-> 8

the output is:
-> 8 3

Your program must define and call the following function. swap_values() returns the two values in swapped order.
def swap_values(user_val1, user_val2)

'''


def swap_values(user_val1, user_val2):
    return user_val2, user_val1


if __name__ == '__main__':
    first = int(input())
    second = int(input())

    first_value, seconf_value = swap_values(first, second)
    print("{} {}".format(first_value, seconf_value))