def variant_1():
    s = input("Введите строку: ")
    sep_str = input("Введите разделители (подряд): ")
    seps = set(sep_str)

    words = []
    delims = []  
    cur = []    
    buf_delim = []  

    for ch in s:
        if ch in seps:
            if cur:
                words.append(''.join(cur))
                cur = []
            buf_delim.append(ch)   
        else:
            if buf_delim:
                delims.append(''.join(buf_delim))
                buf_delim = []
            cur.append(ch)

    if cur:
        words.append(''.join(cur))
    if buf_delim:
        delims.append(''.join(buf_delim))

    if len(words) < 2:
        print("Нужно не менее двух слов.")
        return

    max_len = max(len(w) for w in words)
    idx_max = next(i for i, w in enumerate(words) if len(w) == max_len)

    min_len = min(len(w) for w in words)
    idx_min = max(i for i, w in enumerate(words) if len(w) == min_len)

    words[idx_max], words[idx_min] = words[idx_min], words[idx_max]

    result = words[0]
    for i in range(1, len(words)):
        result += delims[i-1] + words[i]

    print("Результат:", result)


def variant_7():
    s = input("Введите строку: ")
    sep_str = input("Разделители: ")
    seps = set(sep_str)

    vowels = set("aeiouAEIOU")
    result_words = [] 
    cur = []  

    for ch in s + sep_str[0]:
        if ch in seps:
            if cur:
                w = ''.join(cur)
                if w[0] in vowels:
                    w = w[0].upper() + w[1:]
                    result_words.append(w)
                cur = []
        else:
            cur.append(ch)

    if not result_words:
        print("Нет слов, начинающихся с гласной.")
    else:
        print(" ".join(result_words))

variant_7()

variant_1()