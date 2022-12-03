from collections import defaultdict, Counter
from itertools import pairwise
import functools
import math

from pprint import pprint


def p1(lines, p2=False):
    bits = ""
    for c in lines:
        bits += format(int(c), "04b")

    versions = []

    def parse(bits, pos=0):
        nonlocal versions
        version = bits[pos:pos+3]
        versions.append(version)
        pos += 3
        type = bits[pos:pos+3]
        pos += 3
        if type == '100': # is literal
            readbits = True
            out = ""
            while readbits:
                v = bits[pos:pos+5]
                pos += 5
                check = v[0]
                v = v[1:]
                if check == '0':
                    readbits = False
                out += v
            return pos, int(out, 2)
        else: # is_operator
            i = bits[pos]
            pos += 1
            subpackets = []
            if i == '0': # Length 
                l = bits[pos:pos+15]
                pos += 15
                limit = pos + int(l, 2)
                while pos < limit:
                    pos, v = parse(bits, pos)
                    subpackets.append(v)
            else: # numOfSubPackets
                l = bits[pos:pos+11]
                pos += 11
                for p in range(int(l, 2)):
                    pos, v = parse(bits, pos)
                    subpackets.append(v)

            out = ""
            type = int(type, 2)
            if type == 0:
                out = sum(subpackets)
            elif type == 1:
                out = math.prod(subpackets)
            elif type == 2:
                out = min(subpackets)
            elif type == 3:
                out = max(subpackets)
            elif type == 5:
                a, b = subpackets
                if a > b:
                    out = 1
                else:
                    out = 0
            elif type == 6:
                a, b = subpackets
                if a < b:
                    out = 1
                else:
                    out = 0
            elif type == 7:
                a, b = subpackets
                if a == b:
                    out = 1
                else:
                    out = 0

            return pos, out


    pos, values = parse(bits)
    # print(versions, values)
    s = [int(x, 2) for x in versions]

    print(sum(s))
    print(values)

    # def unpack(bit_string, value=0, part=None, sum=0):
    #     sum += int(bit_string[:3], 2)
    #     string = bit_string[3 : 6]
    #     packetID = int(string, 2)

    #     if packetID == 4: # is_literal 
    #         literal = ""
    #         for i in range( 6, len(bit_string) - 1, 5):
    #             literalPart = bit_string[i+1 : i+5]
    #             literal += literalPart
    #             if bit_string[i] != "0":
    #                 continue
    #             else : # is last group
    #                 literal_value = int(literal, 2)

    #                 if part == None: 
    #                     return sum
    #                 elif part == True and value > 0:
    #                     if literal_value > value: 
    #                         return sum
    #                     else:
    #                         # start of new pack
    #                         return unpack(bit_string[i + 5: ],
    #                                     value - literal_value, part, sum)
    #                 else: # False 
    #                     value[1] += 1
    #                     if value[1] == value[0]:
    #                         return sum
    #                     else: 
    #                         # start of new pack
    #                         return unpack(bit_string[i + 5: ], 
    #                                     value, part, sum)



    #     else: # is_operator
    #         length_id = bit_string[6]
    #         if length_id == "0": # 15 bits
    #             totalLength = int(bit_string[7 :  7 + 15], 2)

    #             # start of new pack
    #             return unpack(bit_string[7 + 15 :] , totalLength, True, sum)
                                
    #         else: # 11 bits
    #             numPackets = int(bit_string[7 :  7 + 11], 2)
    #             return unpack(bit_string[   7 + 11 :],  [numPackets, 0], False, sum)

        

    # return unpack(bits,  0) 

    


def p2(lines):
    return
   

if __name__ == "__main__":
    with open("day16.txt") as f:
        content = [int(x,16) for x in f.readline().strip()]

        print(p1(content))
    # print(p2(lines))




