num = int(input('Enter the number for check to divide on 3 without remainder: '))

if num % 3 == 0:
    print('Your input divide on 3 without remainder. Your input: ' + str(num))
else:
    print('Your input divide on 3 with remainder. You input: ' + str(num) + ' Remainder: ' + str(num % 3))