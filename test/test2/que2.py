num = int(input('enter a no'))
first = num // 100
second = num // 10 % 10
third = num % 10

if first == 2*second and first == third / 2 :
    print('yes,you have done it')
else:
    print('please try next time')
    