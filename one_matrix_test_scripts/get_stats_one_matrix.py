#!/usr/bin/python
#title			:get_stats_of_nmf_vs_asaph.py
#description	:given NMF results and asaph results, generate stats
#author			:kschlum
#date			:20190203
#version		:1.0
#usage			:python get_stats_of_nmf_vs_asaph.py
#notes			:
#python_version	:2.6.6
#==============================================================================
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def generate_exp_results(testCaseFile, testCaseNum, totalFeat):
    """
        generate_exp_results(): description
            This generates an expected list of results for all features found in each test case

        Args:
            testCaseFile (file): The file where testcase metadata is located
            testCaseNum (int): the test case number *also found in first index of testCaseFile
            totalFeat (int): the total number of features in matrix

        Returns:
        expResults (list): length of totalFeat where 1 if feature being tested for and 0 if feature is not tested for significant
    """
    expResults = []
#    expResults = [0]*
    with open(testCaseFile, 'r') as exp:
        for f in exp.readlines()[1:]:
            fSplit = f.split(",")
            if int(fSplit[0].strip()) == testCaseNum:
                vals = range(int(fSplit[4].strip()), int(fSplit[5].strip())) 
                for v in vals:
                    expResults[int(v)] = 1

    return expResults




def generate_nmf_observed_vals(testCaseNum, totalFeat, fileDir, fileName, nmfCutOff, testing):
    """
        generate_nmf_observed_vals(): description
            This generates an observed list of values based on nmfCutoff supplied and logic
            table

        logic:

                # +----------------------------------+-------+
                # | test    |  sig value  | signif. | obs    |
                  |         |             | sign    | value  |
                # +---------+-------------+---------+--------+
                # | absent  |  nmfCutOff  | <=      |    1   |
                # | present |  nmfCutOff  | >=      |    1   |
                # +-----------------------+---------+--------+


        Args: testCaseNum (int): The test case number *also found in first index of testCaseFile
              totalFeat (int): the total number of features in matrix
              fileDir(filePath): path where test case located
              fileName(fileName): name of feature Prob file 
              nmfCutOff (int): the cutoff probablitity NMF value
              testing (str): if testing for prseent or absent
        Returns:
            observedNMFResults(list): list of observed values for testCaseNum evaluating
    """
    observedNMFResults = [0]*totalFeat
    with open(fileDir + "/" + fileName) as nmfFile:
        for n in nmfFile.readlines()[1:]:
            nSplit = n.split(",")
            if testing == "present":
                if float(nSplit[2].strip()) >= nmfCutOff:
                    observedNMFResults[int(nSplit[0].strip())-1] = 1
            elif testing == "absent":
                if float(nSplit[2].strip()) <= nmfCutOff:
                    observedNMFResults[int(nSplit[0].strip())-1] = 1

    return observedNMFResults


def generate_asaph_observed_vals(testCaseNum, totalFeat, fileDir, pc_comp_file, asaphCutOff, testing): 
    """

        generate_asaph_observed_vals(): description
        generate asaph observed values based on asahCutoff supplied and logic table

        logic:
                # +----------------------------------+---------+
                # | test    |  sig value    | signif. | obs    |
                  |         |               | sign    | value  |
                # +---------+---------------+---------+--------+
                # | absent  |  asaphCutOff  | >=      |    1   |
                # | present |  asaphCutOff  | <=      |    1   |

        Args: testCaseNum (int): The test case number *also found in first index of testCaseFile
              totalFeat (int): the total number of features in matrix that are being tested for
              fileDir(filePath): path where test case located
              pc_comp_file(file): name of snp significant file output from asaph
              asaphCutOff (int): the cutoff for asaph p-value 
              testing (str): if testing for prseent or absent
        Returns:
            observedAsaphResults(list): list of observed values for testCaseNum evaluating
    """
    observedAsaphResults = [0]*totalFeat
    with open(fileDir + "/analysis/" + pc_comp_file) as asaph_one:
            for f in asaph_one.readlines():
                fSplit = f.split("\t")
                if testing == "present":
                    if float(fSplit[2].strip()) <= asaphCutOff:
                        observedAsaphResults[int(fSplit[1].strip())-1] = 1
                elif testing == "absent":
                    if float(fSplit[2].strip()) >= asaphCutOff:
                        observedAsaphResults[int(fSplit[1].strip())-1] = 1

    return observedAsaphResults


def generate_stats(expected, observed):
    """
    generate_stats(): description
    generate accuracy, precision and recall based on sklearn default functions

    return: accuracy (float)
            precison (float)
            reacal (float) 
    """
    acc = accuracy_score(expected, observed)
    prec = precision_score(expected, observed)
    recall = recall_score(expected, observed)
    return acc, prec, recall





