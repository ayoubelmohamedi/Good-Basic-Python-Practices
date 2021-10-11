'''


Many documents use a specific format for a person's name. Write a program whose input is:

firstName middleName lastName

and whose output is:

lastName, firstInitial.middleInitial.

Ex: If the input is:

-> Pat Silly Doe

the output is:

-> Doe, P.S.
---------------------
If the input has the form:

-> firstName lastName

the output is:

-> lastName, firstInitial.

Ex: If the input is:

Julia Clark

the output is:

Clark, J.

'''

if __name__ == '__main__':

    # enter full name
    full_name = str(input())

    # full_name = "{} {} {}".format(firstName,middleName,lastName)

    out = full_name.count(' ')  # counts number of spaces

    if out == 1:
        name_list = full_name.split(' ')
        first_name = name_list[0]
        lastName = name_list[1]
        first_initial = first_name[0]
        result = "{0}, {1}.".format(lastName, first_initial)
        print(result)

    elif out == 2:
        name_list = full_name.split(' ')
        first_name = name_list[0]
        first_initial = first_name[0]

        middle_name = name_list[1]
        middle_initial = middle_name[0]

        lastName = name_list[2]
        result = "{0}, {1}.{2}.".format(lastName, first_initial, middle_initial)
        print(result)
    else:
        print("Enter full name")
