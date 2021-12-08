lines = [line for line in open("input","r")]

digits = []
outputs = []

total = 0

for d, o in [line.split("|") for line in lines]:
    these_digits = d.strip().split()
    this_output = [char for char in o.strip().split()]

    
    digits.append(these_digits)
    outputs.append(this_output)

    digit_segs = [-1] * 10
    pinout = [-1] * 7

    one = [digit for digit in these_digits if len(digit) == 2][0]
    digit_segs[1] = set([char for char in one])
    
    four = [digit for digit in these_digits if len(digit) == 4][0]
    digit_segs[4] = set([char for char in four])

    seven = [digit for digit in these_digits if len(digit) == 3][0]
    digit_segs[7] = set([char for char in seven])
    pinout[0] = digit_segs[7] - digit_segs[1]

    eight = [digit for digit in these_digits if len(digit) == 7][0]
    digit_segs[8] = set([char for char in eight])

    nine_six_zero = [digit for digit in these_digits if len(digit) == 6]
    while -1 in (digit_segs[9],digit_segs[6],digit_segs[0]):
        for nsz in nine_six_zero:
            chars = set([char for char in nsz])
            if len(set.intersection(chars,digit_segs[1])) == 1: #six
                pinout[5] = set.intersection(chars,digit_segs[1])
                pinout[2] = digit_segs[1] - pinout[5]
                digit_segs[6] = chars

            elif len(chars - digit_segs[4]) == 2: # nine
                digit_segs[9] = chars
                pinout[6] = chars - digit_segs[4] - pinout[0]
                pinout[4] = digit_segs[8] - chars

            else: #zero
                digit_segs[0] = chars
                pinout[3] = digit_segs[8] - chars

    five_three_two = [digit for digit in these_digits if len(digit) == 5]

    while -1 in (digit_segs[5],digit_segs[3],digit_segs[2]):
        for ftt in five_three_two:
            chars = set([char for char in ftt])

            if len(set.intersection(pinout[2], chars)) == 0: # five
                print("five")
                digit_segs[5] = chars
            elif len(set.intersection(pinout[5],chars)) == 0: #two
                print("two")
                digit_segs[2] = chars
                if pinout[4] == -1:
                    continue
                pinout[1] = digit_segs[0] - digit_segs[7] - pinout[6] - pinout[4]

            else: #three
                digit_segs[3] = chars
                print("three")

    print(digit_segs)
    print(pinout)

    for i,this_digit in enumerate(this_output):
        these_segs = set([char for char in this_digit])
        print(digit_segs.index(these_segs))
        total += digit_segs.index(these_segs) * (10 ** (3 - i))
print(total)
