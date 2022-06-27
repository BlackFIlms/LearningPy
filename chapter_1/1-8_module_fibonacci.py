def getUserInput() -> int:
    return int(input('Please enter the number for calculate fibonacci sequence: '))

length = getUserInput()

while length < 0:
    print('You input the negative number, please provide the positive number!')
    length = getUserInput()

def fibonacci(n: int) -> list:
    if n == 0:
        return [0]
    elif n == 1 or n == 2:
        seq: list = fibonacci(n-1)
        seq.append(1)
        return seq
    else:
        seq: list = fibonacci(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

print(str(fibonacci(length)))