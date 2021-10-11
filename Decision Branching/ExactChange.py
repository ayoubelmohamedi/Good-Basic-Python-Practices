

'''
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line.
 The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate,
 like 1 Penny vs. 2 Pennies.

Ex: If the input is:
-> 0
(or less than 0), the output is:
-> No change

Ex: If the input is:
-> 45
the output is:
-> 1 Quarter
-> 2 Dimes

NOTE :
Dollars 100, Quarters 25, Dimes 10 , Nickels 5, and Penny(ies) 1.
'''


if __name__ == '__main__':
    total_change = int(input())

    dict_coins = {'dollar': 100
        , 'quarers': 25
        , 'dimes': 10
        , 'nickels': 5
        , 'penny': 1}

    if total_change > 0:
        dollars = total_change // dict_coins['dollar']
        total_change %= dict_coins['dollar']

        quarers = total_change // dict_coins['quarers']
        total_change %= dict_coins['quarers']

        dimes = total_change // dict_coins['dimes']
        total_change %= dict_coins['dimes']

        nickels = total_change // dict_coins['nickels']
        total_change %= dict_coins['nickels']

        penny = total_change

        values = [dollars, quarers, dimes, nickels, penny]

        # print("All values are ", values)
        for index, x in enumerate(values):

            if x > 0:

                if index == 0:
                    if values[index] > 1:
                        print("{} Dollars".format(values[0]))
                    elif values[0] == 1:
                        print("{} Dollar".format(values[0]))

                elif index == 1:
                    if values[index] > 1:
                        print("{} Quarters".format(values[1]))
                    elif values[1] == 1:
                        print("{} Quarter".format(values[1]))

                elif index == 2:
                    if values[index] > 1:
                        print("{} Dimes".format(values[2]))
                    elif values[2] == 1:
                        print("{} Dime".format(values[2]))

                elif index == 3:
                    if values[index] > 1:

                        print("{} Nickels".format(values[3]))
                    elif values[3] == 1:
                        print("{} Nickel".format(values[3]))

                elif index == 4:
                    if values[index] > 1:
                        print("{} Pennies".format(values[4]))
                    elif values[4] == 1:
                        print("{} Penny".format(values[4]))

        '''Dollars 100, Quarters 25, Dimes 10 , Nickels 5, and Penny(ies) 1.'''
    else:
        print("No change")
