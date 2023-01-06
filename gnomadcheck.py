import tabix 
import re

genome = tabix.open("/home/kieron/Downloads/gnomad.genomes.v3.1.2.sites.chr22.vcf.bgz")

genes = genome.query("chr22", 10510066, 10510177) 

filter_list = "AC=" ,"AF_popmax=", "nhomalt_controls_and_biobanks=", "AF=", "AS_FS="

anno_dict = {}

anno_list = []

for g in genes:
	line = g[7]
	for l in line:
		entry = l.split("=")

		anno_dict[entry[0]] = entry[1]
		print(anno_dict)





	#new_info = new_anno.split(";")








#	for filt in filter_list:
#		for anno in new_info:
#			if filt in anno:
#				split = anno.split("=")
#
#				anno_dict[split[0]] = split[1]
#

#print(anno_dict)