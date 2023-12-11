""" A version of the popular Battleships game
    One person places ships in a grid
    The other tries to guess or figure out the positions of the ships

    It is a text based version using no external packages and modules
    A focus of this activity is the use of Exceptions
    There are built in exceptions for where there is a runtime error
    e.g. you put the wrong type of value, the index of a list is out of range.
    You can also add your own exceptions 
    In this one it is when you try to place two ships in the same place
    
    Like the game from the previous activity it uses Unicode characters"""

from copy import deepcopy
    
#global constants
BOARD_SIZE=10
SHIP_SYMBOL="\U0001F6A2"
BOMB_SYMBOL="\U0001F4A3"
BLANK_SYMBOL="\u26AA"
SHIP_START="\u2693"
MISS_SYMBOL ="\u274C"


class Already_There(Exception):
     def __init__(self):
         print('There is already a ship there! Try Again')

print("*************** Battleships ***************")

ans = input("do you want instructions? Yes or No? ")

if ans.lower().strip() in ("y", "yes"):
    print("Battleships is a two player game")
    print("Player 1 will place the ships")
    print("Give numbers for the row and then column where you want the ship to be")
    print(SHIP_START + " marks where the ship starts")
    print("Then give the direction you want the ship to go")
    print(SHIP_SYMBOL +" marks where a previous battleship is")
    print("You can not place a ship where another one is")
    print("Nor can you go past the border of the grid")
    print("Make sure player 2 does not see where you place the ships!")
    print("When finished it will print blank lines to hide the grid")
    input("Press enter to continue and see player 2 instructions")
    print("\n\nPlayer 2 will be the bomber of the fleet")
    print("To win the game P2 must bomb every square where there is a ship")
    print("As with player 1 give numbers for the row and column you want")
    print("This will drop a bomb at that position")
    print("It will show if it was a hit or a miss")
    print(MISS_SYMBOL + " is a miss while " + BOMB_SYMBOL + " is a successful hit")
    print("The game continues until all ships are hit")
    print("It should give the number of bombs used to destroy the fleet")
    print("Try playing again swapping roles")
    print("Who can do it with the fewest bombs dropped?")

def print2D (Array2D):
    #print top row of numbers starting with blanks
    print("  ", end=" ")
    for i in range(len(Array2D)):
        print(i,end="  ")
    print("") #empty line
    for i in range(len(Array2D)):
        print(i,end=" ") #guide number at start of row
        for j in range(len(Array2D[i])):
            print(Array2D[i][j],end=" ")
        print("")
    print("")


def addShip(board, shipSize, row, col):
    direction=input("should it point up, down, left or right?")
    if direction not in ("up","down","left","right"):
        print("please write up down left or right") 
    else:
        for i in range(shipSize):
            if board[row][col]==SHIP_SYMBOL:
                raise Already_There()
            board[row][col]=SHIP_SYMBOL
            if i ==shipSize-1:
                return board
            if direction=="up":
                row-=1
            elif direction=="down":
                row+=1
            elif direction=="left":
                col-=1
            elif direction=="right":
                col+=1              
            if row<0 or col<0:
                raise IndexError
            #except IndexError:
            #    print("sorry but that would put it off the board")
            #    return


def shipStart(board, shipSize, type):
    #make a copy of the board in case of exception
    new_board=deepcopy(board)
    while True: #loop until we have returned a good value
        print2D(board)
        print("place a ", type, "of  size", shipSize)
        try:
            row=int(input("put the row number of the ships start "))
            col=int(input("put the col number of the ships start "))
            if board[row][col]== SHIP_SYMBOL:
                raise Already_There()
            new_board[row][col]=SHIP_START
            print2D(new_board)
            addShip(new_board, shipSize, row, col)
        except IndexError:
            print("can't do, the position must be between 0 and ", BOARD_SIZE)
            new_board=deepcopy(board)
        except ValueError:
            print("can't do, make sure you put in whole numbers")
            new_board=deepcopy(board)
        except Already_There:
            new_board=deepcopy(board)
        else:
            return new_board
        

board=[[BLANK_SYMBOL for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

ship_sizes={"carrier":5, "battleship":4, "cruiser":3, "submarine":3, "destroyer":2}

shipSquares=0
for ship in ship_sizes:
    board=shipStart(board, ship_sizes[ship], ship)
    shipSquares+=ship_sizes[ship]
    
hits=0
bombs=0
#clears screen and new lines stops bug of making new lines later
print("\n"*50, end=" ") 
bombBoard=[[BLANK_SYMBOL for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

while hits<shipSquares:
    print2D(bombBoard)
    bombs+=1
    try:
        row=int(input("what row to bomb? "))
        col=int(input("what column to bomb? "))
        if board[row][col]==SHIP_SYMBOL:
            print("you hit a ship!")
            hits+=1
            bombBoard[row][col]=BOMB_SYMBOL
        else:
            print("you missed it this time but try again")
            bombBoard[row][col]=MISS_SYMBOL
    except IndexError:
            print("can't do, the number must be between 0 and ", BOARD_SIZE)
    except ValueError:
            print("can't do make sure you put in whole numbers")

print("well done you did it with ", bombs, " bombs")

