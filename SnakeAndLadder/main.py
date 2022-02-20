# Imports:
import random

ladder = {
    20: 30,
    46: 65,
    8: 25,
    74: 92
}

snake ={
    94: 9,
    78: 54,
    32: 22,
    63: 43
}


WIN_POSITION = 100


def _snake(prevpos):
    newpos = snake.get(prevpos)
    if newpos:
        return newpos
    return prevpos


def _ladder(prevpos):
    newpos = ladder.get(prevpos)
    if newpos:
        return newpos
    return prevpos


def win(finalpos):
    if finalpos == WIN_POSITION:
        return -1
    return 0


def diceRoll():
    dice = random.randint(0, 6)
    return dice


def play(player):
    '''

    :param player:Current position of player .
    :return: player:Next position of player after rolling Dice.
    '''
    while player <= 100:
        dice = diceRoll()
        if (player + dice) > 100:
            player += 0
        else:
            player += dice
            templadder = _ladder(player)
            if templadder > player:
                player = templadder
                return player
            else:
                tempsnake = _snake(player)
                player = tempsnake
                return player


# Starting position of both Players:
player1 = 0
player2 = 0
while True:
    option = int(input("Enter value:\n1.Roll Dice\n2.Exit Game\n"))
    if option == 1:
        play1 = play(player1)
        play2 = play(player2)

        if win(play1) == -1:
            print(f"1st Player Wins The Game!!!")
            break
        if win(play2) == -1:
            print("2nd Player Wins The Game!!!")
            break
        print(f"Player 1 Position --> {play1}\nPlayer 2 Position --> {play2}")
        player1 = play1
        player2 = play2
    elif option == 2:
        break
    else:
        print("Please enter right value")