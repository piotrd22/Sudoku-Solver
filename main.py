
# -1 is false and 0 is true !

sudoku = [['*',3,'*','*',8,'*','*','*',1],
          ['*','*',7,4,'*',1,'*',5,'*'],
          [9,'*','*','*',5,'*',2,'*','*'],
          ['*','*',2,'*','*',5,'*',1,'*'],
          [3,'*','*',2,1,'*',5,'*','*'],
          [5,9,'*','*',6,'*','*','*',2],
          ['*','*',6,5,'*',2,'*','*','*'],
          ['*','*',9,6,'*','*','*',2,7],
          ['*','*','*','*','*',8,'*',6,5]]

def sudoku_solving(sudoku):

    find = empty(sudoku)
    if find == 0:
        return 0
    else:
        row, column = find

    for i in range(1,10):
        if actual(sudoku, i, (row,column)) == 0:
            sudoku[row][column] = i

            #Recursion -- this will call our func sudoku_solving to a momemnt when find ==0 or when our loop will end and we don't have any number that works -- then we backtrack and make our number a '*'
            if sudoku_solving(sudoku) == 0:
                return 0
            else:
                sudoku[row][column] = '*'

    return -1

def actual(sudoku, number, position):

    #Position is going to be a tuple from def empty so position[0] means i, means row,j means column

    for i in range(len(sudoku)):
        if sudoku[position[0]][i] == number and position[1] != i:
            return -1

    for j in range(len(sudoku)):
        if sudoku[j][position[1]] == number and position[0] != j:
            return -1

    square_x = position[1] // 3
    square_y = position[0] // 3

    #Multiply by 3 to be in the right square of the sudoku (index), because square_x and y gonna give us 0,1,2 index, but ot get to index 6 we have to multiply 2 * 3 and we have 6 index (where square of index 2 is gonna start, pretty cool)
    for x in range(square_y * 3, square_y * 3 + 3):
        for y in range(square_x * 3, square_x * 3 + 3):
            if sudoku[x][y] == number and (x,y) != x:
                return -1

    return 0

def draw_sudoku(sudoku):

    for i in range(len(sudoku)):
        if i % 3 == 0:
            print('-------------------------------')
        for j in range(len(sudoku[0])):
            if j % 3 == 0:
                print('| ', end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(sudoku[i][j],' ',end='')
    print('-------------------------------')
    return ''

def empty(sudoku):

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == '*':
                return (i,j)   #i is row and j is column
    return 0

print('Sudoku')
print(draw_sudoku(sudoku))
print('Sudoku solving.........')
sudoku_solving(sudoku)
print('This is it!')
print('\n')
print(draw_sudoku(sudoku))
