from functools import reduce


class AES:
    def __init__(self) -> None:
        self.state = None
        self.cipher_key = None

    s_box = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

    def bin_number(self, num):
        # turn the number into a bit string and take of the '0b' at the beginning
        return ((bin(num))[2:])

    def ffAdd(self, a, b):
        return a ^ b

    def ffMultiply(self, a, b):
        # get just the bits and then reverse the string
        bits = (self.bin_number(b))[::-1]
        result = 0
        c = [a]
        for i in range(len(bits)):
            x = int(bits[i])
            if i == 0 and x & 1:  # and first bit is one
                result = self.ffAdd(result, a)
            else:
                result = self.xtime(result)
                # if the bit is set then XOR result together
                if x & 1:
                    c.append(result)

        return reduce((lambda num, num2: self.ffAdd(num, num2)), c)

    def xtime(self, num):
        if num & 0x80:
            num <<= 1
            num = self.ffAdd(num, 0x1B)
        else:
            num <<= 1
        num = num & 0xFF
        return num


    def subWord(self, num):
       pass


    def rotWord(self, num):
        pass


    def subBytes(self, my_state):
        for i in range(4):
            for j in range(4):
                r = 0
                c = self.bin_number(my_state[i][j])
                if len(c) > 4:
                    r = int(c[:len(c) - 4], 2)
                    c = int(c[len(c) - 4:], 2)
                else:
                    c = int(c, 2)
                my_state[i][j] = self.s_box[r][c]
        return my_state

    def shift_rows(self, my_state):
        for rowIdx in range(1, 4):
            # simply rotate the list around
            my_state[rowIdx] = (my_state[rowIdx])[rowIdx:] + (my_state[rowIdx])[:rowIdx]
        return my_state

    def mix_columns(self, state):
        for  col in state[0]
            for every row, r, in given_matrix
        c = mult(r, c)  # the new column replaces c
    

mult(row, col):
result = [0, 0, 0, 0]  # a 1D array of zeroes to start
for i where i < len(row), i++:
    # since the length of col and row are the same we can just use this for both
    idx = (i + 1) % len(row)
    ffadd(result(i), ffadd(ffmult(row(i), col(i))), ffmult(row(idx), col(idx)))
return result


state =  [ [0x19,0xa0,0x9a,0xe9],
                 [0x3d,0xf4,0xc6,0xf8],
                 [0xe3,0xe2,0x8d,0x48],
                 [0xbe,0x2b,0x2a,0x08]]

sub =    [[0xd4,0xe0,0xb8,0x1e],
                         [0x27,0xbf,0xb4,0x41],
                         [0x11,0x98,0x5d,0x52],
                         [0xae,0xf1,0xe5,0x30]]

shift =  [[0xd4, 0xe0, 0xb8, 0x1e],
                         [0xbf, 0xb4, 0x41, 0x27],
                         [0x5d, 0x52, 0x11, 0x98],
                         [0x30, 0xae, 0xf1, 0xe5]]

mix =    [[0x04, 0xe0, 0x48, 0x28],
                         [0x66, 0xcb, 0xf8, 0x06],
                         [0x81, 0x19, 0xd3, 0x26],
                         [0xe5, 0x9a, 0x7a, 0x4c]]

# xtime(57) = ae
# xtime(ae) =
# ae = 1010 1110 bit shifted becomes 1 0101 1100
c = AES()
#c.state = state
b = c.s_box[0][0]
if c.ffAdd(0x57, 0x83) == 0xd4 and c.xtime(0x57) == 0xae and c.xtime(0xae) == 0x47 and c.xtime(
        0x47) == 0x8e and c.xtime(0x8e) == 0x07:
    print("Success: ffAdd works!")

if c.ffMultiply(0x57, 0x13) == 0xfe:
    print("Success: ffMult works!")

state = c.subBytes(state)
if  state == sub:
    print("Success: subBytes works!")
state = c.shift_rows(state)
if state == shift:
    print("Success: shiftRows works!")
state = c.mix_columns(state)
if state == mix:
    print("Success: mix_columns works!")
#if c.subWord(0x00102030) == 0x63cab704 and c.subWord(0x40506070) == 0x0953d051 and c.subWord(0x8090a0b0) == 0xcd60e0e7 and c.subWord(0xc0d0e0f0) == 0xba70e18c:
 #   print("Success: subWord works!")

#if c.rotWord(0x09cf4f3c) == 0xcf4f3c09 and c.rotWord(0x2a6c7605) == 0x6c76052a:
 #   print("Success: rotWord works!")