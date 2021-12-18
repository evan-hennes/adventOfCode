from useful import convertToVar
import math

def binToDec(n):
    return int(n, 2)

hexa = convertToVar('day16Input.txt', ' ')[0]

hexDict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',\
     'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

binStr = ''
for c in hexa:
    binStr += hexDict[c]

def parsePackets(binary):
    v = binToDec(binary[:3])
    t = binToDec(binary[3:6])
    vSum = v
    if t == 4:
        lits = []
        rem = ''
        for i in range(6, len(binary) + 1, 5):
            lits.append(binary[i+1:i+5])
            if binary[i] == '0':
                rem = binary[i+5:]
                break
        lits = binToDec(''.join(lits))
        return (rem, lits)
    else:
        sp = []
        lenType = binToDec(binary[6])
        if lenType == 0:
            subPacketLen = binToDec(binary[7:22])
            subPackets = binary[22:22+subPacketLen]
            while len(subPackets) != 0:
                spv = parsePackets(subPackets)
                subPackets = spv[0]
                sp.append(spv[1])
            subPackets = binary[22+subPacketLen:]
        else:
            numSubPackets = binToDec(binary[7:18])
            subPackets = binary[18:]
            for i in range(numSubPackets):
                spv = parsePackets(subPackets)
                subPackets = spv[0]
                sp.append(spv[1])
        if t == 0:
            return (subPackets, sum(sp))
        elif t == 1:
            return (subPackets, math.prod(sp))
        elif t == 2:
            return (subPackets, min(sp))
        elif t == 3:
            return (subPackets, max(sp))
        elif t == 5:
            if sp[0] > sp[1]:
                return (subPackets, 1)
            else:
                return (subPackets, 0)
        elif t == 6:
            if sp[0] < sp[1]:
                return (subPackets, 1)
            else:
                return (subPackets, 0)
        else:
            if sp[0] == sp[1]:
                return (subPackets, 1)
            else:
                return (subPackets, 0)
#end my life
        

print(parsePackets(binStr)[1])