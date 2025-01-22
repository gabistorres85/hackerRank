ar = [10, 20, 20, 10, 10, 30, 50, 10,30, 20]      
n = 9 
colorsSocket = []
pair =[]
result = 0
for i in ar:
    if colorsSocket.count(i) == 0:
        colorsSocket.append(i)
for i in colorsSocket:
    pair.append(ar.count(i))
for i in pair:
    result = i//2 + result
    print(i, result)
    


