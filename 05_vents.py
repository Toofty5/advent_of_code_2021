lines = [line.split() for line in open("input", "r")]

segments = []

for line in lines:
    x1,y1 = line[0].split(",")
    x2,y2 = line[2].split(",")

    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1,y2 = y2,y1

    segments.append((int(x1),int(y1), int(x2), int(y2)))


x_dict = {} 
y_dict = {} 

total = 0

for (x1,y1,x2,y2) in segments:

    if x1 == x2:
        total += abs(y1-y2)
        if x1 in x_dict:
            x_dict[x1].append((y1,y2))
            print(x_dict[x1])
        else:
            x_dict[x1] = [(y1,y2)]
    else: 
        total += abs(x1-x2)
        if y1 in y_dict:
            y_dict[y1].append((x1,x2))
        else:
            y_dict[y1] = [(x1,x2)]
print(total)
#find crosses
for x_key in x_dict:
    segments = x_dict[x_key]
    
    for y_key,y_segs in y_dict.items():
        for (y1,y2) in segments:
            if y1 <= y_key <= y2:
                total += 1
                break


print(total)
print(x_dict)
        
