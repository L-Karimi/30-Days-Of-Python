b = 3
if b < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
    
    
    
c = 4
if c < 0:
    print('A is a negative number')
    
elif c<0:
    print('')
else:
    print('A is zero')
    
d = 6
print('A is my number ') if d<6 else print('A is not my number')
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
    user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')