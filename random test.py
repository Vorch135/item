import random

x_list = ['Restaurant', 'Hotel', 'Bank', 'Auto Shop', 'Park', 'Hospital']
x_random_location = random.choice(x_list)

if x_random_location == 'Bank':
    print('I love money')
elif x_random_location == 'Auto Shop':
    print('Cars are cool!')
elif x_random_location == 'Restaurant':
    print('I love food!')
else:
    print('lets go somewhere else...')
