import random
numbers = [1,2,3,4,5,6,7,8,9,0]
account_number = []
money = 1000
bank_account_exists = False
name = input('What is your name? ')
print('Hello',name,'! This is a bank management system.')
options = {
    1:'view your bank account details',
    2:'make transactions',
    3:'create your account',
    4:'exit the program'
}
print(options)
player_action = int(input('What do you want to do?(Please choose from 1, 2, 3 or 4) '))
while player_action not in options:
    if player_action != int(player_action):
        print('Sorry, but that is not an integer value... Please try again...')
        print(options)
        player_action = int(input('What do you want to do?'))
    else:
        print('Sorry, but that was an invalid response. Please try again...')
        print(options)
        player_action = int(input('What do you want to do? '))
    if player_action in options:
        break
while player_action in options:
    if player_action == 1:
        if bank_account_exists:
            print('Your bank account number:- ',account_number)
            print('Your savings are:- $',money)
        else:
            print('Sorry, but you do not have an account...')
    elif player_action == 2:
        if bank_account_exists:
            transaction = input('Do you want to make deposition or withdrawal of your money from your account? ')
            if transaction.lower() == 'deposit' or transaction.lower() == 'deposition':
                amount_of_adding = int(input('How much money do you want to deposit in your account?'))
                money += amount_of_adding
            elif transaction.islower() == 'withdraw' or transaction.lower() == 'withdrawal':
                amount_of_borrowing = int(input('How much money do you want to withdraw from your account?'))
                if amount_of_borrowing > money:
                    print('Sorry, but you cannot borrow that much money...')
                else:
                    money -= amount_of_borrowing
            else:
                print('Sorry, but I did not understand')
        else:
            print('Sorry, but you do not have an account...')
    elif player_action == 3:
        if not bank_account_exists:
            for i in range(10):
                account_number.append(random.randint(0,9))
            print('Account Number:- ',account_number)
            print('Congrats! You have successfully made an account! You get $1000 when you create your account...')
            bank_account_exists = True
        else:
            print('Sorry, but you have already created account...')
    elif player_action == 4:
        print('Thanks for managing your account with us!')
        break
    else:
        print('Sorry, but that is an invalid response...')
    print(options)
    player_action = int(input('What do you want to do?(Please enter the option number only) '))