hex_in = [int(char, 16) for char in open("input","r").readline().strip()]
bin_in = ''.join([format(digit, '04b') for digit in hex_in])



def main():
    print(bin_in)
    print(packetize(bin_in))



#return list of tuples
def packetize(in_str):
    pkt_ver = int(in_str[:3], 2)
    pkt_type = int(in_str[3:6], 2)

    return (pkt_ver,pkt_type)

if __name__ == "__main__":
    main()

