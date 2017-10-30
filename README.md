# 计算疾病之间的相似性
- 这是一个基于 SDNE 进行疾病相似性计算的项目
- 如需要使用, 请务必遵守 SDNE 的要求.
## 文件说明
### 数据说明
#### 来自疾病网络论文
- 如需使用, 请遵守疾病网络这篇论文的要求. 不过好像没有.
- DataS1-interactome.txt 描述基因之间的关系
- DataS2-disease_genes.txt 描述与疾病相关联的基因, 这些基因来自 
    OMIM 和 GWAS 的基因.
#### 其他来源
- TaskData.txt  抽取 DataS1 中的数据, 只保留基因作用对. 
- TaskData_group.txt 读取 DataS2 中的数据, 保存疾病与基因之间的关系, 其中疾病的 ID 由其在数据中出现的行数索引给出
- Map.txt  geneID 离散化为连续值后的 TaskData.txt, 因为 SDNE 只能处理连续值.
- Task_group.txt 将 geneID 离散化为连续值的 TaskData_group.txt, 原因同上.
- Task_class.txt 存储疾病与基因的关系, 形式为 disease_id : gene_id1, gene_id2, ..., gene_idn
### 功能文件说明
- extract_file.py 见 TaskData.txt
- distribute_class.py 见 TaskData_group.txt
- discrete.py 见 Map.txt 和 Task_group.txt
- node2class.py 见 Task_class.txt

## TO DO
- 整合文件或者聚合文件, 方便使用.
- distribute_class.py 中没有区别 GWAS 和 OMIM 基因, 需要分为两个基因集合进行计算.
### SDNE
This repository provides a reference implementation of *SDNE* as described in the paper:<br>
> Structural Deep network Embedding.<br>
> Daixin Wang, Peng Cui, Wenwu Zhu<br>
> Knowledge Discovery and Data Mining, 2016.<br>
> <Insert paper link>

The *SDNE* algorithm learns a representations for nodes in a graph. Please check the [paper](http://www.kdd.org/kdd2016/subtopic/view/structural-deep-network-embedding) for more details. 

#### Basic Usage
```
$ python main.py
```
After execute the above command, You will get a embedding file named "xxx_embedding.mat"
>noted: your can just checkout and modify config.py or main.py to get what you want.
#### Input
Your input graph data should be a **txt** file and be under **GraphData folder** 
##### file format
the txt file should be **edgelist** and **the first line** should be **N** , the number of vertexes and **E**, the number of edges
##### A sample
	5242 14496
	0 1
	0 2
	4 9
	...
	4525 4526

> noted: The nodeID start from 0.<br>
> noted: The graph should be an undirected graph, so if (I  J) exist in the Input file, (J  I) should not.
#### Citing
If you find *SDNE* useful in your research, we ask that you cite the following paper:

	@inproceedings{Wang:2016:SDN:2939672.2939753,
	 author = {Wang, Daixin and Cui, Peng and Zhu, Wenwu},
	 title = {Structural Deep Network Embedding},
	 booktitle = {Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
	 series = {KDD '16},
	 year = {2016},
	 isbn = {978-1-4503-4232-2},
	 location = {San Francisco, California, USA},
	 pages = {1225--1234},
	 numpages = {10},
	 url = {http://doi.acm.org/10.1145/2939672.2939753},
	 doi = {10.1145/2939672.2939753},
	 acmid = {2939753},
	 publisher = {ACM},
	 address = {New York, NY, USA},
	 keywords = {deep learning, network analysis, network embedding},
	} 



