import tabix 
import re

ref = "AG"
alt = "A"

genome = tabix.open("/home/kieron/Downloads/gnomad.genomes.v3.1.2.sites.chr22.vcf.bgz")

genes = genome.query("chr22", 15528124, 15528125)

geno = []

for g in genes:
	geno = g

#print(geno)

exome = tabix.open("/home/kieron/Downloads/gnomad.exomes.r2.1.1.sites.22.liftover_grch38.vcf.bgz")

exo = exome.query("chr22", 15528124, 15528125)

ex = []

for e in exo:
	ex = e

both = [geno, ex]


#print(both)
sign = "="
dict1 = {}
seven = []

for b in both:
	if b[3] == ref and b[4] == alt:

		b = b[7:]

print(b)






#print(g)
#print(e)

		


#print(dict1)
#print(seven)






#print(anno)









#if geno[3] == ref and geno[4] == alt:

#	genoinfo = geno[7]

#if ex[3] == ref and ex[4] == alt:

#	exinfo = ex[7]
#else:
#	break


#print(genoinfo)
#print(exinfo)
#print(anno)