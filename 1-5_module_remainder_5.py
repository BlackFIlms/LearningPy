length = int(input('Enter the list length for get remainders for 5 which equals 3: '))
listRemainders = [int]

index = 0

while index < length:
    num = index % 5
    if num == 3:
        listRemainders.append(index)
    index += 1

print('Your list with calculated remainders for 5 which equals 3 (it\'s length - ' + str(length) + ' ):')
print(listRemainders)
print('Reverse remainders list:')
listRemainders.reverse()
print(listRemainders)