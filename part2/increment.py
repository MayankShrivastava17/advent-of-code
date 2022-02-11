with open("input.txt") as infile:
    data = [int(line) for line in infile.readlines()]

pass_one = [sum(data[j-3:j]) for j in range(3, len(data)+1)]
print (sum([pass_one[i-1] < pass_one[i] for i in range(1,len(pass_one))]))