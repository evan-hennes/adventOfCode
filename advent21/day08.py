from useful import convertToVar

digits = convertToVar('day08Input.txt', '\n')

# unique = 0
# for d in digits:
#     tot = d.split('|')
#     out = tot[-1]
#     out = out.strip()
#     out = out.split(' ')
#     for num in out:
#         if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
#             unique += 1
# print(unique)

def getOneChars(ns):
    oneChars = []
    for n in ns:
        ln = len(n)
        if ln == 2:
            for x in n:
                oneChars.append(x)
    return set(oneChars)

def getSevenChars(ns):
    sevenChars = []
    for n in ns:
        ln = len(n)
        if ln == 3:
            for x in n:
                sevenChars.append(x)
    return set(sevenChars)

def getFourChars(ns):
    fourChars = []
    for n in ns:
        ln = len(n)
        if ln == 4:
            for x in n:
                fourChars.append(x)
            break
    return set(fourChars)

def getEightChars(ns):
    eightChars = []
    for n in ns:
        ln = len(n)
        if ln == 7:
            for x in n:
                eightChars.append(x)
            break
    return set(eightChars)

def convertToDigits(nums):
    one = getOneChars(nums)
    seven = getSevenChars(nums)
    four = getFourChars(nums)
    eight = getEightChars(nums)
    right = one
    top = seven - one
    topLeftCenter = four - one
    bottomLeftCorner = eight - four - top
    totalLetters = right.union(top).union(topLeftCenter).union(bottomLeftCorner)
    #print(right, top, topLeftCenter, bottomLeftCorner)
    digi = []
    for n in nums:
        nList = set(list(n))
        if nList == one:
            digi.append(1)
        elif nList == seven:
            digi.append(7)
        elif nList == four:
            digi.append(4)
        elif nList == eight:
            digi.append(8)
        elif len(nList) == 6:
            if not right.issubset(nList):
                digi.append(6)
            elif not bottomLeftCorner.issubset(nList):
                digi.append(9)
            else:
                digi.append(0)
        elif len(nList) == 5:
            if not topLeftCenter.issubset(nList) and not right.issubset(nList):
                digi.append(2)
            elif not topLeftCenter.issubset(nList) and not bottomLeftCorner.issubset(nList):
                digi.append(3)
            else:
                digi.append(5)
    return digi


totalDigs = []
for d in digits:
    tot = d.split('|')
    inp = tot[0].strip().split(' ')
    out = tot[-1].strip().split(' ')
    numbers = inp + out
    numbers = convertToDigits(numbers)[-4:]
    #print(numbers)
    totalDigs.append(numbers)
#print(totalDigs)
s = 0
for x in totalDigs:
    x = [str(i) for i in x]
    x = int(''.join(x))
    #print(x)
    s += x
print(s)