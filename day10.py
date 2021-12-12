from useful import convertToVar

def cock(val, dick):
    for key, value in dick.items():
         if val == value:
             return key
    return "key doesn't exist"

lines = convertToVar('day10Input.txt', '\n')
for schmeat in range(len(lines)):
    lines[schmeat] = list(lines[schmeat])

containers = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

score = 0
score2 = []
badLines = []
for line in lines:
    #print(line)
    stack = []
    for c in line:
        #print(c, stack)
        if c in containers:
            stack.append(c)
        elif c in containers.values():
            pee = cock(c, containers)
            if stack.pop() != pee:
                badLines.append(line)
                if containers[pee] == ')':
                    score += 3
                    break
                elif containers[pee] == ']':
                    score += 57
                    break
                elif containers[pee] == '}':
                    score += 1197
                    break
                else:
                    score += 25137
                    break
    if line not in badLines:
        closeyBoys = reversed(stack)
        closeyBoys = [containers[c] for c in closeyBoys]
        current = 0
        for penis in closeyBoys:
            current *= 5
            if penis == ')':
                current += 1
            elif penis == ']':
                current += 2
            elif penis == '}':
                current += 3
            else:
                current += 4
        score2.append(current)
cummies = sorted(score2)[len(score2)//2]
print(score, cummies)

