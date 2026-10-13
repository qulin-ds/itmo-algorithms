queue = []
head = 0

def push(x):
    queue.append(x)

def pop():
    global head
    if head >= len(queue):
        return 'Error'
    else:
        a = queue[head]
        head += 1
        return a

def get():
    if head >= len(queue):
        return 'Error'
    else:
        return queue[head]

def size():
    return len(queue) - head


Q = int(input())

for i in range(Q):
    command = input().split()

    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "get":
        print(get())
    elif command[0] == "size":
        print(size())