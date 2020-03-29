from functools import reduce

def udp_add(num1,num2):
    numRes=num1+num2
    if numRes >=2**16:
        numRes-=(2**16-1)
        numRes=2**16-1-numRes
    return numRes

def udp_rdc(listnum):
    res=reduce(udp_add,listnum)
    return res



def main():
    numA=0B0110011001100000
    numB=0B0101010101010101
    numC=0B1000111100001100
    listnum=[numA,numB,numC]
    print("检验和为")
    print(udp_rdc(listnum))
    print("二进制为")
    print("{0:b}".format(udp_rdc(listnum)))

if __name__ == '__main__':
    main()