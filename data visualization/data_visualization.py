
title = input('Enter a title for the data:\n')
print('You entered: ' + title)
print()

header_1 = input('Enter the column 1 header:\n')
print('You entered: ' + header_1);
print();

header_2 = input('Enter the column 2 header:\n')
print('You entered: ' + header_2);
print();

data = input('Enter a data point (-1 to stop input):\n');

author_books = [];

def hasDigit (string):
    for char in string:
        if char.isdigit():
            return True;
        else:
            return False;

while(data != '-1'):
    if ',' not in data:
        print('Error: No comma in string.');
        print();
    elif (data.count(',') > 1):
        print('Error: Too many commas in input.');
        print();
    elif not hasDigit(data):
        print('Error: Comma not followed by an integer.');
        print();
    else:
        tokens = data.split(',');
        string = tokens[0].strip();
        number = tokens[1].strip();
        author_books.append([tokens[0],tokens[1]]);
                
        print('Data string: ' + string);
        print('Data integer: ' + number);
        
    data = input('Enter a data point (-1 to stop input):\n');
    
#print table
if(len(author_books)>0):
    print('{string:>33}'.format(string = title))


    format_string = '{name:<20}|{number:>23}';
    print(format_string.format(name = header_1, number = header_2))
    print('-'*44);
    for item in author_books:
        print(format_string.format(name = item[0], number = item[1]));

