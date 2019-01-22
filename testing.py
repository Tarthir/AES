import numpy as np
import AES as aes
starting_state =  [ [0x19,0xa0,0x9a,0xe9],
                 [0x3d,0xf4,0xc6,0xf8],
                 [0xe3,0xe2,0x8d,0x48],
                 [0xbe,0x2b,0x2a,0x08]]

sub = [[0xd4,0xe0,0xb8,0x1e],
                         [0x27,0xbf,0xb4,0x41],
                         [0x11,0x98,0x5d,0x52],
                         [0xae,0xf1,0xe5,0x30]]

shift = [[0xd4, 0xe0, 0xb8, 0x1e],
                         [0xbf, 0xb4, 0x41, 0x27],
                         [0x5d, 0x52, 0x11, 0x98],
                         [0x30, 0xae, 0xf1, 0xe5]]

mix = [[0x04, 0xe0, 0x48, 0x28],
                         [0x66, 0xcb, 0xf8, 0x06],
                         [0x81, 0x19, 0xd3, 0x26],
                         [0xe5, 0x9a, 0x7a, 0x4c]]

round = [[0xa4, 0x68, 0x6b, 0x02],
                          [0x9c, 0x9f, 0x5b, 0x6a],
                          [0x7f, 0x35, 0xea, 0x50],
                          [0xf2, 0x2b, 0x43, 0x49]]

key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
                          0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]

#expanded = [[0x2b, 0x7e, 0x15, 0x16], [0x28,0xae,0xd2,0xa6], [0xab,0xf7,0x15,0x88], [0x09,0xcf,0x4f,0x3c],
#                          [0xa0, 0xfa, 0xfe, 0x17], [0x88,0x54,0x2c,0xb1], [0x23,0xa3,0x39,0x39], [0x2a,0x6c,0x76,0x05],
#                          [0xf2c295f2], [0x7a96b943], [0x593580,0x7a], [0x73,0x59,0xf6,0x7f],
#                          [0x3d80477d], [0x4716fe3e], [0x1e237e,0x44], [0x6d,0x7a,0x88,0x3b],
#                          [0xef44a541], [0xa8525b7f], [0xb67125,0x3b], [0xdb,0x0b,0xad,0x00],
#                          [0xd4d1c6f8], [0x7c839d87], [0xcaf2b8,0xbc], [0x11,0xf9,0x15,0xbc],
 #                         [0x6d88a37a], [0x110b3efd], [0xdbf986,0x41], [0xca,0x00,0x93,0xfd],
 #                         [0x4e54f70e], [0x5f5fc9f3], [0x84a64f,0xb2], [0x4e,0xa6,0xdc,0x4f],
 #                         [0xead27321], [0xb58dbad2], [0x312bf5,0x60], [0x7f,0x8d,0x29,0x2f],
 #                         [0xac7766f3], [0x19fadc21], [0x28d129,0x41], [0x57,0x5c,0x00,0x6e],
 #                         [0xd014f9a8], [0xc9ee2589], [0xe13f0c,0xc8], [0xb6,0x63,0x0c,0xa6] ]
expanded = [0x2b7e1516, 0x28aed2a6, 0xabf71588, 0x09cf4f3c,
                          0xa0fafe17, 0x88542cb1, 0x23a33939, 0x2a6c7605,
                          0xf2c295f2, 0x7a96b943, 0x5935807a, 0x7359f67f,
                          0x3d80477d, 0x4716fe3e, 0x1e237e44, 0x6d7a883b,
                          0xef44a541, 0xa8525b7f, 0xb671253b, 0xdb0bad00,
                          0xd4d1c6f8, 0x7c839d87, 0xcaf2b8bc, 0x11f915bc,
                          0x6d88a37a, 0x110b3efd, 0xdbf98641, 0xca0093fd,
                          0x4e54f70e, 0x5f5fc9f3, 0x84a64fb2, 0x4ea6dc4f,
                          0xead27321, 0xb58dbad2, 0x312bf560, 0x7f8d292f,
                          0xac7766f3, 0x19fadc21, 0x28d12941, 0x575c006e,
                          0xd014f9a8, 0xc9ee2589, 0xe13f0cc8, 0xb6630ca6 ]
