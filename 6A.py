def find_K_and_P(arr):
    K = 0
    P = 1
    for num in arr:
        if num > 2:
            break
        K += 1
        P *= num
    return K, P

# Пример массива
A = [1, 2, 3, 4, 5]
K, P = find_K_and_P(A)

print("Исходный массив A:", A)
print("Количество элементов K:", K)
print("Произведение элементов P:", P)
