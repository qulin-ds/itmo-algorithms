from math import comb

def generate(start, current):
    if len(current) == K:
        print(*current)
        return

    for i in range(start, N + 1):
        current.append(i)
        generate(i + 1, current)
        current.pop()


N, K = map(int, input().split())

print(comb(N, K))

current = []

generate(1, current)