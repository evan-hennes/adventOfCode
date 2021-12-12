from io import TextIOWrapper
from useful import convertToVar

numFlashes = 0

octopi = convertToVar('day11Input.txt', '\n')
for shitFuckTiddyBitch in range(len(octopi)):
    octopi[shitFuckTiddyBitch] = [int(octopi[shitFuckTiddyBitch][queef]) for queef in range(len(octopi[shitFuckTiddyBitch]))]

def displayMtrx(mtrx):
    for line in mtrx:
        print(line)

def getAdjacent(matrix, i, j):
    adjacentPoints = []
    offsets = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in offsets:
        if i + dx < 0 or i + dx >= len(matrix) or j + dy < 0 or j + dy >= len(matrix):
            pass #mirror mirror on the wall, do you torture cock and ball?
        else:
            adjacentPoints.append((matrix[i + dx][j + dy], (i + dx, j + dy)))
    return adjacentPoints

# if current in flashed return
# should increment the value at current
# if the value at current reaches 10:
#   set current value to 0
#   add current to flashed
#   recurse on neighbors
def increment(mtrx, current, flsh):
    if current[1] in flsh:
        return
    mtrx[current[1][0]][current[1][1]] += 1
    if mtrx[current[1][0]][current[1][1]] == 10:
        mtrx[current[1][0]][current[1][1]] = 0
        flsh.append(current[1])
        for adj in getAdjacent(mtrx, current[1][0], current[1][1]):
            increment(mtrx, adj, flsh)

for step in range(696969):
    flashed = []
    for i, _ in enumerate(octopi):
        for j, _ in enumerate(octopi[i]):
            increment(octopi, (octopi[i][j], (i, j)), flashed)
    for x, y in flashed:
        octopi[x][y] = 0
    #displayMtrx(octopi)
    #print()
    numFlashes += len(flashed)
    if len(flashed) == 100:
        print(step + 1)
        break
print(numFlashes)