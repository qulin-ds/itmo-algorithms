def merge(a, temp, left, mid, right):
    i = left
    j = mid
    k = left
    count = 0

    while i < mid and j < right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            count += mid - i
            j += 1
        k += 1

    while i < mid:
        temp[k] = a[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = a[j]
        j += 1
        k += 1

    for i in range(left, right):
        a[i] = temp[i]

    return count


def merge_sort(a, temp, left, right):
    if right - left <= 1:
        return 0

    mid = (left + right) // 2

    count = 0

    count += merge_sort(a, temp, left, mid)
    count += merge_sort(a, temp, mid, right)
    count += merge(a, temp, left, mid, right)

    return count


N = int(input())
a = list(map(int, input().split()))

temp = [0] * N

answer = merge_sort(a, temp, 0, N)

print(answer)
