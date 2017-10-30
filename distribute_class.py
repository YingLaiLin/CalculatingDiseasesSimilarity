import pandas as pd
import numpy as np
df = pd.read_csv('GraphData/DataS2_disease_genes.tsv', sep='\t', usecols=[0, 4, 5])
index = 0
pair = dict()
for row, rowSeries in df.iterrows():

    # print 'row: %s rowSeries %s' % (row,rowSeries)
    if not pd.isnull(rowSeries[1]):
        for gene_id in rowSeries[1].split(';'):

            if gene_id == ';':
                continue
            if gene_id in pair:
                pair[gene_id].append(row)

            else:

                pair[gene_id] = [row]

    if not pd.isnull(rowSeries[2]):
        for gene_id in rowSeries[2].split(';'):
            if gene_id == ';':
                continue
            if gene_id in pair:
                if gene_id != ';':
                    pair[gene_id].append(row)

            else:
                pair[gene_id] = [row]
# print pair
# s = pd.Series(pair)
# print s
# s.to_csv('GraphData/TaskData_group.txt', sep='\t')
with open('GraphData/TaskData_group.txt1', 'w') as out:
    for key in pair.keys():
        out.write(key)
        out.write(' : ')
        nums = pair[key]
        for index in range(len(nums)):
            if index:
                out.write(' ')
            print str(nums[index]),
            out.write(str(nums[index]))

        out.write('\n')