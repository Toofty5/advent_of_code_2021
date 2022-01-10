import textwrap
import re


class BitStream:
    def __init__(self, bits):
        self.ptr = 0
        self.bits = bits
    def __str__(self):
        return self.bits
    def __int__(self):
        return int(self.bits, 2)
    
    #returns next num bits without moving pointer
    def next(self, num=1): 
        ptr = self.ptr
        return self.bits[ ptr: ptr+num ]

    def tail(self):
        return self.bits[self.ptr:]
    
    #returns num bits and moves pointer
    def read(self, num):
        ptr = self.ptr
        bits = self.bits

        output = bits[ptr: ptr+num] if ptr + num < len(self.bits) else bits[ptr:]
        self.ptr += num
        return output

    
    def packetize(self):
        version = int(self.read(3),2)
        type_id = int(self.read(3),2)
        print(version, type_id)

        if type_id == 4:
            contents = []
            while(self.next() == "1"):
                contents.append(self.read(5)[1:])
            contents.append(self.read(5)[1:])
            print(contents)
            print(self.tail())
            return int(''.join(contents), 2)

        else:
            length_type_ID = int(self.read(1),2)

            if length_type_ID == 0:
                total_length = int(self.read(15),2)
                content_bits = self.read(total_length)

                content_stream = BitStream(content_bits)

                print(total_length, content_bits)
                while not re.match(self.tail(), r"0*"):
                    contents.append(self.packetize())
                print(contents)

            else:
                sub_packets = int(self.read(11),2)
                print(sub_packets)




def main():
    hex_in = [int(char, 16) for char in open("input","r").readline().strip()]
    bin_in = ''.join([format(digit, '04b') for digit in hex_in])

    stream = BitStream(bin_in)
    print(stream)
    print(int(stream))

    stream.packetize()

    

#return list of tuples

if __name__ == "__main__":
    main()

