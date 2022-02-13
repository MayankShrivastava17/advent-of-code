from collections import Counter

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

most, least = "", ""

for col in range(len(data[0])):
    out = Counter([line[col] for line in data])
    if out["1"] > out["0"]:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"

print(int(most, 2) * int(least, 2))