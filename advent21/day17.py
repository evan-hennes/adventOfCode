from useful import convertToVar
from math import inf
import sys
sys.setrecursionlimit(2000)

targetArea = convertToVar('day17Input.txt', ' ')[2:]
targetArea = [rng[2:].split('..') for rng in targetArea]
targetArea = ((int(targetArea[0][0]), int(targetArea[1][0])), (int(targetArea[0][1][:-1]), int(targetArea[1][1])))

'''
step function (current position, current velocity, max y value)
    current x += current x velocity
    current y += current y velocity
    if current y > max y value
        max y value = current y
    vx +=/-= 1 #depends on if vx is pos or neg
    vy -= 1
    if x and y in targetArea
        return True & max y value
    elif x < targetArea and y > targetArea
        return step(new position, new velocity, max y value)
    else
        return False & 
'''
def step(curr, velo, initVelo):
    x, y = curr
    vx, vy = velo
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    newCurr, newVelo = (x, y), (vx, vy)
    if (targetArea[0][0] <= x <= targetArea[1][0]) and (targetArea[0][1] <= y <= targetArea[1][1]):
        return (True, initVelo)
    elif x < targetArea[1][0] and y > targetArea[0][1]:
        return step(newCurr, newVelo, initVelo)
    else:
        return (False, (0, 0))
#end me please

start = (0, 0)
initVelos = []
for i in range(500):
    for j in range(-500, 500):
        pog, initVelo = step(start, (i, j), (i, j))
        if pog:
            initVelos.append(initVelo)
print(len(initVelos))