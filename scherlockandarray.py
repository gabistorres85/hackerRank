'''Watson gives Sherlock an array of integers. His challenge is to find
 an element of the array such that the sum of all elements 
to the left is equal to the sum of all elements to the right.'''
def balancedSums(arr):
    totalSum = sum(arr)
    leftSum = 0
    for i in range(len(arr)):
        totalSum -= arr[i]
        if leftSum == totalSum:
            return "YES"
        leftSum += arr[i]
    
    return "NO"

print(balancedSums([2,0,0,0])) 