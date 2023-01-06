'''
SNPCLASSIFIER
'''

def load_gnomad_annotations(self, chrom):

	self.gnomad_genome = "/data/resources/human/gnomad/38/gnomad.genomes.v3.1.2.sites." + chrom +".vcf.bgz"

	self.gnomad_exome = gnomad_exome_path

def load_gnomad_coverage(self, gnomad_coverage_path):

	self.gnomad_coverage = gnomad_coverage_path


def add_gnomad_annotations(self):
	'''
	Add annotations from Gnomad to the self.variants dict
	'''
	if self.gnomad is None:
		raise Exception("Gnomad reference not loaded.")

	self.variants = code_utils.get_gnomad_scores(self.variants, self.gnomad)


def add_gnomad_coverage(self):
	'''
	Add coverage from Gnomad to the self.variants dict
	'''
	if self.gnomad_coverage is None:
		raise Exception("Gnomad coverage reference not loaded.")

	self.variants = code_utils.get_gnomad_coverage(self.variants, self.gnomad_coverage)

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CODE_UTILS
'''

import tabix

def get_gnomad_scores(variants, gnomad):

	filter_list = "AC" ,"AF_popmax", "nhomalt_controls_and_biobanks", "AF", "AS_FS"

	sign = "="
	gnomad_dict = {}
	values = []


	for variant in variants:

		chrom = variants[variant]['chrom']
		pos = variants[variant]['pos']
		ref = variants[variant]['ref']
		alt = variants[variant]['alt']

		gnomad = tabix.open(gnomad_file_path)

		gnomad_info = gnomad.query(chrom, pos-1, pos)

		for info in gnomad_info:

			if info[3] == ref and info[4] == alt:

				gnomad_anno = info[7]
				gnomad_anno = gnomad_anno.split(";")

				for anno in gnomad_anno:

					if sign in anno:

						entry = anno.split("=")

						gnomad_dict[entry[0]] = entry[1]


				for filt in filter_list:

					annotations = gnomad_dict.get(filt, f'NA')

					values.append(annotations)

		variants[variant]['acmg_gnomad_anno'] = values

	return variants



def get_gnomad_coverage(variants, gnomad_coverage):

	for variant in variants:

		chrom = variants[variant]['chrom']
		pos = variants[variant]['pos']

		coverage = tabix.open(gnomad_coverage)

		cov_info = coverage.query(chrom, pos-1, pos)  # chromosome, position, mean, median_approx, total_DP, over_1, over_5, over_10, over_15, over_20, over_25, over_30, over_50, over_100

		for entry in cov_info:

			gnomad_coverage = entry

		variants[variant]['acmg_gnomad_coverage'] = gnomad_coverage

	return variants

