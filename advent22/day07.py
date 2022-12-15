from useful import convertToVar
from collections import defaultdict

currPath = []
inp = convertToVar("advent22/day07Input.txt", '\n')
# directories = {"":0}
directories = defaultdict(int) 

for line in inp:
    if line[:4] == "$ cd":
        currDir = line[5:]
        if(currDir == ".."):
            currPath.pop()
        else:
            currPath.append(line[5:])
    elif line[:4] != "$ ls":
        line = line.split(' ')
        if line[0] == 'dir': continue
        size = int(line[0])
        directories[""] += size
        relPath = ""
        for char in currPath:
            relPath += '/' + char 
            directories[relPath] += size
# print(directories)
sum = 0
for key in directories:
    if directories[key] < 100_000:
        sum += directories[key]
print(sum)

# remember directories[''] is the size of root
# availableSpace = 70_000_000 - directories['']
# currMin = 70_000_000
# dirToDelete = ''
# for key in directories:
#     if directories[key] > 30_000_000 - availableSpace and directories[key] < currMin:
#         currMin = directories[key]
#         dirToDelete = key
# print(currMin)

print(min(x for x in directories.values() if x > directories[''] - 40_000_000))

"""
use a single dictionary to store the sizes of all directories
the keys of this dictionary should be the full path for the directory

when u encounter a file just ahead and add its size to every single parent directory

store your path as a list of string. like /a/a would be ["a","a"]
to make the key for the dictionary you could just do '/'.join(path)
or to take some prefix of the path: '/'.join(path[:end])
"""
