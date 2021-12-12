from useful import convertToVar
from re import L, sub

def checkRow(board):
    result = False
    for x in range(len(board)):
        #print(board[x])
        if all(ele == board[x][0] for ele in board[x]):
            result = True
            return result
    return result

def checkCol(board):
    result = False
    for y in range(5):
        col = []
        for x in range(5):
            col.append(board[x][y])
        if all(ele == col[0] for ele in col):
            result = True
            return result
    return result

def checkBingo(board):
    bingo = False
    if checkRow(board) or checkCol(board):
        bingo = True
    return bingo            

wholeBing = convertToVar('day04Input.txt', '\n\n')
nums = wholeBing[0].split(',')
boards = wholeBing[1:]
hek = 0
for i in range(len(boards)):
    b = boards[i]
    boards[i] = b.split('\n')
    for j in range(len(boards[i])):
        boards[i][j] = boards[i][j].lstrip()
        boards[i][j] = sub(' +', ' ', boards[i][j])
        boards[i][j] = boards[i][j].split(' ')
        #print(boards[i][j])
filtered = boards
filtered2 = boards
print(filtered)


bingoBoard = None

for n in nums:
    if bingoBoard != None:
        break
    hek = int(n)
    for i in range(len(filtered)):
        for j in range(len(filtered[i])):
            for k in range(len(filtered[i][j])):
                if filtered[i][j][k] == n:
                    filtered[i][j][k] = "cock"
                    #print(boards[i][j][k], n)
        if checkBingo(filtered[i]):
            bingoBoard = filtered[i]
            break

summyWummy = 0
for i in range(len(bingoBoard)):
    for j in range(len(bingoBoard[i])):
        if bingoBoard[i][j] != 'cock':
            #print(bingoBoard[i][j])
            summyWummy += int(bingoBoard[i][j])
            #print(summyWummy)
#print(summyWummy * hek)

bingoBoards = []

for n in nums:
    if len(bingoBoards) == len(filtered2):
        break
    print()
    hek = int(n)
    for i in range(len(filtered2)):
        if filtered2[i] in bingoBoards:
            continue
        for j in range(len(filtered2[i])):
            for k in range(len(filtered2[i][j])):
                if filtered2[i][j][k] == n:
                    filtered2[i][j][k] = "cock"
                    #print(boards[i][j][k], n)
        if checkBingo(filtered2[i]):
            bingoBoards.append(filtered2[i])
            

summyWummy = 0
for i in range(len(bingoBoards[-1])):
    for j in range(len(bingoBoards[-1][i])):
        if bingoBoards[-1][i][j] != 'cock':
            #print(bingoBoards[-1][i][j])
            summyWummy += int(bingoBoards[-1][i][j])
            #print(summyWummy)
print(summyWummy, hek)
print(summyWummy * hek)