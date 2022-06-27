length = int(input('Provide length for number sequence, which will be used for get sum odd: '))
result = 0

for x in range(length+1):
    if x%2 != 0:
        result += x

print('Calculated odd sum: ' + str(result) + ' from number sequence with length: ' + str(length))