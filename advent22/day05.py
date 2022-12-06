from useful import convertToVar

inp = convertToVar("advent22/day05Input.txt", '\n')
directions = 0
stacks = [[], [], [], [], [], [], [], [], []]
tops = ""

for line in inp:
    if(line == ''):
        directions = 1
        #print('oop')
        continue
    if not directions:
        lCount = 0
        for char in line:
            if char != '[' and char != ']' and char != ' ' and not char.isdigit():
                currStack = (lCount // 4)
                #print(currStack, char)
                if(currStack - 1 > len(stacks)):
                    currStack -= 1
                stacks[currStack].append(char)
                lCount += 1
            else:
                lCount += 1
    else:
        line = line.split()
        numBlocks = int(line[1])
        fromStack = int(line[3]) - 1
        toStack = int(line[5]) - 1
        #print(numBlocks, fromStack, toStack)
        #print(stacks[toStack], stacks[fromStack])
        # for i in range(numBlocks):
        #     stacks[toStack].insert(0, stacks[fromStack][0])
        #     stacks[fromStack].pop(0)
        miniStack = []
        if(numBlocks == 1):
            miniStack.append(stacks[fromStack][0])
        else:
            miniStack = stacks[fromStack][0:numBlocks]
        stacks[fromStack] = stacks[fromStack][numBlocks:]
        #print(stacks[toStack], miniStack)
        stacks[toStack] = miniStack + stacks[toStack]
#print(stacks)
for stack in stacks:
    tops += stack[0]
print(tops)
    