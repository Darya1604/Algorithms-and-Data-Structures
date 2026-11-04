expression = input().split()

operation = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y}

stack = []
for symbol in expression:
    if symbol in operation:
        b, a = stack.pop(), stack.pop()
        stack.append(operation[symbol](a, b))
    else:
        stack.append(int(symbol))
print(stack[0])