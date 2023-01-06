import tabix

#test = tabix.open("/home/kieron/Documents/gnomad.genomes.r3.0.1.coverage.summary.tsv.gz")

#records = test.query("chr1", 100009, 100010)

#for record in records:
	#print(record)

#genome = tabix.open("/home/kieron/Pipelines/variant_filtering_app/variant_filtering/tests/test_data/vcfs/test38.norm.anno.vcf.bgz")

#genes = genome.query("chr22", 15820079, 15820080)

#for gene in genes:
	#print(gene)


#test = tabix.open("/home/kieron/Downloads/gnomad.genomes.v3.1.2.sites.chr22.vcf.bgz")

#records = test.query("chr22", 15820079, 15820080)

#for record in records:
	#print(record)

'''
----------------------------------------------------------------------------------------------------------
'''
annotations = "nhomalt_non_topmed_ami_XX=0;AC_ami_XY=0;AN_ami_XY=428;AF_ami_XY=0.00000;nhomalt_ami_XY=0;AC_oth_XX=0;AN_oth_XX=998;AF_oth_XX=0.00000;nhomalt_oth_XX=0;AC_non_cancer_eas=0;AN_non_cancer_eas=4778;AF_non_cancer_eas=0.00000;nhomalt_non_cancer_eas=0;AC_non_topmed_XY=1;AN_non_topmed_XY=46418;AF_non_topmed_XY=2.15434e-05"

string = "nhomalt_non_topmed_ami_XX=", "AN_ami_XY=", "nhomalt_ami_XY=", "AF_oth_XX=", "AN_non_cancer_eas=", "AC="

new_anno = annotations.split(";")
#print(new_anno)

list2 = []

dict = {}

for i in string:
	for anno in new_anno:
		if i in anno:
			split = anno.split("=")

			dict[split[0]] = split[1]
		if i not in anno:
			split = i.replace("=", "")

			dict[split] = 123


print(dict)




#print(new_anno)
print(list2)

#for x in list2:

	#split = x.split("=")

	#dict[split[0]] = split[1]

#print(dict)
