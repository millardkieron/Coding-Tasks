## Task 1

Task1 = open("/home/kieron/Downloads/174-0.txt")

dict1 = {}
punctuation = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~-"   # String to find all punctuation and remove them to match up words.

for line in Task1:
	line = line.strip()                               # Remove all leading and new line spaces from each line
	line = line.lower()                               # Convert all letters into lower case for matching
	line = line.replace(punctuation, "")              # Replacing all punctuation with nothing 
	words = line.split(" ")                           # Split each line into words at every whitespace
	for w in words:                                       # Loop for every word in line
		if w in dict1:                                    
			dict1[w] = dict1[w] + 1                       # Checking if the word is already in the dictionary, if it is, add 1 to dictionary value.
		else:
			dict1[w] =1                                   # If not in dictionary then add to dictionary with a value of 1

print(dict1)			



## Task 2 - Consequences Exporting and Counting

import re                                              # Imported to help with spliting at special characters

Task2 = open("/home/kieron/Downloads/test38.norm.anno.vcf")


list1 = []
divide = "\|"                                          # String of special character excaped to help with splitting


# List of all the possible consequences VEP as strings can define to then be searched from the vcf.

Consequence_String = ["transcript_ablation","splice_acceptor_variant", "splice_donor_variant", "stop_gained", "frameshift_variant", "stop_lost", "start_lost", "transcript_amplification",\
 "inframe_insertion", "inframe_deletion", "missense_variant", "protein_altering_variant", "splice_region_variant", "splice_donor_5th_base_variant", "splice_donor_region_variant",\
 "splice_polypyrimidine_tract_variant", "incomplete_terminal_codon_variant", "start_retained_variant", "stop_retained_variant", "synonymous_variant", "coding_sequence_variant",\
 "mature_miRNA_variant", "5_prime_UTR_variant", "3_prime_UTR_variant", "non_coding_transcript_exon_variant", "intron_variant", "NMD_transcript_variant", "non_coding_transcript_variant", "upstream_gene_variant"\
 "downstream_gene_variant", "TFBS_ablation", "TFBS_amplification", "TF_binding_site_variant", "regulatory_region_ablation", "regulatory_region_amplification", "feature_elongation",\
 "regulatory_region_variant", "feature_truncation", "intergenic_variant"]

for line in Task2:
	line = line.replace("&", "\|")                      # Replacing every & with a | to remove the combined consequences as well as allowing each one to be counted later
	line = re.split(divide, line)                       # Splitting each line at every | as this is the main divider and borders every consequence in the VEP.
	for i in line:
		if i in Consequence_String:                     # Searches every word within the line to see if it is also present in the Consequence String List
			list1.append(str(i))                        # If it is found then it is added to a list

counts = {x:list1.count(x) for x in list1}              # Each string is then counted and then converted into a dictionary of consequence : count.

print(counts)

# This is computationally intensive so output is as follows:

#{'intron_variant': 137796, 'synonymous_variant': 40869, 'missense_variant': 31142, 'regulatory_region_variant': 24174, 'TF_binding_site_variant': 7205, 'inframe_deletion': 392, 
#'5_prime_UTR_variant': 6314, '3_prime_UTR_variant': 9199, 'non_coding_transcript_exon_variant': 11366, 'non_coding_transcript_variant': 19041, 'frameshift_variant': 566, 'inframe_insertion': 360, 
#'splice_acceptor_variant': 75, 'start_lost': 44, 'stop_gained': 200, 'splice_region_variant': 688, 'splice_donor_variant': 113, 'intergenic_variant': 529, 'stop_retained_variant': 25, 
#'start_retained_variant': 8, 'stop_lost': 18, 'protein_altering_variant': 5, 'coding_sequence_variant': 13}



## Task 3 - Maths Function

def my_function(x):                                     # Create a function that , while x is larger than 1, if it is even, half it, if it is odd, multiply by 3 and add 1.
	while x > 1:                                        # while loop used to check x is above 1
		if x % 2 == 0:                                  # Using division by 2 to see if x creates a remainder value or not
			x = x / 2                                   # If it doesnt then divide x by 2
		else:
			x = ((x*3) + 1)                             # If odd then do other command 
		print(x)                                        # Print x each time it goes through the loop to see all iterations of x before reaching 1

print(my_function(12))