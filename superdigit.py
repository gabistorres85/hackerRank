'''We define super digit of an integer x using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is .
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.'''



def superDigit(n,k):
    digitaSum = sum([int(i) for i in str(n)]) * k
    while digitaSum >= 10:
        digitaSum = sum([int(i) for i in str(digitaSum)])
    return digitaSum


print(superDigit(9875,2))
