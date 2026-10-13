numbers = list(map(int, input().split()))

answer = -1
answer_1 = -1
answer_2 = -1
zero = []
one = []
two = []

for number in numbers:
    if number % 3 == 0:
        zero.append(number)
    elif number % 3 == 1:
        one.append(number)
    else:
        two.append(number)

zero.sort(reverse=True)
one.sort(reverse=True)
two.sort(reverse=True)

if len(zero) >= 2:
    answer_1 = zero[0] + zero[1]
if len(one) >= 1 and len(two) >= 1:
    answer_2 = one[0] + two[0]


if answer_1 >= answer_2:
    print(answer_1)
else:
    print(answer_2)



    


