diseases = dict()

with open('GraphData/Task_group.txt', 'r') as read:
    head = read.readline()
    line = read.readline()
    while line:
        gene, classes = line.split(' : ')
        gene = gene.strip()
        classes = classes.strip()
        classes = classes.split(' ')
        for class_number in classes:
            class_number = int(class_number)
            if class_number in diseases:
                diseases[class_number].append(gene)
            else:
                diseases[class_number] = [gene]
        line = read.readline()

diseases_keys = diseases.keys()
with open('GraphData/Task_class.txt', 'w') as out:
    out.write(head)
    for key in diseases_keys:
        out.write(str(key))
        out.write(' : ')
        for index in range(len(diseases[key])):
            if index:
                out.write(' ')
            out.write(str(diseases[key][index]))

        out.write('\n')
