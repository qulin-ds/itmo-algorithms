max_even_1 = 0
max_even_2 = 0 
max_odd_1 = 0
max_odd_2 = 0
answer = 0
numbers = list(map(int, input().split()))

for number in numbers:
    if number % 2 == 0:
        if number>=max_even_1:
            max_even_2 = max_even_1
            max_even_1 = number
        elif number > max_even_2:
            max_even_2 = number

    else:
        if number>=max_odd_1:
            max_odd_2 = max_odd_1
            max_odd_1 = number
        elif number > max_odd_2:
            max_odd_2 = number

odd_sum = max_odd_1 + max_odd_2
even_sum = max_even_1 + max_even_2

if max_odd_2 == 0 and max_even_2 == 0:
    print(-1)
elif max_odd_2 == 0:
    print(even_sum)
elif max_even_2 == 0:
    print(odd_sum)
else:
    print(max(odd_sum, even_sum))