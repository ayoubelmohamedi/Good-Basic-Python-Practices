# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    ''' Type your code here. '''
    '''Dollars 100, Quarters 25, Dimes 10 , Nickels 5, and Penny(ies) 1.'''

while True:

    total_change = int(input())
    if total_change == 0:
        print("program exited")
        break
    dict_coins = {'dollar': 100
        , 'quarters': 25
        , 'dimes': 10
        , 'nickels': 5
        , 'penny': 1}

    if total_change > 0:
        dollars = total_change // dict_coins['dollar']
        total_change %= dict_coins['dollar']

        quarter = total_change // dict_coins['quarters']
        total_change %= dict_coins['quarters']

        dimes = total_change // dict_coins['dimes']
        total_change %= dict_coins['dimes']

        nickels = total_change // dict_coins['nickels']
        total_change %= dict_coins['nickels']

        penny = total_change

        values = [dollars, quarter, dimes, nickels, penny]

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
        print("-" * 40)
        '''Dollars 100, Quarters 25, Dimes 10 , Nickels 5, and Penny(ies) 1.'''
    else:
        print("No change")
