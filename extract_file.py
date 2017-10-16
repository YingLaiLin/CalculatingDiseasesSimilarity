# -*- coding=utf-8 -*-
import pandas as pd

# cols=['Interaction_A(Entrez Gene_ID)',	'Interaction_B(Entrez Gene_ID)']
df = pd.read_csv('GraphData/DataS1_interactome.tsv', delim_whitespace=True, usecols=[0, 1])
query_cols = df.keys()
id_set = set()
for gene_id in df[query_cols[0]]:
    id_set.add(gene_id)
for gene_id in df[query_cols[1]]:
    id_set.add(gene_id)
print len(id_set)
print len(df)
df.to_csv('GraphData/TaskData.txt', sep=' ', index=False)

##

# gene2disease = pd.read_csv('GraphData/gene2disease.txt', delim_whitespace=True, usecols=[0, 1])
# print gene2disease
# mim2entrez = pd.read_csv('GraphData/MIM2Entrez.txt', delim_whitespace=True, usecols=[0, 2])
# print mim2entrez
# df = pd.merge(mim2entrez, gene2disease, how='inner', on='MIM_Number')
# for row in df:
#     if pd.isnull(row[2]) or pd.isnull(row[1]):
#         del row
#
# df.to_csv('GraphData/entrez2disease.txt', sep='\t', index=False)
