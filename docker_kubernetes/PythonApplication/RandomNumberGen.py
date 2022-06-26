from random import randint

min_number = int(input('Please Enter Min Number'))
max_number = int(input('PLease Enter Max Number'))

if (max_number < min_number):
    print('Invalid Input')
else:
    rand_number = randint(min_number,max_number)
    print(rand_number)