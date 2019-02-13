#!/usr/bin/python
#title			:generate_simulated_matrix_.py
#description	:given use cases for testing NMF vs asaph, generate simulated matrix of absent or present
#author			:kschlum
#date			:20190121
#version		:1.0
#usage			:python generate_simulated_matrix_.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import numpy as np
from random import random
from random import randint


def generateMatrix(n_feat, n_samples):
    mat = np.empty([n_feat,n_samples], dtype=np.int)
    for x in range(0, n_feat):
        for y in range(0, n_samples):
            rand = np.random.uniform(0,1)
            if rand > 0.90:
                mat[x, y] = 1
            else:
                mat[x, y ] = 0
    return mat



def testFeatMatSetup(startTestFeat, endTestFeat, startGroup, endGroup, matrix, testVal):
    total_groups = endGroup - startGroup
    matrix[startTestFeat:endTestFeat, startGroup:endGroup] = [testVal]*total_groups

    return matrix



def saveMatrix(saveDir, fileName, matrix):
    np.savetxt(saveDir + fileName, matrix, delimiter=",", fmt = '%d')


#initialize matrix
starterMatrix = generateMatrix(400, 100)

#generate where genes present in both groups
secondMatrix = testFeatMatSetup(0, 50, 0, 100, starterMatrix, 0)

#generate where genes present in absent groups
thirdMatrix = testFeatMatSetup(50, 100, 0, 100, secondMatrix, 1)

#generate where genes present in group 1
fourthMatrix = testFeatMatSetup(100, 150, 0, 50, thirdMatrix, 1)
fifthMatrix = testFeatMatSetup(100, 150, 50, 100, fourthMatrix, 0)

#generate where genes present in group 2
sixthMatrix = testFeatMatSetup(150, 200, 0, 50, fifthMatrix, 0)
seventhMatrix = testFeatMatSetup(150, 200, 50, 100, sixthMatrix, 1)


saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/" , "matrix_all_comparision_test_case_1.csv", seventhMatrix)




#test case 2 - where 200 features but same setupa as test case 1 

starterMatrix = generateMatrix(200, 100)

#generate where genes present in both groups
secondMatrix = testFeatMatSetup(0, 50, 0, 100, starterMatrix, 0)

#generate where genes present in absent groups
thirdMatrix = testFeatMatSetup(50, 100, 0, 100, secondMatrix, 1)

#generate where genes present in group 1
fourthMatrix = testFeatMatSetup(100, 150, 0, 50, thirdMatrix, 1)
fifthMatrix = testFeatMatSetup(100, 150, 50, 100, fourthMatrix, 0)

#generate where genes present in group 2
sixthMatrix = testFeatMatSetup(150, 200, 0, 50, fifthMatrix, 0)
seventhMatrix = testFeatMatSetup(150, 200, 50, 100, sixthMatrix, 1)


saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/" , "matrix_all_comparision_test_case_2.csv", seventhMatrix)


#test case 3 - where 200 features but random features in complementary group that is not being tested  
