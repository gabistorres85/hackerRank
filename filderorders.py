k = 40
order = [20,10,30]  
n = len(order)
result = 0
total = 0
for i in range(n):
    total += min(order)
    if total <= k: 
        result += 1
        print(total,order,result)
    order.remove(min(order))
    print (order)
print(result)