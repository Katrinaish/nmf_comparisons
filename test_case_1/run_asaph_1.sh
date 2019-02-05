python /data1/compbio/kschlum/ecoli/asaph_out/scripts/generate_dummy_vcf_noHeader.py /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/testCase_1.csv /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/test_case_1.vcf 20

python /data1/compbio/kschlum/software/asaph_py2/asaph/asaph/import.py --feature-type categories --vcf /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/test_case_1.vcf --populations /data1/compbio/kschlum/ecoli/asaph_out/labels_ecoli_asaph_test.csv --workdir /data1/compbio/kschlum/ecoli/asaph_out/test_case_1

python /data1/compbio/kschlum/software/asaph_py2/asaph/asaph/pca.py --workdir /data1/compbio/kschlum/ecoli/asaph_out/test_case_1 train --n-components 9

python /data1/compbio/kschlum/software/asaph_py2/asaph/asaph/pca.py --workdir /data1/compbio/kschlum/ecoli/asaph_out/test_case_1 snp-association-tests --components 1 2 3 4 --model-type logistic

python /data1/compbio/kschlum/software/asaph_py2/asaph/utils/sig_test_snps.py --input /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/analysis/snp_pc_1_logreg_assoc_tests.tsv --output /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/analysis/snp_pc_1_logreg_assoc_tests.sig_01.tsv --significance 0.01

python /data1/compbio/kschlum/software/asaph_py2/asaph/utils/sig_test_snps.py --input /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/analysis/snp_pc_1_logreg_assoc_tests.tsv --output /data1/compbio/kschlum/ecoli/asaph_out/test_case_1/analysis/snp_pc_1_logreg_assoc_tests.sig_003.tsv --significance 0.003
