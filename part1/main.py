from scipy import ndimage
import numpy as np

with open("input.txt", "r") as f:
    dem = np.array([[*map(int, line)] for line in f.read().splitlines()])

adjacent = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
lowest_neighbor = ndimage.rank_filter(dem, 1, footprint=adjacent, mode="constant", cval=9.0)
low_points_mask = dem < lowest_neighbor

basins_mask = ndimage.binary_dilation(low_points_mask, structure=adjacent, iterations=-1, mask=dem != 9)
basins, n_basins = ndimage.label(basins_mask, structure=adjacent)
basin_nrs, basin_sizes = np.unique(basins[basins>0], return_counts=True)

print(f"Answer 1: {np.sum(dem[low_points_mask] + 1)}")
print(f"Answer 2: {np.product(basin_sizes[np.argsort(basin_sizes)[-3:]])}")
