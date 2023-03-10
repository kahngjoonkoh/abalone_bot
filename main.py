import numpy as np
import math

start_pos = 0b111110000111111000000111000000000000000000000000000000000111000000111111000011111


board = 0b111110000111111000000111000000000000000000000000000000000111000000111111000011011
bitboard = 2346943363816235378703903
# bitboard = 2346943363816235378703899



def print_board(bb):
    # print("{0:b}".format(bitboard))
    x = bb
    x = flip_diagonal(bb)
    visualize(convert_to9x9(x))

    visualize(x)

# vertical
def flip_bits(x):
    return ((x >> 72)) | \
           ((x >> 54) & 261632) | \
           ((x >> 36) & 133955584) | \
           ((x >> 18) & 68585259008) | \
           ( x & 35115652612096) | \
           ((x << 18) & 17979214137393152) | \
           ((x << 36) & 9205357638345293824) | \
           ((x << 54) & 4713143110832790437888) | \
           ((x << 72));

# horizontal
def mirror_bits(x):
    return ((x >> 8) & 4731607904558235517441) | ((x & 4731607904558235517441) << 8) | \
           ((x >> 6) & 9463215809116471034882) | ((x & 9463215809116471034882) << 6) | \
           ((x >> 4) & 18926431618232942069764) | ((x & 18926431618232942069764) << 4) | \
           ((x >> 2) & 37852863236465884139528) | ((x & 37852863236465884139528) << 2) | \
           ( x & 75705726472931768279056)

def flip_diagonal(x):
    # x = 2417851639229258349412351
    k1 = 6124988953138320640
    k2 = 3689292520605548544
    k4 = 1085102592318504960
    visualize8x8(k1)
    x = convert_to8x8(x)
    t = k4 & (x ^ (x << 28))
    x ^= t ^ (t >> 28)
    t = k2 & (x ^ (x << 14))
    x ^= t ^ (t >> 14)
    t = k1 & (x ^ (x << 7))
    x ^= t ^ (t >> 7)
    return x

def flip_anti_diagonal(x):
    k1 = C64(0xaa00aa00aa00aa00);
    k2 = C64(0xcccc0000cccc0000);
    k4 = C64(0xf0f0f0f00f0f0f0f);
    x = convert_to8x8(x)
    t = x ^ (x << 36);
    x ^= k4 & (t ^ (x >> 36));
    t = k2 & (x ^ (x << 18));
    x ^= t ^ (t >> 18);
    t = k1 & (x ^ (x << 9));
    x ^= t ^ (t >> 9);
    return x;

    # return (x & 4740885567116192841984) | \
    #        ((x >> 10) & 9223372036854775808)

def convert_to8x8(x):
    return (x & 15) | \
           ((x >> 1) & 4080) | \
           ((x >> 2) & 1044480) | \
           ((x >> 3) & 267386880) | \
           ((x >> 4) & 4026531840) | \
           ((x >> 13) & 64424509440) | \
           ((x >> 14) & 17523466567680) | \
           ((x >> 15) & 4486007441326080) | \
           ((x >> 16) & 1148417904979476480) | \
           ((x >> 17) & 17293822569102704640)


def convert_to9x9(x):
    return (x & 15) | \
           ((x << 1) & 8160) | \
           ((x << 2) & 4177920) | \
           ((x << 3) & 2139095040) | \
           ((x << 4) & 64424509440) | \
           ((x << 13) & 527765581332480) | \
           ((x << 14) & 287104476244869120) | \
           ((x << 15) & 146997491837372989440) | \
           ((x << 16) & 75262715820734970593280) | \
           ((x << 17) & 2266735911777429702574080)

def visualize(x):
    for i, n in enumerate("{:0>81}".format("{0:b}".format(x % 2417851639229258349412352))):
        print(n, end="")
        if int(i) % 9 == 8:
            print("\n", end="")
    print("\n")

def visualize8x8(x):
    for i, n in enumerate("{:0>64}".format("{0:b}".format(x % 18446744073709551616))):
        print(n, end="")
        if int(i) % 8 == 7:
            print("\n", end="")
    print("\n")

print_board(bitboard)
# print("{0:b}".format(mirror_bits(bitboard)))