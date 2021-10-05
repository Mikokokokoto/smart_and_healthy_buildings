import pandas as pd
import utility as util
from datetime import datetime
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt, image as mpimg

GRID = np.zeros((10,20)).astype(int)



def check_fields(fields, all_fields):
	for idx, field in enumerate(all_fields):
		if field in fields:
			return True, idx
	return False, idx

def generate_linklab_heatmap(start_datetime, end_datetime
, fields, export_filepath):
	df = pd.read_csv("book_with_grids.csv")

	for n in range(200):
		all_fields = df[df['grid']==n]['fields']
		
		if len(all_fields) != 0:
			field_lst = all_fields.values[0].split(',')
			condition, param_index = check_fields(fields, field_lst)
			if condition:
				parameter = field_lst[param_index]
				entry = util.get_lfdf(parameter, start_datetime, end_datetime, list(df[df['grid']==n]['device_id']))
				if isinstance(entry, pd.DataFrame):
					entry_num = len(entry)
					GRID[n//20][n%20] += entry_num

	data = pd.DataFrame(GRID)
	plt.figure(figsize=(30, 10))
	map_img = mpimg.imread('./img/lll_grid.png')
	heatmap = sns.heatmap(data, linewidths=1, cmap="Reds", annot=True, fmt="d", alpha=0.8, zorder=2)
	# heatmap = sns.heatmap(data, linewidths=1, cmap="Reds", annot=True, cbar=True, fmt="d", zorder=2)
	heatmap.imshow(map_img, aspect=heatmap.get_aspect(), extent=heatmap.get_xlim()+heatmap.get_ylim(), zorder=1)
	# heatmap.imshow(map_img, aspect=heatmap.get_aspect(), extent=heatmap.get_xlim()+heatmap.get_ylim())
	plt.title('Heatmap')
	
	filepath = f"{export_filepath}/heatmap.png"
	plt.savefig(filepath)
	return filepath





if __name__ == "__main__":
	s= datetime(2021,1,1) # start datetime
	e= datetime(2021,9,23) # end datetime

	fields = ['Illumination_lx', 'Range select', 'Supply voltage_V', 
	'rssi', 'Humidity_%', 'Temperature_°C', 'awair_score', 'co2_ppm', 
	'pm2.5_μg/m3', 'voc_ppb', 'T-Sensor', 'PIR Status', 'Supply voltage (OPTIONAL)_V', 
	'Supply voltage availability', 'Contact', 'Concentration_ppm', 'H-Sensor']

	generate_linklab_heatmap(s, e, fields, './img')

	print(GRID)
	