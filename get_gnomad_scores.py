import tabix
import re

self.variants, self.gnomad_genome_path, self.gnomad_exome_path



filter_list = "AC" ,"AF_popmax", "nhomalt_controls_and_biobanks", "AF", "AS_FS"

sign = "="
gnomad_dict = {}
values = []

for variant in variants:
	chrom = variants[variant]['chrom']
	pos = variants[variant]['pos']
	ref = variants[variant]['ref']
	alt = variants[variant]['alt']

	exo_chrom = re.findall(r'\d+', chrom)


	genome = tabix.open(gnomad_genome_path)
	exome = tabix.open(gnomad_exome_path)

	genome_info = genome.query(chrom, pos-1, pos)
	exome_info = exome.query(exo_chrom, pos-1, pos)

	for info in genome_info:

		if info[3] == ref and info[4] == alt:

			genome_anno = info[7]
			genome_anno = genome_anno.split(";")

			for anno in genome_anno:

				if sign in anno:

					entry = anno.split("=")

					genome_dict[entry[0]] = entry[1]

	for info in exome_info:

		if info[3] == ref and info[4] == alt:

			exome_anno = info[7]
			exome_anno = exome_anno.split(";")

			for anno in exome_anno:

				if sign in anno:

					entry = anno.split("=")

					exome_dict[entry[0]] = entry[1]

