import random

def main():
    Player1 = 0
    # player1wins = 0
    Player2 = 0
    # player2wins = 0
    rounds = 1
    # while rounds != 2: (This is for 2 player playing only one single round.) 
    while rounds != 7:
        print("Round " + str(rounds))
        Player1 = dice_roll()
        Player2 = dice_roll()
        print("player 1 Roll: " + str(Player1))
        print("player 2 Roll: " + str(Player2))

        if Player1 == Player2:
            print("Draw!\n")
        elif Player1 > Player2:
            print("Player 1 wins!\n")
        else:
            print("player 2 wins!\n")

        rounds = rounds + 1

    # if player1wins == player2wins: (This is for check overall result who wins in the last, so no cheating. LOL)
    #     print("Draw!\n")
    # elif player1wins > player2wins:
    #     print("player 1 wins - Rounds won: " + str(player1wins))
    # else:
    #      print("player 2 wins - Rounds won: " + str(player2wins))

def dice_roll():
    diceRoll = random.randint( 1 , 6 )
    return diceRoll

main()