starting_state = np.array(starting_state)
state = np.array(starting_state)
sub = np.array(sub)
shift = np.array(shift)
mix = np.array(mix)
key = np.array(key)
expanded = np.array(expanded)
# xtime(57) = ae
# xtime(ae) =
# ae = 1010 1110 bit shifted becomes 1 0101 1100
c = aes.AES()
#c.state = state
if c.ffAdd(0x57, 0x83) == 0xd4 and c.xtime(0x57) == 0xae and c.xtime(0xae) == 0x47 and c.xtime(
        0x47) == 0x8e and c.xtime(0x8e) == 0x07:
    print("Success: ffAdd and xtime works!")

if c.ffMultiply(0x57, 0x13) == 0xfe:
    print("Success: ffMult works!")

if c.subWord([0x00, 0x10, 0x20, 0x30]) == [0x63, 0xca, 0xb7, 0x04] \
        and c.subWord([0x40, 0x50, 0x60, 0x70]) == [0x09, 0x53, 0xd0, 0x51] \
        and c.subWord([0x80, 0x90, 0xa0, 0xb0]) == [0xcd, 0x60, 0xe0, 0xe7] \
        and c.subWord([0xc0, 0xd0, 0xe0, 0xf0]) == [0xba, 0x70, 0xe1, 0x8c]:
    print("Success: subWord works!")

if np.array_equal(c.rotWord([0x09, 0xcf, 0x4f, 0x3c]), np.array([0xcf, 0x4f, 0x3c, 0x09])) \
        and np.array_equal(c.rotWord([0x2a, 0x6c, 0x76, 0x05]), np.array([0x6c, 0x76, 0x05, 0x2a])):
    print("Success: rotWord works!")

c.curr_round = 1
state = c.subBytes(starting_state)
if np.array_equal(state, sub):
    print("Success: subBytes works!")

invState = c.subBytes(state, c.InvSbox)
if np.array_equal(invState, starting_state):
    print("Success: invSubBytes works!")
state = sub # reset the matrix since we reversed it
state = c.shift_rows(state)
if np.array_equal(state, shift):
    print("Success: shiftRows works!")

invState = c.shift_rows(state, 1)
if np.array_equal(invState, sub):
    print("Success: invShiftRows works!")
state = shift
state = c.mix_columns(state)
if np.array_equal(state, mix):
    print("Success: mix_columns works!")

invState = c.mix_columns(state, c.inv_rgf_matrix)
if np.array_equal(invState, shift):
    print("Success: invMix_columns works!")
state = mix

# TODO need to setup testing for this, already did it manually, looks good
c.expanded_key = c.key_expansion(key)
#if w == expanded:
#    print("Success: key_expansion works!")
state = c.add_round_key(state)
if np.array_equal(state, round):
    print("Success: add_round_key works!")

state = c.add_round_key(state)
if np.array_equal(state, mix):
    print("Success: inv_add_round_key works!")

###
# cipher test from video
d = aes.AES()
vid_input = "328831e0435a3137f6309807a88da234"
#cipher = d.text_to_arr("2b28ab097eaef7cf15d2154f16a6883c")
d.expanded_key = d.key_expansion(key)  # TODO Bug with how we are getting cipher?
test_encrypted = d.cipher(vid_input)
test1_decrypted = d.inv_cipher(test_encrypted.copy())
if np.array_equal(d.initial_state, test1_decrypted):
    print("Success: D/E worked")
################################

my_input = "00112233445566778899aabbccddeeff"
cipher_key = d.text_to_arr("000102030405060708090a0b0c0d0e0f") # length of 32
#cipher_key2 = d.text_to_arr("000102030405060708090a0b0c0d0e0f1011121314151617") #len of 48
#cipher_key3 = d.text_to_arr("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f") #len of 64
#d.expanded_key = d.key_expansion(cipher_key)
#test1_encrypted = d.cipher(my_input)
#test1_decrypted = d.inv_cipher(test1_encrypted.copy())
#if np.array_equal(test1_encrypted, test1_decrypted):
#    print("Success: Encryption and decryption works!")
