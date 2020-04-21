
####### FUNCTIONS -> ########
# Print the game board outline along w user pieces (X's and O's)
def print_live_gameboard(pieces):
    print("\t|\t|")
    print(" " + str(pieces[0]) + " \t| " + str(pieces[1]) + "\t|  " + str(pieces[2]))
    print("\t|\t|")
    print("--------------")
    print("\t|\t|")
    print(" " + str(pieces[3]) + " \t| " + str(pieces[4]) + "\t|  " + str(pieces[5]))
    print("\t|\t|")
    print("--------------")
    print("\t|\t|")
    print(" " + str(pieces[6]) + " \t| " + str(pieces[7]) + "\t|  " + str(pieces[8]))
    print("\t|\t|\n\n")


# Prints a sample gameboard to show users where they can enter their pieces
def print_sample_gameboard(pieces):
    print("\t|\t|")
    print(" " + str(pieces[0]) + " \t| " + str(pieces[1]) + "\t|  " + str(pieces[2]))
    print("\t|\t|")
    print("--------------")
    print("\t|\t|")
    print(" " + str(pieces[3]) + " \t| " + str(pieces[4]) + "\t|  " + str(pieces[5]))
    print("\t|\t|")
    print("--------------")
    print("\t|\t|")
    print(" " + str(pieces[6]) + " \t| " + str(pieces[7]) + "\t|  " + str(pieces[8]))
    print("\t|\t|\n\n")

# Verify the user entered a valid number between 1 & 9 (inclusive)
# This guarantees they will be playing on the game board
def validate_input(choice, gameBoard):

    if not "" in gameBoard: # Check to see if the game board is full before verifying the input
        print("Jeez! Looks like a stalemate... Cya!")
        exit()
    while True:
        print("\n\n")
        try:
            choice = int(choice)
            if choice < 0 or choice > 9: # See if the input is within the game board space
                print("Sorry! Your choice has to be a number between 1 and 9 inclusive. Please try again...")
                choice = input("Select a new position [1-9]: ")
            else:
                if gameBoard[choice - 1] == "X" or gameBoard[choice - 1] == "O": # Check if there is already a piece in this location
                    print("Ooo this spot is already taken")
                    choice = input("Select a new position [1-9]: ")
                else:
                    return choice
        except ValueError:
            print("Sorry! Your choice has to be a number between 1 and 9 inclusive. Please try again...")
            choice = input("Select a new position [1-9]: ")


def select_positions(gameBoard, u1_piece, u2_piece):
    winner = False
    while True:
        user1_choice = input("User 1! Select your move: ")  # Prompt user 1 to insert their first piece
        user1_choice = validate_input(user1_choice, gameBoard)

        gameBoard[user1_choice - 1] = u1_piece  # Assign the chosen value in the array
        print("\n"

              * 50)
        print_live_gameboard(gameBoard)

        if checkWinner(gameBoard, u1_piece): #Check to see if user 1 has won
            print("Congrats User 1! You won the game!\n\n")
            break

        user2_choice = input("User 2! Select your move: ") # Prompt user 2 to insert their first piece
        user2_choice = validate_input(user2_choice, gameBoard)

        gameBoard[user2_choice - 1] = u2_piece # Assign the chosen value in the array
        print("\n" * 50)
        print_live_gameboard(gameBoard)

        if checkWinner(gameBoard, u2_piece): # Check to see if user 2 has won
            print("Congrats User 2! You won the game!\n\n")
            break

def checkWinner(gameBoard, piece): # Verify if there is a winner

    if checkHorizontal(gameBoard,piece): # Check if the user wins horizontally
        return True
    elif checkVertical(gameBoard,piece): # Check if the user wins vertically
        return True
    elif checkDiagonal(gameBoard,piece): # Check if the user wins diagonally
        return True
    else: # The user did not win
        return False


def checkHorizontal(gameBoard,piece): # Checks each row of the game board to see if the user won
    winner = False
    if gameBoard[0] == piece and gameBoard[1] == piece and gameBoard[2] == piece:
        winner = True
        return winner
    elif gameBoard[3] == piece and gameBoard[4] == piece and gameBoard[5] == piece:
        winner = True
        return winner
    elif gameBoard[6] == piece and gameBoard[7] == piece and gameBoard[8] == piece:
        winner = True
        return winner
    else:
        return winner


def checkVertical(gameBoard,piece): # Checks each column of the game board to see if the user won
    winner = False
    if gameBoard[0] == piece and gameBoard[3] == piece and gameBoard[6] == piece:
        winner = True
        return winner
    elif gameBoard[1] == piece and gameBoard[4] == piece and gameBoard[7] == piece:
        winner = True
        return winner
    elif gameBoard[2] == piece and gameBoard[5] == piece and gameBoard[8] == piece:
        winner = True
        return winner
    else:
        return winner


def checkDiagonal(gameBoard,piece): # Checks both diagonal ways to win
    winner = False
    if gameBoard[0] == piece and gameBoard[4] == piece and gameBoard[8] == piece:
        winner = True
        return winner
    elif gameBoard[2] == piece and gameBoard[4] == piece and gameBoard[6] == piece:
        winner = True
        return winner
    else:
        return winner

####### FUNCTIONS -| ########

####### Variables -> #########

SampleGamePieces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Game pieces to show the user where pieces can be inserted
LiveGamePieces = ["", "", "", "", "", "", "", "", ""] # Game board with no values. This array holds the actual pieces the user will use to win
user1_piece = "" # Game piece User 1 selects to use
user2_piece = "" # Game piece User 2 uses
continue_play = True
choice = "" # Allows the user to keep playing the game after it has concluded

####### Variables -| #########

######### Main() -> ###########

while continue_play == True:
    print("Welcome to Tic Tac Toe!\n------------------------\n\n")  # Introduction game heading
    user1_piece = input("Hello User 1! Will you be X's or O's? [Enter x|X or o|O]: ").upper()
    print("\n")

    # If user 1 selects X, user 2 is 0 & vice versa
    while True:
        if user1_piece == "X":
            user2_piece = "O"
            break
        elif user1_piece == "O":
            user2_piece = "X"
            break
        else:
            print("Oops! Whatever you entered is not valid..")
            user1_piece = input("Will you be X's or O's? [Enter x|X or o|O]]: ").upper()

    # Show the user where they can insert game pieces
    print("\n\nHere is where you can insert your game pieces!\n")
    print_sample_gameboard(SampleGamePieces)

    select_positions(LiveGamePieces, user1_piece, user2_piece)

    choice = input("Would you like to play again? [y|Y or n|N]: ").upper()
    while True:
        if choice == "Y":
            break
        if choice == "N":
            print("Great game! Cya later!\n\n")
            continue_play = False
            break
        else:
            print("Oops! Whatever you entered is not valid..\n\n")
            choice = input("Would you like to play again? [y|Y or n|N]: ").upper()

######### Main() -| ###########

