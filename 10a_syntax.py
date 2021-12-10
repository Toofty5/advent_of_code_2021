lines = [line.strip() for line in open("input","r").readlines()]

total = 0
part_2_lines = []

for line in lines:
    valid_line = True
    stack = []
    for char in line:
        if char in ('([{<'):
            stack.append(char)
        else:
            if char == ")" and stack[-1] != "(":
                valid_line = False
                total += 3
                break
            if char == "]" and stack[-1] != "[":
                valid_line = False
                total += 57
                break
            if char == "}" and stack[-1] != "{":
                valid_line = False
                total += 1197
                break
            if char == ">" and stack[-1] != "<":
                valid_line = False
                total += 25137
                break
            stack.pop()
    if valid_line:
        part_2_lines.append(line)


print(total)

scores = []

for line in part_2_lines:
    valid_line = True
    stack = []
    for char in line:
        if char in ('([{<'):
            stack.append(char)
        else:
            if ( (char == ")" and stack[-1] == "(" ) or
                (char == "]" and stack[-1] == "[" ) or
                (char == "}" and stack[-1] == "{" ) or
                (char == ">" and stack[-1] == "<" ) ):
                stack.pop()
    print(stack)

    score = 0
    stack.reverse()
    for char in stack:
        score = 5 * score
        if char == "(":
            score += 1
        if char == "[":
            score += 2
        if char == "{":
            score += 3
        if char == "<":
            score += 4

    scores.append(score)
        
scores.sort()
print(scores)
i = int(len(scores) / 2)
print(scores[i])
