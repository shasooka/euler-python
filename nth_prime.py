# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sys
import math

def main():
    #in_number=int(sys.argv[1])
    nth_num=10001
    nth_prime = get_prime(nth_num)
    print ("Max Prime is:" , nth_prime)

def get_prime(numb):
    c = 1
    n = 2
    while 1:
        if is_prime(n):
            if c==numb:
                return n
                break
            c=c+1
        n=n+1

def is_prime(numb):
    i = 2
    is_prime = 1
    while i <= math.sqrt(numb):
        if (numb%i == 0):
            is_prime = 0
            break
        i = i +1
    return is_prime

if __name__== "__main__":
    main()