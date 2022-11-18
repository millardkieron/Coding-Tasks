#!/bin/bash

#SBATCH --partition=dev
#SBATCH --time=24:00:00
#SBATCH --mem=4G

#Change the line below for the module needed
module load samtools/1.10

samtools idxstats alignment_sorted_withRG.bam | awk '{print $1" "$3}' > finalcount.txt
