sequence = input()
stack = []
answer = True

for bracket in sequence:
    if bracket not in ["(", "{", "[", ")", "}", "]"]:
        continue
    if bracket in ["(", "{", "["]:
        stack.append(bracket)
        continue
    if len(stack) != 0 and (bracket == ")" and stack[-1] == "(" or
                            bracket == "]" and stack[-1] == "[" or
                            bracket == "}" and stack[-1] == "{"):
        stack.pop()
    else:
        answer = False
        break
if len(stack) != 0:
        answer = False
print("yes" if answer else "no")