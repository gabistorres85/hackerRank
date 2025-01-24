# Calculate the minimum pages to turn in a book to reach a target page
n = 95073 # total pages of the book 1 |2 3| 4 5| 6 7 
p = 17440 # page number to turn to 
med = n//2 # 2  
way = 0
if p <= med:
    if p %2 == 0:
        p+=1
    way = p //2
if p > med:
    if p % 2 != 0:
        p -= 1
    way = (n - p)//2
print(way)