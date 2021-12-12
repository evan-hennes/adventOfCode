from useful import convertToVar
from collections import defaultdict

connections = convertToVar('day12Input.txt', '\n')
connections = [c.split('-') for c in connections]

conns = defaultdict(list)
for to, frm in connections:
    conns[frm].append(to)
    conns[to].append(frm)
#print(conns)

def go(current, pts, usedSmall):
    if current == 'end':
        return 1
    paths = 0
    pogMoment = conns[current]
    for c in pogMoment:
        used = usedSmall
        if c in pts and usedSmall or c == 'start':
            continue
        if c in pts:
            used = True
        if c.islower():
            pts.add(c)
        paths += go(c, pts, used)
        if c.islower() and (used == usedSmall):
            pts.remove(c)
    return paths

print(go('start', {'start'}, False))