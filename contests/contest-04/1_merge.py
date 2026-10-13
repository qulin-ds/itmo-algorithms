def merge(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            # добавляем a[i]
            result.append(a[i])
            # двигаем i
            i += 1
        else:
            # добавляем b[j]
            result.append(b[j])
            # двигаем j
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1


    return result

N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
