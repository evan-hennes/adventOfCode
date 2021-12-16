from useful import convertToVar, getAdjacent
from math import inf

tile1 = convertToVar('test.txt', '\n')
tile1 = [[int(rl) for rl in list(l)] for l in tile1]

def displayMtrx(mtrx):
    for line in mtrx:
        print(line)

def createTiles(tiles = [], currentIter = 1, maxIter = 8):
    curr = tiles[-1]
    tileX = [[1 if l + 1 == 10 else l + 1 for l in line] for line in curr]
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

tt = createTiles([tile1], currentIter = 1, maxIter = 8)

t0, t1, t2, t3, t4, t5, t6, t7, t8 = tt[0], tt[1], tt[2], tt[3], tt[4], tt[5], tt[6], tt[7], tt[8]
mtrx = [[t0,t1,t2,t3,t4], [t1,t2,t3,t4,t5], [t2,t3,t4,t5,t6], [t3,t4,t5,t6,t7], [t4,t5,t6,t7,t8]]

cave = createMatrix(mtrx)

def djikstras(source, graph):
    q = [(i, j) for i in range(len(graph)) for j in range(len(graph[i]))]
    dist = {((i, j)):(inf if (i, j) != source else 0) for i in range(len(graph)) for j in range(len(graph[i]))}
    while len(q) != 0:
        v = min({key:dist[key] for key in dist if key in q}, key={key:dist[key] for key in dist if key in q}.get)
        i, j = v[0], v[1]
        q.remove(v)
        adj = getAdjacent(graph, i, j, False)
        for a in adj:
            u, weight = a[1], a[0]
            du, dv = dist[u], dist[v]
            if dv + weight < du:
                dist[u] = dv + weight
    return dist
#end def djikstras

shortest = djikstras((0, 0), tile1)
print(shortest)