#!/usr/bin/env Rscript
.libPaths(c("/home/kschlum/software/R_lib", .libPaths()))
library("NMF")
library("vegan")
source("https://bioconductor.org/biocLite.R")
biocLite()
nmf.options(shared.memory=FALSE)
setwd("/data1/compbio/kschlum/ecoli/asaph_out/test_case_1")
geneCounts <- as.matrix(read.csv(file = "/data1/compbio/kschlum/ecoli/asaph_out/test_case_1/testCase_1.csv" ,  row.names=NULL, header = FALSE, sep=","))
zeroRemovedGeneCounts<- geneCounts[which(rowSums(geneCounts) > 0),]

res <- nmf(zeroRemovedGeneCounts,3, method="nsNMF")
featuresProb <- predict(res, what = "features", prob = TRUE)
samplesProb <- predict(res, what = "samples", prob = TRUE)
write.csv(featuresProb,  "featuresProb_testCase1_k_3.csv", quote = FALSE)
write.csv(samplesProb,  "samplesProb_testCase1_k_3.csv",  quote = FALSE)
w <- basis(res)
write.csv(w, "w_mat_k_3_testCase1_k_3.csv", quote=FALSE)
