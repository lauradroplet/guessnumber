import random
r = random.randint(1,100)
while True:
    a = input('please give me a number:')
    a = int(a)
    if a == r: 
        print('you are right!')
        break
    else:
        if a > r:
            print('bigger than the answer')
        else:
            print('smaller than the answer')
