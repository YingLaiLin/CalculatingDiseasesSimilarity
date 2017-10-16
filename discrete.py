import pandas as pd
discrete = set()
df = pd.read_csv('GraphData/TaskData.txt', delim_whitespace=True)
query_cols = df.keys()
for gene_id in df[query_cols[0]]:
    discrete.add(int(gene_id))
for gene_id in df[query_cols[1]]:
    discrete.add(int(gene_id))
output = dict()
index = 0
for key in discrete:
    output[key] = index
    index += 1
# with open ('GraphData/Map.txt','w') as out:
#     for key in output.keys():
#         out.write(str(key))
#         out.write(' ')
#         out.write(str(output[key]))
#         out.write('\n')
# with open ('GraphData/Task.txt','w') as out:
#     for row, rowSeries in df.iterrows():
#         out.write(str(output[rowSeries[0]]))
#         out.write(' ')
#         out.write(str(output[rowSeries[1]]))
#         out.write('\n')

with open ('GraphData/Task_group.txt', 'w') as out:
    with open('GraphData/TaskData_group.txt', 'r') as f:
        out.write(f.readline())
        line = f.readline()
        while line:
            print line
            head, tail = line.split(' : ')
            head = int(head)
            if not output.has_key(head):
                line = f.readline()
                continue
            out.write(str(output[head]))
            out.write(" : ")
            out.write(tail)
            line = f.readline()

