#manhattan plot visualization


library(qqman)

snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)


snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("//Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)


snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("//Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)


colnames(snp1) <- c("SNP", "BP", "P")
snp1$CHR <- rep(1,nrow(snp1))
manhattan(snp1)
title(main = "PC1")


colnames(snp2) <- c("SNP", "BP", "P")
snp2$CHR <- rep(1,nrow(snp2))
manhattan(snp2)
title(main = "PC2")




colnames(snp3) <- c("SNP", "BP", "P")
snp3$CHR <- rep(1,nrow(snp3))
manhattan(snp3)
title(main = "PC3")






colnames(snp4) <- c("SNP", "BP", "P")
snp4$CHR <- rep(1,nrow(snp4))
manhattan(snp4)
title(main = "PC4")



#visualize NMF results for asaph
snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/nmf/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/nmf/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/nmf/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/nmf/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)


snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/nmf/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/nmf/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("//Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/nmf/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/nmf/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)


snp1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/nmf/snp_pc_1_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/nmf/snp_pc_2_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp3 <- read.table("//Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/nmf/snp_pc_3_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)
snp4 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/nmf/snp_pc_4_logreg_assoc_tests.tsv", sep = "\t", header = FALSE)




colnames(snp1) <- c("SNP", "BP", "P")
snp1$CHR <- rep(1,nrow(snp1))
manhattan(snp1)
title(main = "PC1")


colnames(snp2) <- c("SNP", "BP", "P")
snp2$CHR <- rep(1,nrow(snp2))
manhattan(snp2)
title(main = "PC2")




colnames(snp3) <- c("SNP", "BP", "P")
snp3$CHR <- rep(1,nrow(snp3))
manhattan(snp3)
title(main = "PC3")




#visualize NMF results


nmf1 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present/featuresProb_ecoli_k_2_testCase_0.csv", sep = ",", header = TRUE)
nmf2 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_2/featuresProb_ecoli_k_2_testCase_2.csv", sep = ",", header = TRUE)
nmf3 <- read.table("/Users/kat/work/asaph_vs_nmf/ecoli/test_cases_absent_present_3/featuresProb_ecoli_k_2_testCase_3.csv", sep = ",", header = TRUE)

nmf_1_subset <- nmf1[c("X", "prob")]


colnames(nmf_1_subset) <- c( "BP", "P")
nmf_1_subset$CHR <- rep(1,nrow(nmf_1_subset))
nmf_1_subset$SNP <- rep(0,nrow(nmf_1_subset))

nmf_1_subset$BP <- nmf_1_subset$BP + 50
plot(nmf_1_subset$BP, nmf_1_subset$P)
title(main = "nmf_1_subset")


nmf_2_subset <- nmf2[c("X", "prob")]

colnames(nmf_2_subset) <- c( "BP", "P")
nmf_2_subset$CHR <- rep(1,nrow(nmf_2_subset))
nmf_2_subset$SNP <- rep(0,nrow(nmf_2_subset))
nmf_2_subset$BP <- nmf_2_subset$BP + 50

plot( nmf_2_subset$BP,nmf_2_subset$P)
title(main = "nmf_2_subset")




nmf_3_subset <- nmf3[c("X", "prob")]

colnames(nmf_3_subset) <- c( "BP", "P")
nmf_3_subset$CHR <- rep(1,nrow(nmf_3_subset))
nmf_3_subset$SNP <- rep(0,nrow(nmf_3_subset))
nmf_3_subset$BP <- nmf_3_subset$BP + 50
plot( nmf_3_subset$BP,nmf_3_subset$P)
title(main = "nmf_3_subset")


