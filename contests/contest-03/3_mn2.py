def search(arr, current_sum, position, X, used):
    if position == len(arr):
        if current_sum == X and used:
            return []
        return None

    take = search(arr, current_sum + arr[position], position + 1, X, True)

    if take is not None:
        return [arr[position]] + take

    skip = search(arr, current_sum, position + 1, X, used)

    if skip is not None:
        return skip

    return None


N = int(input())
arr = list(map(int, input().split()))
S = int(input())

result = search(arr, 0, 0, S, False)

if result is None:
    print("No")
else:
    print("Yes")
    print(len(result))
    print(*result)