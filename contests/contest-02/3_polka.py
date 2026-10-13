stack = []

expression = input().split()

for element in expression:
    if element.isdigit() == True:
        stack.append(int(element))
    else:
        b = stack.pop()
        a = stack.pop()
        if element == '+':
            c = b+a
        if element == '-':
            c = a-b
        if element == '*':
            c = b*a
        stack.append(c)
print(stack[0])