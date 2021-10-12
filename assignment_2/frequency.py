import pandas as pd
import utility as util
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt

if __name__ == "__main__":

    # d = {'1':0, "2":3}
    # d['5'] = 3
    # print(d)    

    d = {}

    s = datetime(2021,9,20)
    e = datetime(2021,9,23)
    df = pd.read_csv("book_with_grids.csv")
    grids = [80, 81, 82, 83, 84, 85, 100, 101, 102, 103, 104, 105]

    for grid in grids:
        fields = []
        locations = df[df['grid']==grid]
        for row in locations.iterrows():
            lst = row[1].fields.split(',')
            for element in lst:
                if element not in fields:
                    fields.append(element)
        count = 0
        for field in fields:
            ldf = util.get_lfdf(field, s, e, list(df[df['grid']==grid]['device_id']))
            count += len(ldf)

        d[str(grid)] = count
        
    stats = pd.Series(data=d)
    stats.plot(kind='bar', xlabel='grids', ylabel='count')
    
    export_filepath = './img'
    filepath = f"{export_filepath}/frequency.png"
    plt.savefig(filepath)