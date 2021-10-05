import pandas as pd
import utility as util
from datetime import datetime
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt, image as mpimg

GRID = np.zeros((3, 10))

if __name__ == "__main__":

	data = np.zeros((10,20)).astype(int)

	grid_df = pd.DataFrame(data)
	# grid_df = grid_df.pivot(index="Row", columns="Column", values="data_points")

	plt.figure(figsize=(25, 10))
	map_img = mpimg.imread('./img/lll_grid.png')
	heatmap = sns.heatmap(grid_df, linewidths=1, cmap="Reds", annot=True, fmt="d", alpha=0.8, zorder=2)
	heatmap.imshow(map_img, aspect=heatmap.get_aspect(), extent=heatmap.get_xlim()+heatmap.get_ylim(), zorder=1)
	plt.title(f"LinkLab Heatmap")
	plt.show()
	# df = pd.read_csv("book_with_grids.csv")
	# for i in range(20):
	# 	GRID[i//10][i%10] += 1
	# 	print(GRID)

	# fields = []
	# for element in df.itertuples():
	# 	lst = (element[6].split(','))
	# 	for element in lst:
	# 		if element not in fields:
	# 			fields.append(element)
	# print(fields)
		# for idx, field in enumerate(all_fields):
		# 	print(idx)
		# 	print(field)

	# lst = ['Illumination_lx', 'Range select', 'Supply voltage_V', 
	# 'rssi', 'Humidity_%', 'Temperature_°C', 'awair_score', 'co2_ppm', 
	# 'pm2.5_μg/m3', 'voc_ppb', 'T-Sensor', 'PIR Status', 'Supply voltage (OPTIONAL)_V', 
	# 'Supply voltage availability', 'Contact', 'Concentration_ppm', 'H-Sensor']