import textwrap


class BitStream:
    def __init__(self, bits):
        self.ptr = 0
        self.bits = bits
    
    #returns next num bits without moving pointer
    def next(self, num = 1): 
        return bits[ptr: ptr+num]
    
    #returns num bits and moves pointer
    def read(self, num):
        output = bits[ptr: ptr+num] if ptr + num < len(self.bits) else bits[ptr:]

        ptr += num
        return output

    def __str__(self):
        return self.bits

    def __int__(self):
        return int(self.bits, 2)



def main():
    hex_in = [int(char, 16) for char in open("input","r").readline().strip()]
    bin_in = ''.join([format(digit, '04b') for digit in hex_in])

    stream = BitStream(bin_in)
    print(stream)

    print(int(stream))



#return list of tuples

if __name__ == "__main__":
    main()

