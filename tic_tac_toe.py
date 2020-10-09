# Tic Tac Toe Game with Computer
#           X | X | x
#           +-+-+-+-+
#           X | X | x
#           +-+-+-+-+
#           X | X | x

# import modules
import random
from time import sleep

human = ''
computer = ''
result = False
steps_count = 0
game_list = []
TicTacToe = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

print("Tic Tac Toe is a game of 2 player as well as it contains 2 alphabets: X | O")
def chooseplayer():
    global human, computer
    print("choose X | O")
    human = input("Human Alphbet: ").upper()
    if human == 'X' or human == 'O':
        if human == 'X':
            computer = 'O'
            print("Computer  Alphbet:", computer)
        else:
            computer = 'X'
            print("Computer Alphbet:", computer)
    else:
        print('Invalid Alphabet, please select X | O\n')
        chooseplayer()



def placeIndex():
    # print(human, ':',computer, '\n')
    print(''' Tic Tac Toe Index place
        1  2  3
        4  5  6
        7  8  9
            ''')



def auto_generated_number():
    global steps_count
    number = random.randint(1,9)
    if number in game_list:
        print('computer place: ',number)
        steps_count += 1
        print('Total Move: ', steps_count)
        game_list.remove(number)
        fill_TicTacToe(number, computer)
        return number
    else:
        auto_generated_number()



def human_selected_number():
    global steps_count
    number = int(input("your place: "))
    number_list = [1,2,3,4,5,6,7,8,9]
    if number in number_list:
        if number in game_list:
            steps_count += 1
            print('Total Move: ', steps_count)
            game_list.remove(number)
            fill_TicTacToe(number, human)
            return number
        else:
            print('Place is already taken, please choose again!')
            human_selected_number()
    else:
        print('Number out of range, please select number between 1-9')
        human_selected_number()



def fill_TicTacToe(place, alphabet):
    if place == 1:
        TicTacToe[0][0] = alphabet
    elif place == 2:
        TicTacToe[0][1] = alphabet
    elif place == 3:
        TicTacToe[0][2] = alphabet
    elif place == 4:
        TicTacToe[1][0] = alphabet
    elif place == 5:
        TicTacToe[1][1] = alphabet
    elif place == 6:
        TicTacToe[1][2] = alphabet
    elif place == 7:
        TicTacToe[2][0] = alphabet
    elif place == 8:
        TicTacToe[2][1] = alphabet
    elif place == 9:
        TicTacToe[2][2] = alphabet
    else:
        pass



def show_TicTacToe():
    # h -> human and c -> computer
    global game_list, TicTacToe, steps_count, result
    steps_count = 0
    TicTacToe = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
    game_list = [1,2,3,4,5,6,7,8,9]
    placeIndex()
    while steps_count < 9 or result == False:
        if steps_count < 9:
            human_selected_number()
            TicTacToe_progressBar()
            if winner('Human', human):
                print('Human Won')
                break
        if steps_count < 9:
            sleep(1)
            auto_generated_number()
            TicTacToe_progressBar()
            if winner('Computer', computer):
                print('Computer Won')
                break
        if steps_count == 9:
            print("Match Draw!")
            break



def TicTacToe_progressBar():
    row_count = 0
    for r in TicTacToe:
        col_count = 0
        for c in r:
            if col_count != 2:
                print(c , end = " | ")
                col_count += 1
            else:
                row_count += 1
                print(c)
        if row_count != 3:
            print('+-+-+-+-+')



def winner(player, alphabet):
    # Col Check
    if TicTacToe[0][0] == alphabet and TicTacToe[0][1] == alphabet and TicTacToe[0][2] == alphabet:
        return True
    elif TicTacToe[1][0] == alphabet and TicTacToe[1][1] == alphabet and TicTacToe[1][2] == alphabet:
        return True
    elif TicTacToe[2][0] == alphabet and TicTacToe[2][1] == alphabet and TicTacToe[2][2] == alphabet:
        return True
    # Row Check
    elif TicTacToe[0][0] == alphabet and TicTacToe[1][0] == alphabet and TicTacToe[2][0] == alphabet:
        return True
    elif TicTacToe[0][1] == alphabet and TicTacToe[1][1] == alphabet and TicTacToe[2][1] == alphabet:
        return True
    elif TicTacToe[0][2] == alphabet and TicTacToe[1][2] == alphabet and TicTacToe[2][2] == alphabet:
        return True
    # Digonal Check
    elif TicTacToe[0][0] == alphabet and TicTacToe[1][1] == alphabet and TicTacToe[2][2] == alphabet:
        return True
    elif TicTacToe[2][0] == alphabet and TicTacToe[2][1] == alphabet and TicTacToe[0][2] == alphabet:
        return True
    else:
        return False



def run():
    chooseplayer()
    print('\n')
    show_TicTacToe()
    print('\n')



run()