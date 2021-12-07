crabs = [int(value) for value in open("input","r").read().split(",")]
print(crabs)

max_crab = max(crabs)
print(max_crab)

distances = []
lowest = max_crab**2



for i in range(max_crab):
    total = 0
    for crab in crabs:
        total += abs(crab - i)
    if total < lowest:
        lowest = total
print(lowest)
