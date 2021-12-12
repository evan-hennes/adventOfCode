from useful import convertToVar

inp = convertToVar("day01Input.txt", '\n')
inc = 0
for i in range(1, len(inp)):
    if int(inp[i]) > int(inp[i - 1]):
        inc += 1
print(inc)

inc = 0
for i in range(1, len(inp) - 2):
    a = int(inp[i - 1])
    b = int(inp[i])
    c = int(inp[i + 1])
    d = int(inp[i + 2])
    aSum = a + b + c
    bSum = b + c + d
    if bSum > aSum:
        inc += 1
print(inc)