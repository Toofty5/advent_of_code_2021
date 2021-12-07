crabs = [int(value) for value in open("input","r").read().split(",")]

max_crab = max(crabs)

fuel_costs = []
this_fuel = 0
for i in range(1,max_crab+2):
    fuel_costs.append(this_fuel)
    this_fuel += i
print(fuel_costs)

lowest = 10000000000

for i in range(max_crab):
    total = 0
    for crab in crabs:
        this_dist = abs(crab - i)
        total += fuel_costs[this_dist]
    if total < lowest:
        lowest = total
print(lowest)
