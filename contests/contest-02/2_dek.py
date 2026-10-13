Q = int(input())

deque = [0] * Q
left = 0
right = 0
count = 0

def push_back(x):
    global right, count

    deque[right] = x
    right = (right + 1) % Q
    count += 1

def push_front(x):
    global left, count

    left = (left - 1) % Q
    deque[left] = x
    count += 1

def pop_back():
    global right, count

    if count == 0:
        return "Error"

    right = (right - 1) % Q
    x = deque[right]
    count -= 1
    return x

def pop_front():
    global left, count

    if count == 0:
        return "Error"

    x = deque[left]
    left = (left + 1) % Q
    count -= 1
    return x


def get_back():
    if count == 0:
        return "Error"

    return deque[(right - 1) % Q]

def get_front():
    if count == 0:
        return "Error"

    return deque[left]

def size():
    return count

for i in range(Q):
    command = input().split()

    if command[0] == "push":
        if command[1] == "back":
            push_back(int(command[2]))
        else:
            push_front(int(command[2]))

    elif command[0] == "pop":
        if command[1] == "back":
            print(pop_back())
        else:
            print(pop_front())

    elif command[0] == "get":
        if command[1] == "back":
            print(get_back())
        else:
            print(get_front())

    else:
        print(size())