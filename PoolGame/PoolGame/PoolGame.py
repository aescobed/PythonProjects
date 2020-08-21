
from collections import deque
import random
import os

def delete_nth(LL, n):
    LL.rotate(-n)
    res = LL.popleft()
    LL.rotate(n)
    return res

def clear_console():
    for i in range(100):
        print()


print("Enter number of players")

nPlayers = int(input())

while(nPlayers > 15):

    print("Number of players cannot exceed number of pool balls")

    print("Re-enter number of players")

    nPlayers = int(input())

print("Enter number of balls per player")

nBallsPerPlayer = int(input())

while(nBallsPerPlayer * nPlayers > 15):

    print("Balls given to players cannot exceed the number of pool balls")

    print("Re-enter number of balls per player")

    nBallsPerPlayer = int(input())

print("Press enter when the first player is holding the phone")

input()

clear_console()

list = deque()

for i in range(1, 16):
    list.append(i)

ballsRemaining = 15

for i in range(nPlayers):

    if nBallsPerPlayer>1:
        print("Your balls are:")

    else:
        print("Your ball is:")

    for x in range(nBallsPerPlayer):

        choice = random.randrange(ballsRemaining)

        choice = delete_nth(list, choice)

        ballsRemaining -= 1

        print(choice)

    print("Press enter and pass the phone to the next player once you memorized your balls")

    input()

    clear_console()

    print("Press enter once the next player has the phone")

    input()

    clear_console()




