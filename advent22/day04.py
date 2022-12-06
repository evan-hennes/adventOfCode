from useful import convertToVar

inp = convertToVar("advent22/day04Input.txt", '\n')
assignment1 = []
assignment2 = []
counter = 0

for line in inp:
    line = line.split(",")
    #print(line)
    curr1 = line[0].split('-')
    curr2 = line[1].split('-')
    curr1[0] = int(curr1[0])
    curr1[1] = int(curr1[1])
    curr2[0] = int(curr2[0])
    curr2[1] = int(curr2[1])
    for i in range(curr1[0], curr1[1] + 1):
        assignment1.append(i)
    for i in range(curr2[0], curr2[1] + 1):
        assignment2.append(i)
    if(any(x in assignment1 for x in assignment2) or any(x in assignment2 for x in assignment1)):
        counter += 1
    assignment1.clear()
    assignment2.clear()
print(counter)