import re
import numpy as np
import pandas as pd

filename = "temp/unfiltered_websites_list.txt"
data = np.loadtxt(filename, delimiter='\n', dtype=str)
filtered = []
for i in range(len(data)):
    value = re.findall("(https://usbanksdirectory.com/routing-numbers/([^0-9]*)/)", data[i])
    if value:
        filtered.append(value[0][0])

filtered = pd.DataFrame(filtered)
filtered.to_csv("websites_list.csv")
