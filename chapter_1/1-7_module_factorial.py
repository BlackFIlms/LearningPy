def getUserInput() -> int:
    return int(input('Please enter the number for calculate factorial: '))

num = getUserInput()

while num < 0:
    print('You input the negative number, please provide the positive number!')
    num = getUserInput()

def factorial(n: int) -> int:
    if n > 0:
        result = n * factorial(n - 1)
    else:
        result = 1
    return result

print('Factorial for ' + str(num) + ' is: ' + str(factorial(num)))