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



#generate where genes present in both groups
starterMatrix = generateMatrix(300, 100)
secondMatrix = testFeatMatSetup(0, 20, 0,25, starterMatrix, 1)
thirdMatrix = testFeatMatSetup(0, 20, 75,100, secondMatrix, 1)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_1/" , "matrix_1.csv", thirdMatrix)


#generate where only present in group 1

starterMatrix = generateMatrix(300, 50)
secondMatrix = testFeatMatSetup(0, 20, 0,25, starterMatrix, 1)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_2/" , "matrix_2.csv", secondMatrix)
#
#
#
#
##generate where only present in group 2
#
#
starterMatrix = generateMatrix(300, 50)
secondMatrix = testFeatMatSetup(0, 20, 25,50, starterMatrix, 1)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_3/" , "matrix_3.csv", secondMatrix)


#
##generate where genes absent in both groups
#
#
#
starterMatrix = generateMatrix(300, 100)
secondMatrix = testFeatMatSetup(0, 20, 0,25, starterMatrix, 0)
thirdMatrix = testFeatMatSetup(0, 20, 75,100, secondMatrix, 0)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_4/" , "matrix_4.csv", thirdMatrix)
#
#
##generate where only absent in group 1
#
#
starterMatrix = generateMatrix(300, 50)
secondMatrix = testFeatMatSetup(0, 20, 0,25, starterMatrix, 0)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_5/" , "matrix_5.csv", secondMatrix)


#
#
##generate where only absent in group 2
#
#
starterMatrix = generateMatrix(300, 50)
secondMatrix = testFeatMatSetup(0, 20, 25,50, starterMatrix, 0)
saveMatrix("/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_6/" , "matrix_6.csv", secondMatrix)

