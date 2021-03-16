user_input = input('Enter input string:\n').replace(' ', '');

    
while(user_input != 'q'):
    if ',' not in user_input:
        print('Error: No comma in string.');
        print();
    else:
        tokens = user_input.split(',');
        print('First word: ' + tokens[0]);
        print('Second word: ' + tokens[1]);
        print();
        
    user_input = input('Enter input string:\n').replace(' ', '');