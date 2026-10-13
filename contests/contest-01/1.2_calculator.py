N, M = map(int, input().split())
number = input()
answer = []
ost = 0
for i in range(N):
    ost = (ost * 10 + int(number[i])) % M
    answer.append(ost)
print(*answer)
