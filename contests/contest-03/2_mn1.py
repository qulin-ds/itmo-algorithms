def search(arr, current_sum, position, X, used):
    if position == len(arr):
        if current_sum == X and used:
            return True
        return False
    take = search(arr,current_sum + arr[position], position + 1, X, True)
    skip = search (arr, current_sum, position + 1, X, used)
    return take or skip

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

if search(arr, 0, 0, S, False):
    print("Yes")
else:
    print("No")