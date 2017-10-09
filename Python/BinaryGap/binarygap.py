#!/usr/bin/python
def BinaryGap(N):
    """
    BinaryGap - Counts the 0's between binary 1's
    and returns the largest gap
    1001 = 2
    100010100 = 3
    1010000 = 1
    :param N: Non-negative integer between 1 and 2,147,483,647
    :type N: int
    :return: max number of zeroes separated by 1 in binary form
    :rtype: int
    """
    negative = False
    threshold = False
    if N < 0:
        N = abs(N)
        negative = True
    slicer = N
    zeros = 0
    max = 0
    last_max = 0
    
    while slicer != 0:
        part = slicer % 2
        slicer = int(slicer / 2)
        if part == 0:
            zeros+=1
        else:
            if zeros > last_max and threshold:
                max = zeros
                last_max = max
            zeros = 0
            threshold = True
    return max

def main():
    ansi=True
    while(1):
        print("BinaryGap - Type 0 to Exit")
        data_val = int(input("Enter a number:"))
        if not data_val:
            exit()
        binary_repr = str(bin(data_val)).replace('0b','').replace('-','(-)') # strip out the 0b/-0b prepended to the number
        gap = BinaryGap(data_val)
        RED = "\033[1;31;40m"
        CSI = "\033[0m"
        if ansi:
            formatted_bin = binary_repr.replace('0'*gap,"{}{}{}".format(RED,'0'*gap,CSI))
        else:
            formatted_bin = binary_repr
        print "Int: {} Binary: {}".format(data_val, formatted_bin )
        print "Binary Gap Value: {}".format(BinaryGap(data_val))
        
if __name__ == '__main__':
    main()
