numbers = list(map(int, input().split()))

zero = []
one = []
two = []
sum = 0

for number in numbers:
    if number % 3 == 0:
        zero.append(number)
    elif number % 3 == 1:
        one.append(number)
    else:
        two.append(number)

for number in numbers:
    sum += number

one.sort()
two.sort()

sum_1 = -1
sum_2 = -1

if sum % 3 == 0:
    print(sum)

elif sum % 3 == 1:
    if len(one) >= 1:
        sum_1 = sum - one[0]
    if len(two) >= 2:
        sum_2 = sum - two[0] - two[1]

    print(max(sum_1, sum_2))

else:
    if len(two) >= 1:
        sum_1 = sum - two[0]
    if len(one) >= 2:
        sum_2 = sum - one[0] - one[1]

    print(max(sum_1, sum_2))