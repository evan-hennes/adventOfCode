from useful import convertToVar

inp = convertToVar("advent22/day03Input.txt", '\n')
conversion = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = 0
curr3 = []
score = 0

# for line in inp:
#     comp1 = line[0:int(len(line)/2)]
#     comp2 = line[int(len(line)/2):]
#     arr1 = []
#     arr2 = []
#     for c in comp1:
#         arr1.append(conversion.index(c))
#     for c in comp2:
#         if(conversion.index(c) in arr1 and conversion.index(c) not in arr2):
#             #print(conversion.index(c))
#             score += conversion.index(c)
#         arr2.append(conversion.index(c))

for line in inp:
    if (counter % 3 == 0 and counter != 0):
        for c in curr3[0]:
            if(c in curr3[1] and c in curr3[2]):
                #print(c)
                score += c
                break
        curr3.clear()
    line = list(line)
    for c in range(len(line)):
        line[c] = conversion.index(line[c])
    curr3.append(line)
    #print(len(curr3))
    counter += 1

for c in curr3[0]:
    if(c in curr3[1] and c in curr3[2]):
        #print(c)
        score += c
        break

print(score)