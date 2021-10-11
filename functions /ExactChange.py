'''
Again; but this time with a function applied

Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Ex: If the input is:
-> 0
or less, the output is:
-> no change

Ex: If the input is:
-> 45
the output is:
-> 1 quarter
-> 2 dimes

Your program must define and call the following function. The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
def exact_change(user_total)

'''


def exact_change(user_total):
    dict_coins = {'dollar': 100
        , 'quarters': 25
        , 'dimes': 10
        , 'nickels': 5
        , 'penny': 1}

    dollars = user_total // dict_coins['dollar']
    user_total %= dict_coins['dollar']

    quarter = user_total // dict_coins['quarters']
    user_total %= dict_coins['quarters']

    dimes = user_total // dict_coins['dimes']
    user_total %= dict_coins['dimes']

    nickels = user_total // dict_coins['nickels']
    user_total %= dict_coins['nickels']

    penny = user_total

    return dollars, quarter, dimes, nickels, penny


if __name__ == '__main__':
    input_val = int(input())
    if input_val > 1:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
        values = [num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]

        for index, x in enumerate(values):
            if x > 0:
                if index == 0:
                    if values[index] > 1:
                        print("{} dollars".format(values[0]))
                    elif values[0] == 1:
                        print("{} dollar".format(values[0]))

                elif index == 1:
                    if values[index] > 1:
                        print("{} quarters".format(values[1]))
                    elif values[1] == 1:
                        print("{} quarter".format(values[1]))

                elif index == 2:
                    if values[index] > 1:
                        print("{} dimes".format(values[2]))
                    elif values[2] == 1:
                        print("{} dime".format(values[2]))

                elif index == 3:
                    if values[index] > 1:
                        print("{} nickels".format(values[3]))
                    elif values[3] == 1:
                        print("{} nickel".format(values[3]))

                elif index == 4:
                    if values[index] > 1:
                        print("{} pennies".format(values[4]))
                    elif values[4] == 1:
                        print("{} penny".format(values[4]))

    else:
        print("no change")



