import random
#Demonstration of understanding of basic flow control and some list usage

rps = ['rock','paper','scissors']

player1 = input("rock, paper or scissors; What's your move? ")

player2= random.choice(rps)

print(player2)
if player1 == player2:
    print("draw")
elif player1 == 'rock':
    if player2 == 'scissors':
        print("Player1 wins")
    elif player2 == 'paper':
        print("Player2 wins")
elif player1 == 'scissors':
    if player2 == 'rock':
        print("Player2 wins")
    elif player2 == 'paper':
        print("Player1 wins")
elif player1 == 'paper':
    if player2 == 'scissors':
        print("Player2 wins")
    elif player2 == 'rock':
        print("Player1 wins")
else:
	print("someone peeked")
