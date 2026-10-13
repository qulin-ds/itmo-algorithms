N = int(input())

print(2 ** N - 1)

def hanoi(n, from_rod, to_rod, spare_rod):
    if n == 1:
        print(1, from_rod, to_rod)
        return

    hanoi(n - 1, from_rod, spare_rod, to_rod)
    print(n, from_rod, to_rod)
    hanoi(n - 1, spare_rod, to_rod, from_rod)
hanoi(N, 1, 3, 2)