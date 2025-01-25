'''Given a square grid of characters in the range ascii[a-z], 
rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. 
Return YES if they are or NO if they are not.'''
grid = ['mpxz','abcd','wlmf']
for i in range(len(grid)):
    grid[i]= list(grid[i])
    grid[i] = sorted(grid[i])
yes=0
no =0
minChar = "z"
for j in range(len(grid[0])):
    for i in range(len(grid)-1):
        if grid[i][j]>grid[i+1][j]:
                isOdered = False
                break
    if not isOdered:
         break
             
         
if isOdered:
    print("YES")
else:
    print("NO")