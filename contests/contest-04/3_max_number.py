def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return True
    else:
        return False

def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)

def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result

N = int(input())
a = input().split()

a = merge_sort(a)

answer = ''.join(a)

if answer[0] == '0':
    print(0)
else:
    print(answer)
