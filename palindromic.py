# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

def main():
    #max_number=int(sys.argv[1])
    f_num=999
    s_num=999
    max_numb=get_numb(f_num,s_num)
    print ("Total Sum is:" , max_numb)

def get_numb(f,s):
    l = 0
    for i in range(f,100,-1):
        for j in range(s,100,-1):
            m = str(i*j)
            r = m[::-1]
            if m == r:
                if int(m) > l:
                    l = int(m)
    return l

if __name__== "__main__":
    main()
