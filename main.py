# Password Manager

import random
import os
import json
import time

def clear_terminal():
    return os.system('cls') if os.name == 'nt' else os.system('clear')

def file_start():
    global storage_file
    print('Loading...')
    for root, dirs, files in os.walk(os.path.abspath(os.path.dirname(os.path.realpath(__file__)))):
        for file in files:
            for i in file.split(r'\/'):
                if i.startswith('storage_for_passwordMANAGER_byRAM9_LonGnAMESfoRaReaSOncapatlizationNo.json'):
                    clear_terminal()
                    print('Done!')
                    time.sleep(1.5)
                    clear_terminal()
                    return (os.path.join(root, file))

try:
    storage_file = str(file_start())
    with open(storage_file) as json_file:
        storage = json.load(json_file)
except:
    clear_terminal()
    print('An error has occured!\nThe system has been unable to locate the storage file needed for the program to run ...\nIt is under the name "storage_for_passwordMANAGER_byRAM9_LonGnAMESfoRaReaSOncapatlizationNo.json"\nIf you find it, put this program and the storage file together in a folder (prefrably by themselves)\n\nHopefully thatll fix it! Though, if it doesnt then it is very likely that there is a problem that occured with your system and not the app.')

def password_entryTime():
    while True:
        test_confirm = input('Hello! Welcome to Password-Manager.\nto get started, enter your password\n\n{Type Here}: ')
        if test_confirm == storage['master']:
            clear_terminal()
            print('Alright! Correct password, press "ENTER" to continue')
            input()
            clear_terminal()
            break
        else:
            clear_terminal()
            print(f'Incorrect password!\nPress "ENTER" to continue')
            input()
            clear_terminal()

if storage['master'] == 'placeholder':
    master_setup = input('Hello, time for configuration!\nEnter you master-password here\n\n{Type Here}: ')
    clear_terminal()
    confirmation = input(f'Alright, {master_setup} it is? (y/n): ').lower()
    if confirmation == 'y':
        storage['master'] = master_setup
        with open(storage_file, 'w') as fp:
            json.dump(storage, fp)
        print(f'\nAlright, "{master_setup}" has been set up as the master password!\nDont forget it, youll need to type it in each time you log in!\n\nPress "ENTER" to continue')
        input()
        clear_terminal()
    else:
        print(f'Oh, it looks like "{master_setup}" isnt a winner :/\n')
        master_setup = input('Enter you master-password here\n\n{Type Here}: ')
        storage['master'] = master_setup
        with open(storage_file, 'w') as fp:
            json.dump(storage, fp)
        print(f'\nAlright, "{master_setup}" has been set up as the master password!\nDont forget it, youll need to type it in each time you log in!\n\nPress "ENTER" to continue')
        input()
        clear_terminal()
else:
    password_entryTime()

class Password:

    def __init__(self, length):
        
        self.length = length
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def generate(self, amount):

        for _ in range(amount):
            password = ''
            for _ in range(int(self.length)):
                password += random.choice(self.chars)
            print(password)

def pass_gen():
    amount = int(input('Welcome to Password Generator!\n\nHow many passwords would you like to generate? (number): '))
    clear_terminal()
    length = int(input('Welcome to Password Generator!\n\nWhat is the password length? (number): '))
    password = Password(length)
    clear_terminal()
    try:
        password.generate(amount)
    except:
        print('Invalid Input, press "ENTER" to return to menu')
        input()
        clear_terminal()
        pass_gen()

    print(f'\n\nAll {amount} Passwords, with a length of {length} characters were generated succesfully!')
    print('\nPress "ENTER" to return to menu')
    input()
    clear_terminal()
    main()

def pass_store():
    path = int(input('Password Storage\n\n[1] View all pass words\n[2] Remove password\n[3] Add passwords\n[4] Return to menu\n\n{Select option}: '))
    clear_terminal()
    if path == 1:
        if len(storage['passwords']) == 1:
            print('Password Storage\n\nNo Passwords yet!')
        else:
            for key, value in storage['passwords'].items():
                if key == 'placeholder':
                    continue
                print(f'Email: {key} | Password: {value}')
        print('\nPress "ENTER" to return to menu')
        input()
        clear_terminal()
        pass_store()
    elif path == 4:
        main()
    elif path == 2:
        if len(storage['passwords']) > 1:
            temp_dict = {}
            num = 0
            for key, value in storage['passwords'].items():
                num += 1
                if key == 'placeholder':
                    continue
                temp_dict[num] = f'{key}.{value}'
            for key, value in temp_dict.items():
                if key == 'placeholder':
                    continue
                e = value.split('.')[0]
                p = value.split('.')[1]
                print(f'[{key}] Email: {e} | Password: {p}')    
            enter_num = int(input('\nEnter the number that corresponds wth the password you would like to delete: '))
            try:
                email_for_delete = temp_dict[enter_num]
                email_for_delete = ((str(email_for_delete)).split('.'))[0]
                del storage['passwords'][email_for_delete]
                with open(storage_file, 'w') as fp:
                    json.dump(storage, fp)
            except:
                print(f'Invalid input, press "ENTER" to return to menu.')
                input()
                clear_terminal()
                pass_store()
            print('\nPress "ENTER" to return to menu')
            input()
            clear_terminal()
            pass_store()
        else:
            print('Password Storage\n\nNo Passwords yet!')
            print('\nPress "ENTER" to return to menu')
            input()
            clear_terminal()
            pass_store()
    else:
        new_pass = input('Enter the password you would like to input here: ')
        new_email = input('Enter the email: ')
        storage['passwords'][new_email] = new_pass
        with open(storage_file, 'w') as fp:
            json.dump(storage, fp)
        print('\nPassword saved succesfully!\n\nPress "ENTER" to return to menu')
        input()
        clear_terminal()
        pass_store()

def main():

    path = int(input('Welcome to Password Manager!\n\n[1] Password Storage\n[2] Password Generator\n\n{Select Option}: '))
    if path != 1:
        clear_terminal()
        pass_gen()
    else:
        clear_terminal()
        pass_store()


file_start()
main()