#get expected results for test case
#testCaseFileName = "/data1/compbio/kschlum/ecoli/scripts/testCases_metadata.csv"
testCaseFileName = "/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only/testCases_metadata_asaph_only_1.csv"
exp_one = generate_exp_results(testCaseFileName, 1, 400)
exp_two = generate_exp_results(testCaseFileName, 2, 400)
exp_three = generate_exp_results(testCaseFileName, 3, 400)
exp_four = generate_exp_results(testCaseFileName, 4, 400)
#exp_five = generate_exp_results(testCaseFileName, 5, 300)
#exp_six = generate_exp_results(testCaseFileName, 6, 300)

#get NMF observed values
testCase_one_nmf_obs = generate_nmf_observed_vals(1, 400, "/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only" , "featuresProb_ecoli_k_2_testCase_0.csv", 0.7, "present")
testCase_two_nmf_obs = generate_nmf_observed_vals(2, 400, "/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only" , "featuresProb_ecoli_k_2_testCase_0.csv", 0.7, "present")
testCase_three_nmf_obs = generate_nmf_observed_vals(3, 400, "/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only" , "featuresProb_ecoli_k_2_testCase_0.csv", 0.7, "present")

testCase_four_nmf_obs = generate_nmf_observed_vals(4, 400, "/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only" , "featuresProb_ecoli_k_2_testCase_0.csv", 0.7, "present")


#get asaph observed values
testCase_one_asaph_obs = generate_asaph_observed_vals(1, 400,"/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only", "snp_pc_1_logreg_assoc_tests.tsv", 0.001, "present")
testCase_two_asaph_obs = generate_asaph_observed_vals(2, 400,"/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only", "snp_pc_1_logreg_assoc_tests.tsv", 0.001, "present")
testCase_three_asaph_obs = generate_asaph_observed_vals(3, 400,"/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only", "snp_pc_1_logreg_assoc_tests.tsv", 0.001 ,"present")
testCase_four_asaph_obs = generate_asaph_observed_vals(4, 400,"/data1/compbio/kschlum/ecoli/nmf_vs_asaph/test_case_asaph_only" , "snp_pc_1_logreg_assoc_tests.tsv", 0.001, "absent")
#testCase_five_asaph_obs = generate_asaph_observed_vals(5, 300,"/data1/compbio/kschlum/ecoli/asaph_out/test_case_", "snp_pc_1_logreg_assoc_tests.tsv", 0.001, "absent")
#testCase_six_asaph_obs = generate_asaph_observed_vals(6, 300,"/data1/compbio/kschlum/ecoli/asaph_out/test_case_", "snp_pc_1_logreg_assoc_tests.tsv", 0.001, "absent")


#get stats for expected values and observed for each NMF test case
stats_one_nmf = generate_stats(exp_one, testCase_one_nmf_obs)
stats_two_nmf = generate_stats(exp_two, testCase_two_nmf_obs)
stats_three_nmf = generate_stats(exp_three, testCase_three_nmf_obs)
stats_four_nmf = generate_stats(exp_four, testCase_four_nmf_obs)
#stats_five_nmf = generate_stats(exp_five, testCase_five_nmf_obs)
#stats_six_nmf = generate_stats(exp_six, testCase_six_nmf_obs)
#print(stats_one_nmf)
#print(exp_one, testCase_one_nmf_obs)
print("two_NMF")
print(stats_two_nmf)
print("three_NMF")
print(stats_three_nmf)
print("four_NMF")
print(stats_four_nmf)
#print(stats_five_nmf)
#print(stats_six_nmf)


#get stats for expected values and observed for each asaph test case
stats_one_asaph = generate_stats(exp_one, testCase_one_asaph_obs)
stats_two_asaph = generate_stats(exp_two, testCase_two_asaph_obs)
stats_three_asaph = generate_stats(exp_three, testCase_three_asaph_obs)
stats_four_asaph = generate_stats(exp_four, testCase_four_asaph_obs)
#stats_five_asaph = generate_stats(exp_five, testCase_five_asaph_obs)
#stats_six_asaph = generate_stats(exp_six, testCase_six_asaph_obs)


#print(stats_one_asaph)
#print(exp_one, testCase_one_asaph_obs)
#print(stats_two_asaph)
print(stats_three_asaph)
print(exp_three, testCase_three_asaph_obs)
print(stats_four_asaph)
#print(stats_five_asaph)
#print(stats_six_asaph)
