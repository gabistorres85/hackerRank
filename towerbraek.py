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

if m == 1:
    print(2)
if n%2 == 0:
    print(2)
else:
    print (1)