from useful import convertToVar
import pandas as pd

binary = convertToVar('day03Input.txt', '\n')
#print(binary)
gammaRate = ''
epsilonRate = ''
for b in range(len(binary)):
    binary[b] = [bit for bit in binary[b]]
    #print(b)
df = pd.DataFrame(binary)
for i in range(12):
    zCount = df[i].value_counts(sort = False)
    #print(zCount)
    #print(zCount[0], zCount[1])
    if zCount[1] > zCount[0]:
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'

gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)
print(gammaRate * epsilonRate)

df2 = df

for i in range(12):
    if len(df.index) == 1:
        break
    count = df[i].value_counts()
    #print(count)
    countNdx = count.index.tolist()
    if len(countNdx) == 1:
        if countNdx[0] == '0':
            zeroes = count[0]
        else:
            ones = count[0]
    elif countNdx[0] == '0':
        zeroes = count[0]
        ones = count[1]
    else:
        zeroes = count[1]
        ones = count[0]
    #print(zeroes, ones)
    if ones > zeroes:
        df = df[df[i] == '1']
    elif ones < zeroes:
        df = df[df[i] == '0']
    elif ones == zeroes:
        df = df[df[i] == '1']
    #print(df)
x = df.to_string(header=False, index=False, index_names=False).split('\n')
vals = [''.join(ele.split()) for ele in x]
oxyGenRate = int(vals[0], 2)
#print(oxyGenRate)

for i in range(12):
    if len(df2.index) == 1:
        break
    count = df2[i].value_counts()
    print(count)
    countNdx = count.index.tolist()
    if len(countNdx) == 1:
        if countNdx[0] == '0':
            zeroes = count[0]
        else:
            ones = count[0]
    elif countNdx[0] == '0':
        zeroes = count[0]
        ones = count[1]
    else:
        zeroes = count[1]
        ones = count[0]
    #print(zeroes, ones)
    if ones < zeroes:
        df2 = df2[df2[i] == '1']
    elif ones > zeroes:
        df2 = df2[df2[i] == '0']
    elif ones == zeroes:
        df2 = df2[df2[i] == '0']
    print(df2)
x = df2.to_string(header=False, index=False, index_names=False).split('\n')
vals = [''.join(ele.split()) for ele in x]
carbonScrubberRate = int(vals[0], 2)
print(carbonScrubberRate)
print(oxyGenRate * carbonScrubberRate)