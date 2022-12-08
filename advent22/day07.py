from useful import convertToVar

currDir = "/"
inp = convertToVar("advent22/day07Input.txt", '\n')
directories = {}

def getDirSum(currSum, dir):
    print("going again")
    for obj in directories[dir]:
        print("looping over files in " + dir)
        if type(obj) is tuple:
            currSum += obj[1]
            print("added " + str(obj[1]) + " to " + str(currSum))
        else:
            print("recursively going into directory " + obj)
            currSum += getDirSum(currSum, obj)
    print("current sum: " + str(currSum))
    return currSum

for line in inp:
    if(line[0] == "$"):
        if(line[2:4] == "cd"):
            curr = line[5:]
            if(curr == ".."):
                if(currDir.rindex("/") == 0):
                    currDir = "/"
                else:
                    currDir = currDir[0:currDir.rindex("/")]
            else:
                if(curr == "/"):
                    continue
                else:
                    if(currDir[len(currDir) - 1] == "/"):
                        currDir += curr
                    else:
                        currDir += "/" + curr
            #print(currDir)
        else:
            #print("listing directory contents")
            continue
    else:
        if(line[0:3] == "dir"):
            if(currDir[len(currDir) - 1] in directories):
                directories[currDir[len(currDir) - 1]].append(line[4:])
            else:
                directories[currDir[len(currDir) - 1]] = [line[4:]]
        else:
            splitLine = line.split(" ")
            tup = (splitLine[1], int(splitLine[0]))
            if(currDir[len(currDir) - 1] in directories):
                directories[currDir[len(currDir) - 1]].append(tup)
            else:
                directories[currDir[len(currDir) - 1]] = [tup]
print(directories)

# dirSums = []
# for dir in directories:
#     dirSums.append(getDirSum(0, dir))
# print(dirSums)
print(getDirSum(0, '/'))