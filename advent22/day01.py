import useful

inp = useful.convertToVar("advent22\day01Input.txt", "\n")
maxSum = 0
sum = 0
sumList = []
for line in inp:
    if(line != ""):
        sum += int(line)
    else:
        if(sum > maxSum):
            maxSum = sum
        sumList.append(sum)
        sum = 0
print(maxSum)
sumList.sort()
print(sumList[-1] + sumList[-2] + sumList[-3])