from useful import convertToVar
from collections import defaultdict

lines = convertToVar("day05Input.txt", '\n')

pointsFilled = defaultdict(int)
for line in  lines:
    line = line.split(' -> ')
    point1 = line[0].split(',')
    point2 = line[1].split(',')
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])
    if x1 == x2:
        yPoint = min(y1, y2)
        while yPoint <= max(y1, y2):
            pointsFilled[(x1, yPoint)] += 1
            yPoint += 1
    elif y1 == y2:
        xPoint = min(x1, x2)
        while xPoint <= max(x1, x2):
            pointsFilled[(xPoint, y1)] += 1
            xPoint += 1
    else:
        xPoint = x1
        yPoint = y1
        if x1 < x2:
            if y1 < y2:
                while xPoint <= x2:
                    pointsFilled[(xPoint, yPoint)] += 1
                    xPoint += 1
                    yPoint += 1
            else:
                while xPoint <= x2:
                    pointsFilled[(xPoint, yPoint)] += 1
                    xPoint += 1
                    yPoint -= 1
        else:
            if y1 < y2:
                while xPoint >= x2:
                    pointsFilled[(xPoint, yPoint)] += 1
                    xPoint -= 1
                    yPoint += 1
            else:
                while xPoint >= x2:
                    pointsFilled[(xPoint, yPoint)] += 1
                    xPoint -= 1
                    yPoint -= 1
print(pointsFilled)

poggers = 0
for key in pointsFilled:
    if pointsFilled[key] > 1:
        poggers += 1
print(poggers)