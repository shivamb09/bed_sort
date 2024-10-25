chrom_numbers = [x.strip() for x in open("metadata/chrom_selection.tsv")]

configfile: "config.yaml"

rule split_by_chrom:
    input:
        file_list=config["info"]
    output:
        "splitted/{chrom}.bed"
    run:
        with open(input.file_list) as f:
            bed_files = [line.strip() for line in f.readlines()]
        final_bed_files = " ".join(bed_files)
        shell("mkdir -p splitted")
        shell(f"grep -h -w '^{wildcards.chrom}' {final_bed_files} > {output}")

rule sort_individual_files:
    input:
        "splitted/{chrom}.bed"
    output: 
        "sorted/{chrom}.bed"
    shell:
        "cat {input} | sort -k2,2n -k3,3n > {output}"

rule merge_sorted_files:
    input:
        expand("sorted/{chrom}.bed", chrom=chrom_numbers)
    output:
        "sort_by_chrom_final.bed.gz"
    params:
        chrom_list=",".join(chrom_numbers)
    run:
        file_paths = [f"sorted/{chrom}.bed" for chrom in chrom_numbers]
        final_paths = " ".join(file_paths)
        shell(f"cat {final_paths} | gzip > {output}")
