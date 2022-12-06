from useful import convertToVar

inp = convertToVar("advent22/day02Input.txt", '\n')
scores = {'A':1, 'X':1, 'B':2, 'Y':2, 'C':3, 'Z':3}
#conversions = {'A':'X', 'B':'Y', 'C':'Z'}
p2Score = 0

for line in inp:
    plays = line.split(' ')
    p1Hand = plays[0]
    p2Hand = plays[1]
    #p2Score += scores[plays[1]]
    #p1Hand = conversions[p1Hand]
    if(p2Hand == "Y"):
        p2Score += 3
        p2Score += scores[p1Hand]
    elif(p2Hand == "Z"):
        p2Score += 6
        if(p1Hand == "A"):
            p2Score += scores['B']
        elif(p1Hand == "B"):
            p2Score += scores['C']
        else:
            p2Score += scores['A']
    else:
        if(p1Hand == "A"):
            p2Score += scores['C']
        elif(p1Hand == "B"):
            p2Score += scores['A']
        else:
            p2Score += scores['B']
    #print(p2Score)

print(p2Score)
