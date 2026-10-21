import string

def is_prime(n):
    """Проверка, является ли n простым числом."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def variant_1():
    s = input("Введите строку: ")
    punct = set(string.punctuation)   
    
    words = []
    delims = []       
    cur = []
    buf = []

    for ch in s:
        if ch in punct or ch.isspace(): #isspace - probel
            if cur:
                words.append(''.join(cur))
                cur = []
            buf.append(ch)
        else:
            if buf:
                delims.append(''.join(buf))
                buf = []
            cur.append(ch)
    if cur:
        words.append(''.join(cur))
    if buf:
        delims.append(''.join(buf))

    prime_indices = []
    for i, w in enumerate(words):
        # слово должно состоять только из цифр
        if w.isdigit() and is_prime(int(w)):
            prime_indices.append(i)

    if len(prime_indices) < 2:
        print("Недостаточно простых чисел для обмена.")
        return

    first = prime_indices[0]
    last = prime_indices[-1]

    words[first], words[last] = words[last], words[first]

    result = words[0] if words else ''
    for i in range(1, len(words)):
        result += delims[i-1] + words[i]

    print("Результат:", result)

def variant_5():
    s = input("Введите строку: ")
    punct = set(string.punctuation)

    best = []
    max_distinct = -1
    cur = []

    for ch in s + '.':
        if ch in punct or ch.isspace():
            if cur:
                w = ''.join(cur)
                d = len(set(w))  
                if d > max_distinct:
                    max_distinct = d
                    best = [w]
                elif d == max_distinct:
                    best.append(w)
                cur = []
        else:
            cur.append(ch)

    if not best:
        print("Нет слов.")
    else:
        print(f"Различных символов: {max_distinct}")
        print(" ".join(best))


variant_1()

variant_5()