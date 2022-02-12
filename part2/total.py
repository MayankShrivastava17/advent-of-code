with open("input.txt") as infile:
    data = [line for line in infile.readlines()]

h, a, d = 0, 0, 0

for i in data:
    spt = i.split()
    temp = spt[1]
    if spt[0] == 'forward':
        h += int(temp)
        a += d * int(temp)
    if spt[0] == 'down':
        d += int(temp)
    if spt[0] == 'up':
        d -= int(temp)

print (f'horizontal { h }')
print (f'aim { a }')
print(h*a)