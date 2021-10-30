#Assignment 5
import time
import random
from termcolor import colored

game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
def showGameBoard():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()

def choiceAutonomePlayar():
    choice = int(input("Do you like to play with the computer or are you two? Enter 1 if you are one and 2 if you are two: "))
    if(choice == 1):
        while True:
            onePlayer()
            showGameBoard()
            check(game) 
    elif(choice == 2):
        while True:
            twoPlayers()
            showGameBoard()
            check(game) 
    else:
        print("The number entered is incorrect")

def onePlayer():
    x = 1
    print("The computer is playing... ")
    row = random.randrange(0,3,1)
    col = random.randrange(0,3,1)
    if 0<= row <=2 and 0<= col <=2:
        while game[row][col] == '-':
            game[row][col] = 'O'
            showGameBoard()
            break
        play(x)

def twoPlayers():
    x = int(input("how is your number? 1 or 2? "))
    if(x == 1):
        play(x)
    elif(x == 2):
        play(x)

def play(x):
    print("player "+str(x))
    while True:
        row = int(input("please input the number of row: "))
        col = int(input("please input the number of column: "))
        if 0<= row <=2 and 0<= col <=2:
            if game[row][col] == '-':
                if(x == 1):
                    game[row][col] = colored('X', "red")
                    break
                else:
                    game[row][col] = colored("O","blue")
                    break
            else:
                print("cell is not empty!")
        else:
            print("Index out of range please try again, Enter number between 1-3: ")
                     
def check(game, x):
    for i in range(3):
            if check_row(game, i):
                print("player "+ str(x) + "won")
            if check_column(game, i):
                print("player "+ str(x) + "won")
            if check_diagonals(game):
                print("player "+ str(x) + "won")
            return False

def check_row(game, row):
    return (game[row][0] == game[row][1] and game[row][1] == game[row][2] and game[row][0] != " ")

def check_column(game, col):
    return (game[0][col] == game[1][col] and game[1][col] == game[2][col] and game[0][col] != " ")

def check_diagonals(game):
    return (game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] != " ") or\
            (game[2][0] == game[1][1] and game[1][1] == game[0][2] and game[2][0] != " ")



showGameBoard()
while True:
    choiceAutonomePlayar()
    check(game)
    start_time= time.time()    