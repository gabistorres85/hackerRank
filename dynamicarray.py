'''Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
Declare an integer, lastAnswer, and initialize it to 0.
There are 2 types of queries, given as an array of strings for you to parse:
Query: 1 x y
Let idx = ((x ⊕ lastAnswer) % n).
Append the integer y to arr[idx].
Query: 2 x y
Let idx = ((x ⊕ lastAnswer) % n).
Assign the value arr[idx][y % size(arr[idx])] to lastAnswer.
Store the new value of lastAnswer to an answers array.
Note: ⊕ is the bitwise XOR operation, which corresponds to the ^ operator
in most languages. Learn more about it on Wikipedia. % is the modulo operator.

Finally, size(arr[idx]) is the number of elements in arr[idx].

'''


n=2
queries=[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
# Creating arr.
arr=[ []*n for row in range(n)]
lastAnswer = 0
answer = []
#Trating querie1

for i in range(len(queries)):
    x = queries[i][1]
    y=queries[i][2]
    idx = (x ^ lastAnswer) % n
    if queries[i][0] == 1: #choosen querie 1 
        arr[idx].append(y)
    else: # choosen querie 2
        lastAnswer =arr[idx][y % len(arr[idx])]
        answer.append(lastAnswer)


print(answer)
