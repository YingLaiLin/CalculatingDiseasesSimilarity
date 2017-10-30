#! codeing=utf-8
import pandas as pd
import time

print('load data')
df = pd.read_csv('CalculatedResult/simscores.csv')
scores = df.to_dict()
print df.info()
keys = scores.keys()
length = len(keys)
for index in range(length):
    for sindex in range(0, index):
        scores[str(sindex)][index] = scores[str(index)][sindex]
complete_score = {}
for key in keys:
    data = scores[key]
    complete_score[int(key)] = data
res = pd.DataFrame(complete_score)
res.to_csv('CalculatedResult/sim_scores_complete.csv', sep=',', index=False)
print res.info()
