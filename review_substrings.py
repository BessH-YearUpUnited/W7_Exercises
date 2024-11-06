#name = input('Enter a name: ')

# print(name.find(' '))

def parse_and_display(name):
    first_name = name[:(name.find(' '))+1]
    last_name = name[(name.find(' ') + 1):]
    last_name_test = name[(name.rfind(' ') + 1):]

    if first_name == '':
        print(f'Full name: {name}')
        print(f'Full name: {name}')
        print("Last name: None")
    elif last_name == last_name_test:
        print(f'Full name: {name}')
        print(f'First name: {first_name}')
        print(f'Last name: {last_name}')
    else:
        print(f'Full name: {name}')
        print(f'First name: {first_name}')
        print(f'Middle name: {name[name.find(' '):name.rfind(' ') + 1]}')
        print(f'Last name: {last_name_test}')

name = None

while name == None:
    name = input('Enter a name: ')
    parse_and_display(name)
    repeat = input('Do you want to enter another name? Y/N ')
    if repeat == 'Y':
        name = None
    else:
        print('Thank you, goodbye')