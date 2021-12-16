from useful import convertToVar, getAdjacent
from math import inf
import heapq as heap

tile1 = convertToVar('day15Input.txt', '\n')
tile1 = [[int(rl) for rl in list(l)] for l in tile1]

def displayMtrx(mtrx):
    for line in mtrx:
        print(line)
#end def displayMtrx

def createTiles(tiles = [], currentIter = 1, maxIter = 8):
    tiles.append([[1 if l + 1 == 10 else l + 1 for l in line] for line in tiles[-1]])
    if currentIter == maxIter:
        return tiles
    else:
        iter = currentIter + 1
        return createTiles(tiles, iter, maxIter)
#end def createTiles

def createMatrix(mx):
    mtx = []
    for fuck in mx:
        for i in range(len(fuck[0])):
            line = [el[i] for el in fuck]
            joined = []
            for seg in line:
                joined += seg
            mtx.append(joined)
    return mtx
#end def createMatrix

tt = createTiles([tile1], currentIter = 1, maxIter = 8)

t0, t1, t2, t3, t4, t5, t6, t7, t8 = tt[0], tt[1], tt[2], tt[3], tt[4], tt[5], tt[6], tt[7], tt[8]
mtrx = [[t0,t1,t2,t3,t4], [t1,t2,t3,t4,t5], [t2,t3,t4,t5,t6], [t3,t4,t5,t6,t7], [t4,t5,t6,t7,t8]]

cave = createMatrix(mtrx)
#displayMtrx(cave)

def djikstras(source, graph):
    q = [source]
    distMap = {((i, j)):(inf if (i, j) != source else 0) for i in range(len(graph)) for j in range(len(graph[i]))}
    seen = set()
    while len(q) != 0:
        q.sort(key=lambda q : distMap[q])
        v = q.pop(0)
        seen.add(v)
        for a in getAdjacent(graph, v[0], v[1], False):
            if a[1] not in seen:
                if distMap[v] + a[0] < distMap[a[1]]:
                    seen.add(a[1])
                    q.append(a[1])
                    distMap[a[1]] = distMap[v] + a[0]
    return distMap
#end def djikstras

shortest = djikstras((0, 0), cave)
print(shortest)