lines = [line.strip() for line in open("input2","r").readlines()]

total = 0

for line in lines:
    stack = []
    for char in line:
        if char in ('([{<'):
            stack.append(char)
        else:
            if char == ")" and stack[-1] != "(":
                total += 3
                break
            if char == "]" and stack[-1] != "[":
                total += 57
                break
            if char == "}" and stack[-1] != "{":
                total += 1197
                break
            if char == ">" and stack[-1] != "<":
                total += 25137
                break
            stack.pop()


print(total)
