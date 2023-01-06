import tabix 
import re

genome = tabix.open("/home/kieron/Downloads/gnomad.genomes.v3.1.2.sites.chr22.vcf.bgz")

genes = genome.query("chr22", 15528124, 15528125) #genes = genome.query("chr22", 10510066, 10510077) 

for g in genes:

	print(g) 

#print("Hello World")

exome = tabix.open("/home/kieron/Downloads/gnomad.exomes.r2.1.1.sites.22.liftover_grch38.vcf.bgz")

chrom = 1

exo = exome.query("chr22", 15528124, 15528125) 

for e in exo:
	print(e)


ref = "AG" #C
alt = "A" #A


filter_list = "AC" ,"AF_popmax", "nhomalt_controls_and_biobanks", "AF", "AS_FS"

newdict = {}
sign = "="

final_list = []

total_dict = {}
hostile = ()

for info in genes:
	if info[3] == ref and info[4] == alt:

		gnomad_anno = info[7]

		new_anno = gnomad_anno.split(";")


		for anno in new_anno:
			if sign in anno:

				entry = anno.split("=")

				newdict[entry[0]] = entry[1]



		for filt in filter_list:
			annotations = newdict.get(filt, f'NA')

			final_list.append(annotations)


#print(zipper)
print(final_list)
#print(total_dict)

























coverage = tabix.open("/home/kieron/Documents/gnomad.genomes.r3.0.1.coverage.summary.tsv.gz")

work = coverage.query("chr22", 10510076, 10510077)

for i in work:
	entry = i


#print(entry)


#if "AF=0.00000" in newlist and float(entry[7]) > 0:
#	print(True)
#else:
#	print(False)

'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''
#annotations = "nhomalt_non_topmed_ami_XX=0;AC_ami_XY=0;AN_ami_XY=428;AF_ami_XY=0.00000;nhomalt_ami_XY=0;AC_oth_XX=0;AN_oth_XX=998;AF_oth_XX=0.00000;nhomalt_oth_XX=0;AC_non_cancer_eas=0;AN_non_cancer_eas=4778;AF_non_cancer_eas=0.00000;nhomalt_non_cancer_eas=0;AC_non_topmed_XY=1;AN_non_topmed_XY=46418;AF_non_topmed_XY=2.15434e-05"

#string = "nhomalt_non_topmed_ami_XX=", "AN_ami_XY=", "nhomalt_ami_XY=", "AF_oth_XX=", "AN_non_cancer_eas="

#new_anno = annotations.split(";")
#print(new_anno)

#list2 = []

#for i in string:
#	for anno in new_anno:
#		if i in anno:
#			list2.append(anno)
#



#print(new_anno)
#print(list2)
