# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + … + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + … + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 – 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import sys

def main():
    #numb=int(sys.argv[1])
    numb=100
    diff=get_diff(numb)
    print("Difference is",diff)

def get_diff(n):
    i = 1
    sum_sq = 0
    sq_ind = 0
    for i in range(i,n+1):
        sum_sq = sum_sq + (i*i)
        sq_ind = sq_ind + i

    sq_sum=sq_ind*sq_ind

    return sq_sum-sum_sq


if __name__== "__main__":
    main()
