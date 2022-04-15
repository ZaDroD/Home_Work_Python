# 2. Найти максимальное из пяти чисел
        # #простой способ:   print(max(numbers))

array = [1, 8, 10, 5, 6]
print(array)
max = array[0]
for i in array:
    if i > max:
        max = i
print(max)