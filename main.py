print('Введите ширину трейгольника: ')

width_n = int(input())  # Ввод числа

i = 0
while i < width_n:  # Part 1
    print('*' * (width_n - i))
    i += 1

print('-----------------')

j = 1
while j <= width_n:  # Part 2
    print('*' * j)
    j += 1

print('-----------------')

k = 0
l = 1
while k < width_n:  # Part 3
    if width_n == 1:
        print('*')
        break
    if k == 0:
        print('*' * width_n)
    else:
        print(' ' * l + '*' * (width_n - k))
        l+=1
    k += 1

print('-----------------')

m = 1
while m <= width_n:  # Part 4
    if width_n == 1:
        print('*')
        break
    print(' ' * (width_n - m) + '*' * m)
    m += 1
