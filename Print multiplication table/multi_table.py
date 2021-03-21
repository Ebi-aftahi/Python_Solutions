user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for item in mult_table:
    for index, digit in enumerate(item):
        if(index != len(item)-1):
            print(digit, end='')
            print(' | ', end='')
        else:
            print(digit)
