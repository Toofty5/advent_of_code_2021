import numpy as np
import pdb

blocks = [block.strip() for block in open("input","r").read().split("\n\n")]
draw_nums = [int(num) for num in blocks[0].split(",")]
boards = [np.reshape( [int(num) for num in board.split()],(5,5)) for board in blocks[1:]]
check_boards = boards.copy()

def winner(board):
    for i in range(5):
        if (    sum(board[i,:]) == -5 or
                sum(board[:,i]) == -5 ):
            return True
    return False

win = False

remaining = list(range(len(check_boards)))

for called_num in draw_nums:
    for i in range(len(check_boards)):

        check_boards[i] = np.where(check_boards[i] == called_num, -1, check_boards[i])

        if winner(check_boards[i]):
            if i == 15:
                print("LAST WINNER")
                zeroed = np.where(check_boards[i] == -1, 0, check_boards[i])
                print(zeroed)
                print(called_num, np.sum(zeroed))
                print( f"Answer {called_num * np.sum(zeroed)}")
                


            if len(remaining) == 1:
                print(remaining)
                print(check_boards[remaining[0]])

            if i in remaining:
                remaining.remove(i)
            
