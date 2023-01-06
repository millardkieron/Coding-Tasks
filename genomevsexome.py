import tabix 
import re

ref = "AG"
alt = "A"

filter_list = "AC" ,"AF_popmax", "nhomalt_controls_and_biobanks", "AF", "AS_FS"

genome = tabix.open("/home/kieron/Downloads/gnomad.genomes.v3.1.2.sites.chr22.vcf.bgz")

genes = genome.query("chr22", 15528124, 15528125)

geno = ()

for g in genes:
	geno = g

#print(geno)

exome = tabix.open("/home/kieron/Downloads/gnomad.exomes.r2.1.1.sites.22.liftover_grch38.vcf.bgz")

exo = exome.query("chr22", 15528125, 15528125)

ex = ()

for e in exo:
	ex = e


sign = "="
gdict = {}
edict = {}
glist = []
elist = []

if len(geno) > 0:
	if geno[3] == ref and geno[4] == alt:

		geno = geno[7]

	geno = geno.split(";")


if len(ex) > 0: 

	if ex[3] == ref and ex[4] == alt:

		ex = ex[7]
	ex = ex.split(";")

for g in geno:
	if sign in g:
		entry = g.split("=")

		gdict[entry[0]] = entry[1]

for e in ex:
	if sign in e:
		entry = e.split("=")

		edict[entry[0]] = entry[1]


for filt in filter_list:

	geno_anno = gdict.get(filt, 'NA')

	exo_anno = edict.get(filt, "NA")

	glist.append(geno_anno)

	elist.append(exo_anno)

print(glist)
print(elist)