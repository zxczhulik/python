import math

def sum_of_digits(n: int) -> int:
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s

def max_digit(n: int) -> int:
    mx = 0
    n = abs(n)
    while n > 0:
        d = n % 10
        if d > mx:
            mx = d
        n //= 10
    return mx

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func1(x: int)-> bool:
    while x >= 1:
        temp_x = x 
        last_digit = temp_x % 10
        while temp_x >= 1:
            temp_x //= 10
            temp_digit = temp_x % 10
            if temp_digit == last_digit: return True
        x //= 10
    return False

def find_min_digit(x: int) -> int:
    x = abs(x)
    min = 9
    while x > 0:
        if x % 10 < min and x % 10 != 0:
            min = x % 10
        x //= 10
    return min 

def func2(x: int) -> int:
    min = find_min_digit(x)
    dev = min if min != 0 else 1
    n = 0
    new_x = 0
    while x >= 1:
        if ((x % 10) % dev) != 0:
            new_x += (x % 10) * (10**n)
            n += 1
        x //= 10
    return new_x

def is_perfect(n: int) -> bool:
    if n <= 1: return False
    s = 1  # 1 всегда является делителем
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    return s == n

def is_armstrong(n: int) -> bool:
    temp = n
    digits_count = 0
    
    while temp > 0:
        digits_count += 1
        temp //= 10
        
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        total += d ** digits_count
        temp //= 10
        
    return total == n


print(func1(234536))
print(func2(3254080))
print("Совершенные числа от 1 до 1000:")
for i in range(1, 1001):
    if is_perfect(i):
        print(i, end=" ") 
print("\nЧисла Армстронга от 1 до 1000:")
for i in range(1, 1001):
    if is_armstrong(i):
        print(i, end=" ")  
print("\nПростые числа с простой суммой цифр (от 1 до 150):")
for i in range(2, 151):
    if is_prime(i):
        s = sum_of_digits(i)
        if is_prime(s):
            print(i, end=" ")
print("\nЧисла, где сумма цифр = квадрат максимальной цифры (до 1000):")
for i in range(1, 1001):
    s = sum_of_digits(i)
    mx = max_digit(i)
    if s == mx ** 2:
        print(i, end=" ")
