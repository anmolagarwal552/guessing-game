import random
print('GUESS A NUMBER BETWEEN 1 TO 50')
guess = random.randint(1,50)
quit = False
while not quit:
    user = int(input('>>>'))
    if user > guess:
        print('too high')
    elif user < guess:
        print('too low')
    else:
        print('OH YEAH finally found!')
        quit = True
