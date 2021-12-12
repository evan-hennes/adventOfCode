from useful import convertToVar

#a = [1, 2, 3, 4, 5, 6]
#print(sum(a))

def addSummation(initial = 1, final = 2):
    return sum([i for i in range(initial, final + 1)])
#end def addSummation

positions = convertToVar("day07Input.txt", ',')
positions = [int(p) for p in positions]

sPositions = sorted(positions)
# movements = []

# for i in range(sPositions[0], sPositions[-1]):
#     total = 0
#     for p in sPositions:
#         total += abs(i - p)
#     movements.append(total)
# mn = min(movements)
# print(mn)

movements = []

#print(addSummation(1, 11))

for i in range(sPositions[0], sPositions[-1]):
    total = 0
    for p in sPositions:
        total += addSummation(1, abs(i - p))
    movements.append(total)
mn = min(movements)
print(mn)