from useful import convertToVar, getAdjacent
from collections import defaultdict

tile1 = convertToVar('test.txt', '\n')
tile1 = [[int(rl) for rl in list(l)] for l in tile1]

def displayMtrx(mtrx):
    for line in mtrx:
        print(line)

def createTiles(tiles = [], currentIter = 1, maxIter = 8):
    #print(currentIter)
    tileX = []
    curr = tiles[-1]
    for line in curr:
        #print(line)
        total = []
        for l in line:
            if l + 1 == 10:
                total.append(1)
            else:
                total.append(l + 1)
        tileX.append(total)
    tiles.append(tileX)
    if currentIter == maxIter:
        return tiles
    else:
        iter = currentIter + 1
        return createTiles(tiles, iter, maxIter)

def createMatrix(mx):
    mtx = []
    for fuck in mx:
        #print(fuck)
        for i in range(len(fuck[0])):
            line = [el[i] for el in fuck]
            joined = []
            for seg in line:
                joined += seg
            mtx.append(joined)
    return mtx

ts = [tile1]
tt = createTiles(ts, currentIter = 1, maxIter = 9)
#print(tt)
t0, t1, t2, t3, t4, t5, t6, t7, t8 = tt[0], tt[1], tt[2], tt[3], tt[4], tt[5], tt[6], tt[7], tt[8]
mtrx = [[t0,t1,t2,t3,t4], [t1,t2,t3,t4,t5], [t2,t3,t4,t5,t6], [t3,t4,t5,t6,t7], [t4,t5,t6,t7,t8]]
#print(mtrx)
cave = createMatrix(mtrx)

def djikstras(start, end, graph):
    visited = defaultdict(bool)
    for i in range(len(graph)):
        for j in range(len(graph)):
            loc = (i, j)
            visited[loc] = False