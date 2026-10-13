numbers = list(map(int, input().split()))
summ = 0
min_odd = 1000001

for number in numbers:
    summ += number

    if number % 2 != 0:
        if number < min_odd:
            min_odd = number

if summ % 2 == 0:
    print(summ)
elif summ % 2 != 0:
    print(summ-min_odd)
elif summ == min_odd:
    print(0)
