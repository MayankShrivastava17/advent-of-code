with open("input.txt") as infile:
    data = [line for line in infile.readlines()]

d, h, u = 0, 0, 0

for i in data:
    spt = i.split()
    temp = spt[1]
    if spt[0] == 'forward':
        h += int(temp)
    if spt[0] == 'down':
        d += int(temp)
    if spt[0] == 'up':
        u += int(temp)

dpt = abs(d-u)
print(h*dpt)