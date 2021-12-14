from useful import convertToVar

dotsAndFolds = convertToVar('day13Input.txt', '\n')
splitNdx = dotsAndFolds.index('')
dots = dotsAndFolds[0:splitNdx]
folds = dotsAndFolds[splitNdx + 1:]
dots = [d.split(',') for d in dots]
dots = set([tuple([int(coord) for coord in pt]) for pt in dots])
print(len(dots))

firstFold = folds[0]
firstFold = str(firstFold.split('fold along ')[1]).split('=')


if firstFold[0] == 'y':
    loc = int(firstFold[1])
    updated = set()
    for x, y in dots:
        if y == loc:
            continue
        elif y > loc:
            updated.add((x, loc - (y - loc)))
        else:
            updated.add((x, y))
else:
    loc = int(firstFold[1])
    updated = set()
    for x, y in dots:
        if x == loc:
            continue
        elif x > loc:
            updated.add((loc - (x - loc), y))
        else:
            updated.add((x, y))
print(len(updated))

lastX, lastY = None, None
for f in folds:
    fold = str(f.split('fold along ')[1]).split('=')
    axis, loc = fold[0], int(fold[1])
    if axis == 'y':
        updated = set()
        for x, y in dots:
            if y == loc:
                continue
            elif y > loc:
                updated.add((x, loc - (y - loc)))
            else:
                updated.add((x, y))
        lastY = loc
    else:
        updated = set()
        for x, y in dots:
            if x == loc:
                continue
            elif x > loc:
                updated.add((loc - (x - loc), y))
            else:
                updated.add((x, y))
        lastX = loc
    dots = updated

mtrx = []
for i in range(lastY):
    line = []
    for j in range(lastX):
        if (j, i) in updated:
            line.append('#')
        else:
            line.append('.')
    mtrx.append(line)
for ln in mtrx:
    print(ln)