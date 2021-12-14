from useful import convertToVar
from collections import defaultdict

polymerShit = convertToVar('day14Input.txt', '\n')
template = polymerShit[0]
rs = polymerShit[2:]
rs = [rule.split(' -> ') for rule in rs]

rules = dict()
for key, val in rs:
    rules[key] = val

polymer = template
frequencies = defaultdict(int)
pairs = defaultdict(int)

for c in polymer:
    frequencies[c] += 1

next = ''
for i in range(len(polymer) - 1):
    pair = polymer[i:i + 2]
    pairs[pair] += 1
print(pairs)

for i in range(40):
    newPairs = defaultdict(int)
    for pair, freq in pairs.items():
        new = rules[pair]
        frequencies[new] += freq
        p1, p2 = pair[0] + new, new + pair[1]
        #print(pair, new, p1, p2)
        newPairs[p1] += freq
        newPairs[p2] += freq
    pairs = newPairs
    #print(newPairs)

maxFreq = max(frequencies, key = frequencies.get)
minFreq = min(frequencies, key = frequencies.get)

res = frequencies[maxFreq] - frequencies[minFreq]
print(res)