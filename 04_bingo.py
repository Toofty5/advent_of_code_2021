import numpy as np

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
for called_num in draw_nums:
    if win:
        break
    for i, check_board in enumerate(check_boards):
        check_boards[i] = np.where(check_board == called_num, -1, check_board)

        if winner(check_boards[i]):
            win = True

            print(i, called_num)
            print(boards[i])
            print(check_boards[i])
            zeroed = np.where(check_boards[i]==-1, 0, boards[i])
            print(zeroed, called_num)
            print(called_num * np.sum(zeroed))
            break



