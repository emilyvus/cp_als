import pandas as pd
from os.path import join, basename
import os
from mylib import do_one_gene

script_directory = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(f"Script dir: {script_directory}")
    infile = join(script_directory, "../vn_data/input/per_gene/ALS2.chr2.csv")
    base_infile = basename(infile).replace(".csv", "")

    clinvar_infile = join(script_directory, "data/standardized_clinvar_result.csv")

    outfile_per_genome_counts = join(script_directory, f"data/{base_infile}.per.genome.counts.csv")
    outfile_parsed_INFO = join(script_directory, f"data/{base_infile}.parsed.INFO.csv")
    outfile_linked_clinvar = join(script_directory, f"data/{base_infile}.linked.clinvar.csv")

    print(infile)

    one_gene_df = pd.read_csv(infile)
    clinvar_df = pd.read_csv(clinvar_infile)

    do_one_gene(
                df=one_gene_df,
                cdf=clinvar_df,
                outfile_per_genome_counts=outfile_per_genome_counts,
                outfile_parsed_INFO=outfile_parsed_INFO,
                outfile_linked_clinvar=outfile_linked_clinvar
                )
    pass