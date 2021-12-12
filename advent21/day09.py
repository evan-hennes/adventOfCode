from useful import convertToVar
from math import prod

mtrx = convertToVar('day09Input.txt', '\n')

def getAdjacent(matrix, i, j):
    adjacentPoints = []
    if j == 0:
        if i == 0:
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i + 1][j], (i + 1, j))]
        elif i == (len(matrix) - 1):
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i - 1][j], (i - 1, j))]
        else:
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i - 1][j], (i - 1, j)), (matrix[i + 1][j], (i + 1, j))]
    elif j == (len(matrix[i]) - 1):
        if i == 0:
            adjacentPoints = [(matrix[i][j - 1], (i, j - 1)), (matrix[i + 1][j], (i + 1, j))]
        elif i == (len(matrix) - 1):
            adjacentPoints = [(matrix[i][j - 1], (i, j - 1)), (matrix[i - 1][j], (i - 1, j))]
        else:
            adjacentPoints = [(matrix[i][j - 1], (i, j - 1)), (matrix[i - 1][j], (i - 1, j)), (matrix[i + 1][j], (i + 1, j))]
    else:
        if i == 0:
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i][j - 1], (i, j - 1)), (matrix[i + 1][j], (i + 1, j))]
        elif i == (len(matrix) - 1):
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i][j - 1], (i, j - 1)), (matrix[i - 1][j], (i - 1, j))]
        else:
            adjacentPoints = [(matrix[i][j + 1], (i, j + 1)), (matrix[i][j - 1], (i, j - 1)), (matrix[i - 1][j], (i - 1, j)), (matrix[i + 1][j], (i + 1, j))]
    return adjacentPoints

def getBasin(matrix, current, pts):
    adjPts = getAdjacent(matrix, current[1][0], current[1][1])
    currentHght = current[0]
    for adj in adjPts:
        p = adj[0]
        loc = adj[1]
        if p == 9:
            continue
        elif p > currentHght:
            if loc not in pts:
                pts.add(loc)
                getBasin(matrix, pt, pts)


for i in range(len(mtrx)):
    mtrx[i] = list(mtrx[i])
    for j in range(len(mtrx[i])):
        mtrx[i][j] = int(mtrx[i][j])

lowPointRiskLevels = []
for i in range(len(mtrx)):
    mtrx[i] = list(mtrx[i])
    for j in range(len(mtrx[i])):
        mtrx[i][j] = int(mtrx[i][j])
        current = mtrx[i][j]
        adjacent = getAdjacent(mtrx, i, j)
        adjacent = [p[0] for p in adjacent]
        isLower = []
        for pt in adjacent:
            if current < pt:
                isLower.append(True)
            else:
                isLower.append(False)
        if all(isLower):
            risk = 1 + current
            lowPointRiskLevels.append([risk, (i, j)])
print(lowPointRiskLevels)

basins = []
lowPoints = [point[1] for point in lowPointRiskLevels]
for point in lowPoints:
    i = point[0]
    j = point[1]
    current = (mtrx[i][j], (i, j))
    adjacent = getAdjacent(mtrx, i, j)
    points = set([current[1]])
    getBasin(mtrx, current, points)
    basins.append(len(points))
    
sortedBasins = sorted(basins, reverse = True)
largest = sortedBasins[:3]
print(prod(largest))