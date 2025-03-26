import random

def print_visible():
    print('  A B C D E F G H I ')
    for index2, r in enumerate(visible):
        for index, i in enumerate(r):
            if index == 0:
                print(str(index2+1) + ' ' + i + ' ', end='')
            elif index == 8:
                print(i + ' ' + str(index2+1), end='')
            else:
                print(i + ' ', end='')
        print(' ')
    print('  A B C D E F G H I ')

def show_empty(board, x, y):
    if board[y][x] == '0':
        board[y][x] = ' '
        visible[y][x] = ' '
        for y1 in range(y-1, y+2):
            for x1 in range(x-1, x+2):
                if y1 == y and x1 == x:
                    pass
                elif x1 < 0 or y1 < 0 or x1 >= len(board[0]) or y1 >= len(board):
                    pass
                else:
                    show_empty(board, x1, y1)
    elif board[y][x] != ' ':
        visible[y][x] = board[y][x]

def check_win():
    for index2, r in enumerate(hidden):
        for index, i in enumerate(r):
            if i != 'X' and (visible[index2][index] == '?' or visible[index2][index] == 'F'):
                return False

    return True

def print_hidden():
    print('  A B C D E F G H I ')
    for index2, r in enumerate(hidden):
        for index, i in enumerate(r):
            if index == 0:
                print(str(index2+1) + ' ' + i + ' ', end='')
            elif index == 8:
                print(i + ' ' + str(index2+1), end='')
            else:
                print(i + ' ', end='')
        print(' ')
    print('  A B C D E F G H I ')

hidden = [[0]*9 for i in range(9)]

visible = [['?']*9 for i in range(9)]

mines = 0
while mines < 10:
    x = random.randint(0,8)
    y = random.randint(0,8)
    if hidden[x][y] != 'X':
        hidden[x][y] = 'X'
        mines += 1

for r in range(len(hidden)):
    for c in range(len(hidden[0])):
        if hidden[r][c] == 'X':
            continue
        bomb = 0
        for y in range(r-1, r+2):
            for x in range(c-1, c+2):
                if y == r and x == c:
                    pass
                elif x < 0 or y < 0 or x >= len(hidden[0]) or y >= len(hidden):
                    pass
                elif hidden[y][x] == 'X':
                    bomb += 1
        hidden[r][c] = str(bomb)

print_visible()

while True:
    cell = input('\nChoose a cell: \n')
    x = ord(cell[0]) - 65
    y = int(cell[1]) -1
    if len(cell) == 4:
        visible[y][x] = 'F'
    else:
        if hidden[y][x].isdigit() and hidden[y][x] != '0':
            visible[y][x] = hidden[y][x]
        elif hidden[y][x] == 'X':
            for r in range(len(hidden)):
                for c in range(len(hidden[0])):
                    if hidden[r][c] == 'X':
                        visible[r][c] = 'X'
            print_visible()
            print('\nYou lost!\n')
            break
        else:
            show_empty(hidden, x, y)

    if check_win() == True:
        print_hidden()
        print('\nCongratulations! You won!\n')
        break
    
    print_visible()
    