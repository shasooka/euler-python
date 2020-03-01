# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys

def main():
    #max_number=int(sys.argv[1])
    mul = [20,19,18,17,16,14,13,11]
    start = 2520

    while start:
        
        for i in mul:
            fact = 0
            if start%i != 0:
                fact = 1
                break
        if fact == 1:
            start = start + 20
        else:
            print ("Small num is:" , start)
            break

if __name__== "__main__":
    main()
