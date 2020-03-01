# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

# Ref Prime Number: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

import sys
import math

def main():
    #in_number=int(sys.argv[1])
    in_number=600851475143
    sum = get_fact(in_number)
    print ("Max Prime is:" , sum)

def get_fact(numb):
    i = 2
    sum = 0
    prime_array = []
    while i < math.sqrt(numb):
        if (numb%i == 0 ):
            p_numb=is_prime(i)
            if p_numb != None:
                prime_array.append(p_numb)
        i=i+1
    return max(prime_array)

def is_prime(numb):
    i = 2
    is_prime = 1
    while i < numb:
        if (i != 1 and numb%i == 0):
            is_prime = 0
            next
        i = i +1

    if is_prime :
        return numb

if __name__== "__main__":
    main()