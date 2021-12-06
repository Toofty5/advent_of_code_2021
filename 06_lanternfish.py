fishes = [int(i) for i in open("input","r").read().split(',')]

print(fishes)
fish_dict= [0] * 9

for fish in fishes:
    fish_dict[fish] += 1

print(fish_dict)

for day in range(255):
    new_fresh_fish = fish_dict[1]
    new_baby_fish = fish_dict[0]

    for i in range(0,8):
        fish_dict[i] = fish_dict[i+1]

    fish_dict[8] = new_baby_fish # more baby fish
    fish_dict[7] += new_fresh_fish # reset fish

    print(sum(fish_dict))
