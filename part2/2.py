#!/usr/bin/python3

from collections import defaultdict

#############
#01.2.3.4.56#
###7#8#9#a###
  #b#c#d#e#
  #########

coords = {
        0:  (0,  0),
        1:  (1,  0),
        2:  (3,  0),
        3:  (5,  0),
        4:  (7,  0),
        5:  (9,  0),
        6:  (10, 0),
        7:  (2,  1),
        8:  (4,  1),
        9:  (6,  1),
        10: (8,  1),
        11: (2,  2),
        12: (4,  2),
        13: (6,  2),
        14: (8,  2),
        15: (2,  3),
        16: (4,  3),
        17: (6,  3),
        18: (8,  3),
        19: (2,  4),
        20: (4,  4),
        21: (6,  4),
        22: (8,  4)
        }

costs = [[abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]) for i in range(23)] for j in range(23)]

passes = [
    [(0,) for i in range(7)] +
    [(1, 7)] +
    [(1, 2, 8)] +
    [(1, 2, 3, 9)] +
    [(1, 2, 3, 4, 10)] +
    [(1, 7, 11)] +
    [(1, 2, 8, 12)] +
    [(1, 2, 3, 9, 13)] +
    [(1, 2, 3, 4, 10, 14)] +
    [(1, 7, 11, 15)] +
    [(1, 2, 8, 12, 16)] +
    [(1, 2, 3, 9, 13, 17)] +
    [(1, 2, 3, 4, 10, 14, 18)] +
    [(1, 7, 11, 15, 19)] +
    [(1, 2, 8, 12, 16, 20)] +
    [(1, 2, 3, 9, 13, 17, 21)] +
    [(1, 2, 3, 4, 10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(7,)] +
    [(2, 8)] +
    [(2, 3, 9)] +
    [(2, 3, 4, 10)] +
    [(7, 11)] +
    [(2, 8, 12)] +
    [(2, 3, 9, 13)] +
    [(2, 3, 4, 10, 14)] +
    [(7, 11, 15)] +
    [(2, 8, 12, 16)] +
    [(2, 3, 9, 13, 17)] +
    [(2, 3, 4, 10, 14, 18)] +
    [(7, 11, 15, 19)] +
    [(2, 8, 12, 16, 20)] +
    [(2, 3, 9, 13, 17, 21)] +
    [(2, 3, 4, 10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(7,)] +
    [(8,)] +
    [(3, 9)] +
    [(3, 4, 10)] +
    [(7, 11)] +
    [(8, 12)] +
    [(3, 9, 13)] +
    [(3, 4, 10, 14)] +
    [(7, 11, 15)] +
    [(8, 12, 16)] +
    [(3, 9, 13, 17)] +
    [(3, 4, 10, 14, 18)] +
    [(7, 11, 15, 19)] +
    [(8, 12, 16, 20)] +
    [(3, 9, 13, 17, 21)] +
    [(3, 4, 10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(2, 7)] +
    [(8,)] +
    [(9,)] +
    [(4, 10)] +
    [(2, 7, 11)] +
    [(8, 12)] +
    [(9, 13)] +
    [(4, 10, 14)] +
    [(2, 7, 11, 15)] +
    [(8, 12, 16)] +
    [(9, 13, 17)] +
    [(4, 10, 14, 18)] +
    [(2, 7, 11, 15, 19)] +
    [(8, 12, 16, 20)] +
    [(9, 13, 17, 21)] +
    [(4, 10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(2, 3, 7)] +
    [(3, 8)] +
    [(9,)] +
    [(10,)] +
    [(2, 3, 7, 11)] +
    [(3, 8, 12)] +
    [(9, 13)] +
    [(10, 14)] +
    [(2, 3, 7, 11, 15)] +
    [(3, 8, 12, 16)] +
    [(9, 13, 17)] +
    [(10, 14, 18)] +
    [(2, 3, 7, 11, 15, 19)] +
    [(3, 8, 12, 16, 20)] +
    [(9, 13, 17, 21)] +
    [(10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(2, 3, 4, 7)] +
    [(3, 4, 8)] +
    [(4, 9)] +
    [(10,)] +
    [(2, 3, 4, 7, 11)] +
    [(3, 4, 8, 12)] +
    [(4, 9, 13)] +
    [(10, 14)] +
    [(2, 3, 4, 7, 11, 15)] +
    [(3, 4, 8, 12, 16)] +
    [(4, 9, 13, 17)] +
    [(10, 14, 18)] +
    [(2, 3, 4, 7, 11, 15, 19)] +
    [(3, 4, 8, 12, 16, 20)] +
    [(4, 9, 13, 17, 21)] +
    [(10, 14, 18, 22)],

    [(0,) for i in range(7)] +
    [(2, 3, 4, 5, 7)] +
    [(3, 4, 5, 8)] +
    [(4, 5, 9)] +
    [(5, 10)] +
    [(2, 3, 4, 5, 7, 11)] +
    [(3, 4, 5, 8, 12)] +
    [(4, 5, 9, 13)] +
    [(5, 10, 14)] +
    [(2, 3, 4, 5, 7, 11, 15)] +
    [(3, 4, 5, 8, 12, 16)] +
    [(4, 5, 9, 13, 17)] +
    [(5, 10, 14, 18)] +
    [(2, 3, 4, 5, 7, 11, 15, 19)] +
    [(3, 4, 5, 8, 12, 16, 20)] +
    [(4, 5, 9, 13, 17, 21)] +
    [(5, 10, 14, 18, 22)],

    [(0, 1)] +
    [(1,)] +
    [(2,)] +
    [(2, 3)] +
    [(2, 3, 4)] +
    [(2, 3, 4, 5)] +
    [(2, 3, 4, 5, 6)] +
    [(0,) for i in range(16)],

    [(0, 1, 2)] +
    [(1, 2)] +
    [(2,)] +
    [(3,)] +
    [(3, 4)] +
    [(3, 4, 5)] +
    [(3, 4, 5, 6)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3)] +
    [(1, 2, 3)] +
    [(2, 3)] +
    [(3,)] +
    [(4,)] +
    [(4, 5)] +
    [(4, 5, 6)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 4)] +
    [(1, 2, 3, 4)] +
    [(2, 3, 4)] +
    [(3, 4)] +
    [(4,)] +
    [(5,)] +
    [(5, 6)] +
    [(0,) for i in range(16)],

    [(0, 1, 7)] +
    [(1, 7)] +
    [(2, 7)] +
    [(2, 3, 7)] +
    [(2, 3, 4, 7)] +
    [(2, 3, 4, 5, 7)] +
    [(2, 3, 4, 5, 6, 7)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 8)] +
    [(1, 2, 8)] +
    [(2, 8)] +
    [(3, 8)] +
    [(3, 4, 8)] +
    [(3, 4, 5, 8)] +
    [(3, 4, 5, 6, 8)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 9)] +
    [(1, 2, 3, 9)] +
    [(2, 3, 9)] +
    [(3, 9)] +
    [(4, 9)] +
    [(4, 5, 9)] +
    [(4, 5, 6, 9)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 4, 10)] +
    [(1, 2, 3, 4, 10)] +
    [(2, 3, 4, 10)] +
    [(3, 4, 10)] +
    [(4, 10)] +
    [(5, 10)] +
    [(5, 6, 10)] +
    [(0,) for i in range(16)],

    [(0, 1, 7, 11)] +
    [(1, 7, 11)] +
    [(2, 7, 11)] +
    [(2, 3, 7, 11)] +
    [(2, 3, 4, 7, 11)] +
    [(2, 3, 4, 5, 7, 11)] +
    [(2, 3, 4, 5, 6, 7, 11)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 8, 12)] +
    [(1, 2, 8, 12)] +
    [(2, 8, 12)] +
    [(3, 8, 12)] +
    [(3, 4, 8, 12)] +
    [(3, 4, 5, 8, 12)] +
    [(3, 4, 5, 6, 8, 12)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 9, 13)] +
    [(1, 2, 3, 9, 13)] +
    [(2, 3, 9, 13)] +
    [(3, 9, 13)] +
    [(4, 9, 13)] +
    [(4, 5, 9, 13)] +
    [(4, 5, 6, 9, 13)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 4, 10, 14)] +
    [(1, 2, 3, 4, 10, 14)] +
    [(2, 3, 4, 10, 14)] +
    [(3, 4, 10, 14)] +
    [(4, 10, 14)] +
    [(5, 10, 14)] +
    [(5, 6, 10, 14)] +
    [(0,) for i in range(16)],

    [(0, 1, 7, 11, 15)] +
    [(1, 7, 11, 15)] +
    [(2, 7, 11, 15)] +
    [(2, 3, 7, 11, 15)] +
    [(2, 3, 4, 7, 11, 15)] +
    [(2, 3, 4, 5, 7, 11, 15)] +
    [(2, 3, 4, 5, 6, 7, 11, 15)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 8, 12, 16)] +
    [(1, 2, 8, 12, 16)] +
    [(2, 8, 12, 16)] +
    [(3, 8, 12, 16)] +
    [(3, 4, 8, 12, 16)] +
    [(3, 4, 5, 8, 12, 16)] +
    [(3, 4, 5, 6, 8, 12, 16)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 9, 13, 17)] +
    [(1, 2, 3, 9, 13, 17)] +
    [(2, 3, 9, 13, 17)] +
    [(3, 9, 13, 17)] +
    [(4, 9, 13, 17)] +
    [(4, 5, 9, 13, 17)] +
    [(4, 5, 6, 9, 13, 17)] +
    [(0,) for i in range(16)],

    [(0, 1, 2, 3, 4, 10, 14, 18)] +
    [(1, 2, 3, 4, 10, 14, 18)] +
    [(2, 3, 4, 10, 14, 18)] +
    [(3, 4, 10, 14, 18)] +
    [(4, 10, 14, 18)] +
    [(5, 10, 14, 18)] +
    [(5, 6, 10, 14, 18)] +
    [(0,) for i in range(16)]
    ]

