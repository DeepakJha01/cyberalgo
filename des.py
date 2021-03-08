
def spaced(key, length):
    count = 0

    for i in range(len(key)):
        count+=1
        print(key[i],end='')

        if(count) == length:
            print(" ",end='')
            count = 0

def xor(a,b):
    n = len(a)

    ans = ""
    for i in range(n):
        if a[i]==b[i]:
            ans += "0"
        else:
            ans += "1"

    return ans

## key : string
def key_expansion(key):
    print("KEY EXPANSION ... \n")
    if(len(key)!=64):
        print("OOPS!! key not of 64 bits")
        exit()

    pc1 = [
        [57, 49, 41, 33, 25, 17, 9],
        [1, 58, 50, 42, 34, 26, 18],
        [10, 2, 59, 51, 43, 35, 27],
        [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15],
        [7, 62, 54, 46, 38, 30, 22],
        [14, 6, 61, 53, 45, 37, 29],
        [21, 13, 5, 28, 20, 12, 4]
    ]


    pc2 = [
        [14, 17, 11, 24, 1,5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]
    ]


    ## apply PC-1 permutation
    print("applying PC-1 permutation,")
    pc1_key = ""
    for i in range(len(pc1)):
        for j in range(len(pc1[i])):
            pc1_key += key[pc1[i][j]-1]
    print("K+ = ",end='')
    spaced(pc1_key,7)


    ## split into two halves
    print("\n\nwe split the key into 2 halves")
    c0 = pc1_key[:28]
    d0 = pc1_key[28:]
    print("c0 = ",end='')
    spaced(c0,7)
    print("\nd0 = ",end='')
    spaced(d0,7)


    ## 1 bit circular left shift for first iteration
    print("\n\nFor first iteration, number of left circular shifts = 1")
    c1 = c0[1:] + c0[0]
    d1 = d0[1:] + d0[0]
    print("c1 = ", end='')
    spaced(c1, 7)
    print("\nd1 = ", end='')
    spaced(d1, 7)


    c1d1 = c1 + d1

    ## apply PC-2 permutation
    print("\n\napplying PC-2 permutation,")
    pc2_key = ""
    for i in range(len(pc2)):
        for j in range(len(pc2[i])):
            pc2_key += c1d1[pc2[i][j]-1]
    print("K1 = ",end='')
    spaced(pc2_key,6)
    print("")

    return pc2_key



def encryption(message, key48):
    if(len(message)!=64):
        print("\n\nOOPS!! message not of 64 bits")
        exit()

    ip_table = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]

    ebit_table = [
        [32, 1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8, 9],
        [8, 9, 10, 11, 12, 13],
        [12, 13, 14, 15, 16, 17],
        [16, 17, 18, 19, 20, 21],
        [20, 21, 22, 23, 24, 25],
        [24, 25, 26, 27, 28, 29],
        [28, 29, 30, 31, 32, 1]
    ]

    print("\n\nENCRYPTION ...\n")

    ## initial permutation
    print("applying initial permutation,")
    ip = ""
    for i in range(len(ip_table)):
        for j in range(len(ip_table[i])):
          ip += message[ip_table[i][j]-1]
    print("IP = ",end='')
    spaced(ip, 4)


    print("\n\nSplit into L32 + R32,")
    l0 = ip[:32]
    r0 = ip[32:]
    print("l0 = ", end='')
    spaced(l0, 4)
    print("\nr0 = ", end='')
    spaced(r0, 4)


    print("\n\nExpanded permutation on R32 to convert to 48 bits,")
    er0 = ""
    for i in range(len(ebit_table)):
        for j in range(len(ebit_table[i])):
            er0 += r0[ebit_table[i][j]-1]
    print("E(r0) = ",end='')
    spaced(er0, 6)


    print("\n\nKey(48 bit) XOR R(48 bit),")
    print("K1 = ",end='')
    spaced(key48,6)
    print("\nE(r0) = ",end='')
    spaced(er0, 6)
    val = xor(key48, er0)
    print(f"\nK1 xor E(R0) = ",end='')
    spaced(val,6)






key = "0000000100000001000000000000000100000000000000000000000000000001"
message = "0000000100000001000000000000000100000000000000010000000000000001"
# # print(len(key))
# print(len(message))
key48 = key_expansion(key)
encryption(message, key48)


