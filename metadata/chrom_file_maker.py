chrom_list = list()

with open("chrom_selection.tsv","w") as file:
	for i in range(1,23):
		file.write(f"chr{i}")
		file.write("\n")
	file.write("chrX")
	file.write("\n")
	file.write("chrY")
	file.write("\n")
	file.close()
