from useful import convertToVar

fishies = convertToVar("day06Input.txt", ',')

for hek in range(len(fishies)):
    fishies[hek] = int(fishies[hek])

day = 0
i = 0
zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights = fishies.count(0), fishies.count(1),\
    fishies.count(2), fishies.count(3), fishies.count(4), fishies.count(5), fishies.count(6), fishies.count(7), fishies.count(8)
print(zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights)
while day < 256:
    og0, og1, og2, og3, og4, og5, og6, og7, og8 = zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights
    sevens = og8
    sixes = og7 + og0
    fives = og6
    fours = og5
    threes = og4
    twos = og3
    ones = og2
    zeroes = og1
    eights = og0
    day += 1
    #print(zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights)
total = zeroes + ones + twos + threes + fours + fives + sixes + sevens + eights
print(total)