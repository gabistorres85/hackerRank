'''you will be given a list of integers,ARR , and a single integer k.
 You must create an array of length k from elements of Arr such that its unfairness is minimized. 
 Call that array arr' . Unfairness of an array is calculated as
 mar(arr')-min(arr')

Where:
- max denotes the largest integer in  arr'
- min denotes the smallest integer in arr' '''
arr =[1,2,1,2,1]
arr.sort()

k=3
unfairnessMin = max(arr)-min(arr)
for i in range(len(arr)-k+1):
        unfairness = arr[i+k-1] - arr[i]
        if unfairness ==0:
            unfairnessMin = unfairness
        elif unfairness < unfairnessMin:
            unfairnessMin = unfairness
print(unfairnessMin)    