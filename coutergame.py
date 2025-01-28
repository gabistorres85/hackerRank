"""	Submissions	Leaderboard	Discussions	Editorial
Louise and Richard have developed a numbers game. They pick a number and check to see if it is 
a power of 2 . If it is, they divide it by 2
. If not, they reduce it by the next lower number which is a power of 2.
 Whoever reduces the number to 1 wins the game. Louise always starts.

Given an initial value, determine who wins the game."""

def counterGame(n):
   turns = 0  # Track number of turns
   if n == 1:
        return "Richard"
   
   while n != 1:
        # Verifica se n é uma potência de 2
        if (n & (n - 1)) == 0:
            n = n // 2  # Divide por 2 se for potência de 2
            turns += 1  # Incrementa o contador de turnos
        else:
            # Encontra a maior potência de 2 menor que n
            largest_power = 1 << (n.bit_length() - 1)
            n -= largest_power  # Subtrai a maior potência de 2
            print(n)
            turns += 1  # Incrementa o contador de turnos
   return "Richard" if turns % 2 == 0 else "Louise"


print(counterGame(1463674015))
  