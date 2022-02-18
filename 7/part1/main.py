def compute_fuel_cost1(crabs, align_position):
    fuel_cost = 0
    for crab in crabs:
        fuel_cost += abs(crab - align_position)
    return fuel_cost

def compute_fuel_cost2(crabs, align_position):
    fuel_cost = 0
    for crab in crabs:
        fuel_cost += compute_sum_of_num(abs(crab - align_position))
    return fuel_cost

def compute_sum_of_num(num):
    sum_of_num = 0
    for i in range(num+1):
        sum_of_num += i
    return sum_of_num

def find_solution1(crabs):
    max_crab_position = max(crabs)
    align_positions = range(max_crab_position+1)
    fuel_costs = {}
    for align_position in align_positions:
        fuel_cost = compute_fuel_cost1(crabs, align_position)
        fuel_costs[fuel_cost] = align_position
    lowest_cost = sorted(fuel_costs.keys())[0]
    return lowest_cost

def find_solution2(crabs):
    max_crab_position = max(crabs)
    align_positions = range(max_crab_position+1)
    fuel_costs = {}
    for align_position in align_positions:
        fuel_cost = compute_fuel_cost2(crabs, align_position)
        fuel_costs[fuel_cost] = align_position
    lowest_cost = sorted(fuel_costs.keys())[0]
    return lowest_cost


#INPUT
f = open("input.txt", "r")
data = [int(x) for x in f.read().split("\n")[0].split(",")]
f.close()

#PART 1
print(find_solution1(data))

#PART 2
print(find_solution2(data))