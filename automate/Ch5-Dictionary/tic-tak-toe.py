theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
            'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

printBoard(theBoard)


# game start
startBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
              'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
turn = 'O'
for i in range(9):
    printBoard(startBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    startBoard[move] = turn
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'
printBoard(startBoard)
