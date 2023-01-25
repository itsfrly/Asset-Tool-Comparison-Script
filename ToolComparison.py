import pandas as pd
import numpy as np

#read asset list from csv
assetList = pd.read_csv('assetList.csv', names="Host,Tool,MissingWhich".split(","))

tool1 = input("Enter the name of the first tool exactly as it appears in the CSV: ")
tool2 = input("Enter the name of the second tool exactly as it appears in the CSV: ")

#Check host column for duplicate values. If there are duplicates, set missing which to none and delete the duplicate. If there are no duplicates and tool == Insight IDR, set missing which to SentinelOne. If there are no duplicates and tool == SentinelOne, set missing which to Insight IDR.
assetList['MissingWhich'] = np.where(assetList.duplicated(subset='Host', keep=False), 'None', np.where(assetList['Tool'] == tool1, tool2, tool1))

#delete the duplicate.
assetList = assetList.drop_duplicates(subset='Host', keep='first')

#write updated asset list to csv
assetList.to_csv('assetListCompleted.csv', index=False)