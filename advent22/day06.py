from useful import convertToVar

inp = convertToVar("advent22/day06Input.txt", '\n')
count = 0
#print(inp)
for i in range(14, len(inp[0])):
    curr = inp[0][i - 14:i]
    #print(curr)
    if(len(set(curr)) == len(curr)):
        count += i
        break
    else:
        continue
print(count)