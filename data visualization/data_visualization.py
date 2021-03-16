title = input('Enter a title for the data:\n');
print('You entered: ' + title);
print();

header_1 = input('Enter the column 1 header:\n')
print('You entered: ' + header_1);
print();

header_2 = input('Enter the column 2 header:\n')
print('You entered: ' + header_2);
print();

data = input('Enter a data point (-1 to stop input):\n');

hasDigit = False;
for char in data:
    if char.isdigit():
        hasDigit = True;

while(data != '-1'):
    if ',' not in data:
        print('Error: No comma in string.');
        print();
    elif (data.count(',') > 1):
        print('Error: Too many commas in input.');
        print();
    elif not hasDigit:
        print('Error: Comma not followed by an integer.');
        print();
    else:
        tokens = data.split(',');
        string = tokens[0].strip();
        number = tokens[1].strip();
        
        
        
        print('Data string: ' + string);
        print('Data integer: ' + number);
        
    data = input('Enter a data point (-1 to stop input):\n');
    
#define a function to print data
        
        