'''Two players are playing a game of Tower Breakers! Player  always moves first, 
and both players always play optimally.The rules of the game are as follows:

Initially there are n towers.
Each tower is of height m.
The players move in alternating turns.
In each turn, a player can choose a tower of height x and reduce its height to y, 
where 1<= y < x and y evenly divides x .
If the current player is unable to make a move, they lose the game.
Given the values of n and m, determine which player will win.
 If the first player wins, return . Otherwise, return .'''
n =374625                # towers
m = 796723 # height of towers
choice = 0 
round = 1
# First m divisors numbers
multiples = [i for i in range(1,m) if m%i == 0]
while len(multiples)>1:
    multiples = [i for i in range(1,m) if m%i == 0]
    #The best choice
    choice = max(multiples)
    m = m - choice
    round += 1
print(n)
print(round)
#Always players do the best choice, so repeat for n times.
round =round * n
print(round)
if round%2 ==0:
    print(2)
else:
    print(1)



