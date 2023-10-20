# 1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
def sieve(x):
    b = set(x)
    c = tuple(b)
    c = c[::-1]
    return c
result = sieve(a)
print(result)


# 2
a = '!КЛОУН!'
b = '-- уклон --'
def anagramms(word1, word2):
    w1 = word1.lower()
    w2 = word2.lower()
    s1 = list()
    s2 = list()
    for i in w1:
        if i.isalpha():
            s1.append(i)
    for j in w2:
        if j.isalpha():
            s2.append(j)
    s1.sort()
    s2.sort()
    result = s1 == s2
    return result
print('Слова являюся анагараммами' if anagramms(a, b) is True else 'Слова являюся анагараммами')


# 3
n = int(input('Введите номер месяца'))
def seasons(n):
    mounth = n
    if mounth in [1, 2, 12]:
        return 'Зима'
    elif mounth in [3, 4, 5]:
        return 'Весна'
    elif mounth in [6, 7, 8]:
        return 'Лето'
    elif mounth in [9, 10, 11]:
        return 'Осень'
print(seasons(n))


# 4
a = int(input('Введите число'))
def digit(number):
    count = 0
    while number != 0:
        number = number // 10
        count = count + 1
    return count
print('Количество разрядов =', digit(a))


# 5
a = int(input('Введите сумму вклада'))
b = int(input('Введите срок вклада'))
def bank(x, y):
    for i in range(y):
        x = x + (x * 0.1)
    return x
print('Итоговая сумма:', bank(a, b))


# 6
a = int(input('Первое число'))
b = int(input('Введите второе число'))
if b == 0:
    b = int(input('Введите второе число, не равное 0'))
c = input('Ввведите тип операции')
def arithmetic(a, b, c):
    if c == "+":
        z = f'{a} {c} {b} = {a + b}'
    elif c == "-":
        z = f'{a} {c} {b} = {a - b}'
    elif c == "*":
        z = f'{a} {c} {b} = {a * b}'
    elif c == "/":
        z = f'{a} {c} {b} = {a / b}'
    else:
        z = "Неизвестная операция"
    return z
print(arithmetic(a, b, c))


# 7
n = int(input("Введите число - "))
def factorial(n):
    if n == 0:
        f = 1
    else:
        f = n * factorial(n-1)
    return f
print(factorial(n))


# 8
x = int(input("Введите число (основание)"))
y = int(input("Введите целое число (степень)"))
def power(x, y):
    if y == 1:
        p = x
    else:
        p = x * power(x, y-1)
    return p
print(power(x, y))


# 9
x = int(input("Введите целое число"))
def fib(x):
    if x == 1 or x == 2:
        f = 1
    else:
        f = fib(x-1) + fib(x-2)
    return f
print(f'Число Фибоначчи с индексом {x} равно: {fib(x)}')


# 10
n = int(input('Введите высоту матрицы'))
m = int(input('Введите ширину матрицы'))
def spiral_matrix(n, m):
    matrix = [[0] * m for i in range(n)]
    x = 0
    y = 0
    dx = 0
    dy = 1
    for j in range(1, n * m + 1):
        matrix[x][y] = j
        if matrix[(x + dx) % n][(y + dy) % m]:
            dx, dy = dy, -dx
        x = x + dx
        y = y + dy
    return matrix
matrix = spiral_matrix(n, m)
for i in range(0, n):
    print(matrix[i][:])


# 11
def concat(*args):
    a = map(str, args)
    b = ''.join(a)
    return b
print(concat('car', 'cat', 1234, 'dog', '-+', True))


# 12
def summa(*args):
    result = 0
    for i in args:
        result = result + i**2
    return result
print(summa(1, 2, 3, 4))
print(summa(1, 2))


# 13
def func(x):
    old_str = x
    a = old_str.split(' ')
    while '' in a:
        a.remove('')
    new_str = ' '.join(a)
    print(new_str)
func('a     b    c   d  e f')


# 14
def func(*args):
    word = ''
    for i in args:
        if len(i) > len(word):
            word = i
    return word
print('Слово наибольшей длины:', func('aaaaa', 'aaaa', 'aa'))


# 15
def sandwich(text):
    t = text
    if len(t) % 2 == 1:
        t = t + '_'
    ln = len(t)
    t1 = t[0:int(ln/2)]
    t2 = t[int(ln/2):ln]
    t = ''
    for i in range(int(ln/2)):
        t = t + t1[i] + t2[i]
    return t
print(sandwich('aaaabbb'))


# 16
def sandwich_reverse(text):
    t = text
    t1 = ''
    t2 = ''
    for i in range(0, len(t), 2):
        t1 = t1 + t[i]
        t2 = t2 + t[i+1]
    return t1 + t2
print(sandwich_reverse('abababa_'))