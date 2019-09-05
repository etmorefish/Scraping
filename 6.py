num = 2**100
print(num)

count = 0
while num > 0:
    if num % 10 == 6:
        count += 1
    num = num // 10
print(count)

pos = 0
for digit in str(2**100):
    pos += 1
    if digit =='9':
        break
print(' 2**100 is: %d \n the first posion of 9 is Pos.%d'%(2**100, pos))

i = 2
while (i < 100):
    flag = 0
    j = 2
    while(j <= (i/j)):
        if  i % j == 0:
            flag = 1
            break
        j += 1
    if (flag == 0):
        print(i,'是素数')
    i += 1

without9 = ''
for digit in str(2**100):
    if digit == '9':
        continue
    without9 += digit
    # if digit == '9':
    #     pass
    # else:
    #     without9 += digit
print('2**100 is :%d \n without9 is: %s'%(2**100,without9))
