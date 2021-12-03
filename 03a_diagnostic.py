values = [ int(line, 2) for line in open("input","r").readlines()]


for i in reversed(range(12)):
    sig_bits = [(val>>i & 1) for val in values]
    bit_sum = sum(sig_bits)

    if bit_sum >= len(values)/2:
        values = [val for val in values if val>>i & 1 == 1]
    else:
        values = [val for val in values if val>>i & 1 == 0]

    print(values)
    
    if len(values) == 1:
        break

oxygen = values[0]

values = [ int(line, 2) for line in open("input","r").readlines()]

for i in reversed(range(12)):
    sig_bits = [(val>>i & 1) for val in values]
    
    bit_sum = sum(sig_bits)

    if bit_sum < len(values)/2:
        values = [val for val in values if val>>i & 1 == 1]
    else:
        values = [val for val in values if val>>i & 1 == 0]

    print(bit_sum, values)
    if len(values) == 1:
        break

co2 = values[0]

print(oxygen, co2, oxygen*co2)
