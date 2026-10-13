prices = list(map(int, input().split()))

stack = []
spans = [0] * len(prices)

for i in range(len(prices)):
    while stack and prices[stack[-1]]<=prices[i]:
        stack.pop()
    if stack == []:
        spans[i] = i + 1
    else:
        spans[i] = i - stack[-1]
    stack.append(i)
print(*spans)

import sys

#prices = list(map(int, sys.stdin.buffer.readline().split()))

#stack = []
#spans = []

#for i in range(len(prices)):
#    while stack and prices[stack[-1]] <= prices[i]:
#        stack.pop()
#
#    if not stack:
#        spans.append(i + 1)
#    else:
#        spans.append(i - stack[-1])
#
#    stack.append(i)

#sys.stdout.write(' '.join(map(str, spans)))