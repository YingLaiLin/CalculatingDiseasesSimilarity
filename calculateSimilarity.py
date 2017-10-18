# coding=utf-8
import scipy.io as sio
import pandas as pd
import numpy as np
import time
diseaseVectors = sio.loadmat('embeddingResult/disease_result.mat')
diseaseVectors = diseaseVectors['embedding']

'''
    计算两个向量之间的欧式距离
'''


def cal_similarity(vector, vector1):
    vl = len(vector)
    if vl != len(vector1):
        raise Exception('传入的两个向量长度不相等')
    distance = 0.0
    for index in range(vl):
        distance += (vector[index] - vector1[index]) ** 2
    return distance


''' 
    读取疾病与向量的关系
'''
print 'load data'
diseaseInfo = {}
pre = time.time()
with open('GraphData/Task_class.txt') as read:
    profile = read.readline()
    profile = profile.split(' ')
    vectorNumbers = profile[0]
    diseaseNumbers = profile[1]
    line = read.readline()
    while line:
        line = line.split(' : ')
        diseaseId = int(line[0])
        vectorId = line[1].split(' ')
        vectorId = [IdStr.replace('\n', '') for IdStr in vectorId]
        vectorId = [int(strID) for strID in vectorId]
        diseaseInfo[diseaseId] = vectorId
        line = read.readline()
post = time.time()
print 'cost: ', str(post-pre) +'s'
print 'calculating distances between vectors'
'''
    预先计算所有向量之间的距离
'''
distances = {}

print diseaseVectors
for diseaseId in range(len(diseaseVectors)):
    curDisease = diseaseVectors[diseaseId]

    pre = time.time()
    for secondDiseaseId in range(len(diseaseVectors)):
        if diseaseId < secondDiseaseId:
            distance = cal_similarity(curDisease, diseaseVectors[secondDiseaseId])
        else:
            distance = 0.0
        if diseaseId in distances:
            distances[diseaseId].append(distance)
        else:
            distances[diseaseId] = [distance]
    post = time.time()
    print 'cur: ', str(diseaseId), ' cost: ', str(post - pre),'s'
df = pd.DataFrame(distances)
df.to_csv('CalculatedResult/distance.csv', sep=',', index=False)

'''
    计算疾病相似性得分
'''
print 'calculating scores between disease'
diseaseScores = {}
distances = np.zeros((20000,20000))
print distances
for diseaseId in diseaseInfo:
    curDisease = diseaseInfo[diseaseId]
    print 'calculating {0}'.format(diseaseId), curDisease
    for secondDiseaseId in diseaseInfo:
        if secondDiseaseId > diseaseId:
            secondDisease = diseaseInfo[secondDiseaseId]
            print secondDisease
            score = 0
            for vid in curDisease:
                for svid in secondDisease:
                    if svid < vid:
                        score += distances[svid][vid]
                    else:
                        score += distances[vid][svid]

        else:
            score = 0.0
        if diseaseId in diseaseScores:
            diseaseScores[diseaseId].append(score)
        else:
            diseaseScores[diseaseId] = [score]
df = pd.DataFrame(diseaseScores)
df.to_csv('CalculatedResult/scores.csv', sep=',', index=False)
