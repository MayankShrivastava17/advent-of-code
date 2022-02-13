import numpy as np

data = np.genfromtxt("input.txt", delimiter=1, dtype=int)

def get_levels(data: np.array, case: int, column: int = 0):
    if data.shape[0] == 1:
        return np.sum([digit * 2 ** i for i, digit in enumerate(data[0][::-1])])
    digit_of_interest = int(sum(data[:, column]) >= (len(data[:, column]) / 2)) ^ case
    return get_levels(data[data[:, column] == digit_of_interest], case, column + 1)

print(get_levels(data, 0) * get_levels(data, 1))