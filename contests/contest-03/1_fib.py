import sys

#увелечение глубины рекурсии
sys.setrecursionlimit(200000)

def fib_dunny_memo(n, my_cache, M):
    if n in my_cache:
        return my_cache[n]

    if n <= 1:
        my_cache[n] = 1 % M
        return my_cache[n]

    my_cache[n] = (fib_dunny_memo(n - 1, my_cache, M) + fib_dunny_memo(n - 2, my_cache, M)) % M

    return my_cache[n]


N, M = map(int, input().split())

cache = {}

print(fib_dunny_memo(N, cache, M))