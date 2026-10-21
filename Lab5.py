import random

# ВАРИАНТ 1
# list
n = int(input("Input amount of numbers: "))

choise = int(input(f"ввести числа вручную(1) или рандом(2): "))
if choise == 1:
    arr = [int(input(f"input {n+1} element: ")) for i in range(n)]
else:
    a = int(input(f"input left boerd: "))
    b = int(input(f"input right boerd: "))
    arr = [random.randint(a,b) for _ in range(n)]
print(arr);

mul = 1
for i in range(1,n,2):
    mul *= arr[i]
print(mul)

first_zero = -1
last_zero = -1
for i in range(i):
    if arr[i] == 0:
        if first_zero == -1:
            first_zero = i
        last_zero = i
print(sum(arr[first_zero:last_zero]))

i = 0
while i < n:
    if arr[i] >= 0:
        j = i+1
        while j<n and arr[j] >= 0:
            j += 1
        if j < n:
            temp = arr[j]
            for k in range(j,i,-1):
                arr[k] = arr[k-1]
            arr[i] = temp
    i += 1
print(arr)


# ВАРИАНТ 15
n = int(input("Input amount of numbers: "))

choise = int(input(f"ввести числа вручную(1) или рандом(2): "))
if choise == 1:
    arr = [int(input(f"input {n+1} element: ")) for i in range(n)]
else:
    a = int(input(f"input left boerd: "))
    b = int(input(f"input right boerd: "))
    arr = [random.uniform(a,b) for _ in range(n)]
print(arr);

max_el = max(arr)
min_el = min(arr)
max_idx = -1
min_idx = -1
for i in range(n):
    if arr[i] == max_el:
        max_idx = i
    if arr[i] == min_el:
        min_idx = i
 
start = min(min_idx, max_idx)
end = max(min_idx, max_idx)
mul = 1
for i in range(start + 1, end):
    mul*=arr[i]
print(mul)

even_indices = list(range(1, n, 2))
even_values = [arr[i] for i in even_indices]
even_values.sort()

for k in range(len(even_indices)):
    arr[even_indices[k]] = even_values[k]