multiplier = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def return_amphipods_home(state, habitat):
    d = defaultdict(set) # dijkstra
    d[0].add(tuple(state))
    size = len(state)

    for c in range(200000):
        for s in d[c]:
            if all([all([s[i] == amphipod for i in habitat[amphipod]]) for amphipod in multiplier]):
                return c
                break
            for pos, amphipod in enumerate(s):
                if not amphipod: continue
                for target in range(size):
                    if s[target]: continue
                    if any([s[i] for i in passes[pos][target]]): continue
                    if pos < 7 and target < 7: continue
                    if pos > 6 and target > 6: continue
                    if target > 6 and target not in habitat[amphipod]: continue
                    if target in habitat[amphipod] and any([(s[i] != amphipod and s[i] != '') for i in habitat[amphipod]]): continue
                    if target in habitat[amphipod] and any([not s[i] if i > target else 0 for i in habitat[amphipod]]): continue
                    if pos in habitat[amphipod] and all([s[i] == amphipod if i > pos else 1 for i in habitat[amphipod]]): continue
                    new_s = list(s)
                    new_s[pos] = ''
                    new_s[target] = amphipod
                    d[c + multiplier[amphipod] * costs[pos][target]].add(tuple(new_s))
        else: continue
        break

with open('input.txt') as f:
    lines = f.read().splitlines()[2:-1]

state = ['' for i in range(15)]

for i in range(7, 11):
    state[i]   = lines[0][i*2 - 11]
    state[i+4] = lines[1][i*2 - 11]

habitat = {
        'A': (7, 11),
        'B': (8, 12),
        'C': (9, 13),
        'D': (10, 14)
        }

print(return_amphipods_home(state, habitat))

state = ['' for i in range(23)]

for i in range(7, 11):
    state[i]   = lines[0][i*2 - 11]
    state[i+12] = lines[1][i*2 - 11]
state[11] = 'D'
state[12] = 'C'
state[13] = 'B'
state[14] = 'A'
state[15] = 'D'
state[16] = 'B'
state[17] = 'A'
state[18] = 'C'

habitat = {
        'A': (7, 11, 15, 19),
        'B': (8, 12, 16, 20),
        'C': (9, 13, 17, 21),
        'D': (10, 14, 18, 22)
        }

print(return_amphipods_home(state, habitat))
