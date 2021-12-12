import useful

inp = useful.convertToVar('day02Input.txt', '\n')
x = 0
y = 0
for i in inp:
    splt = i.split(' ')
    dir = splt[0]
    amt = int(splt[1])
    if dir == 'forward':
        x += amt
    elif dir == 'down':
        y += amt
    else:
        y -= amt
print(x * y)

x = 0
y = 0
aim = 0
for i in inp:
    splt = i.split(' ')
    dir = splt[0]
    amt = int(splt[1])
    if dir == 'forward':
        x += amt
        y += (aim * amt)
    elif dir == 'down':
        aim += amt
    else:
        aim -= amt
print(x * y)