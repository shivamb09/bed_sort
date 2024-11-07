#Bed_sort

This particular snakemake code was to sort bed files according to chromosome number followed by their start site and then their stop site. These are two big files so we had to sort them efficiently. 


command to run on terminal 

snakemake --cores n --snakefile final_quick_bed_sort.smk sort_by_chrom_final.bed.gz

n=no of cores you want to assosciate with the task
