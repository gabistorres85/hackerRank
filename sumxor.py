'''Given an integer n, find each x such that:
 <= x <=n
 n+x = n^x'''
def sumXor(n):
    n = bin(n)[2:]
    if n == '0':
        return 1
    elif n.count('0') == 0:
        return 1
    else:
        sum = 2**n.count('0')
    return sum

print(sumXor(0)) # 4