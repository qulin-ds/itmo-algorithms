N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
top, bottom, left, right = 0, N - 1, 0, M - 1
answer = []
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        answer.append(matrix[top][j])
    top += 1
    if top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            answer.append(matrix[i][right])
        right -= 1
    if top <= bottom and left <= right:
        for j in range(right, left - 1, -1):
            answer.append(matrix[bottom][j])
        bottom -= 1
    if left <= right and top <= bottom:
        for i in range(bottom, top - 1, -1):
            answer.append(matrix[i][left])
        left += 1
print(*answer)
