length = int(input('Enter the list length for count 2 pows: '))
listPows = [str]
index = 0

while index < length:
    listPows.append('2^' + str(index) + ' is ' + str(2 ** index))
    index += 1

print('Your list with calculated pows for 2 (it\'s length - ' + str(length) + ' ):')
print(listPows)
