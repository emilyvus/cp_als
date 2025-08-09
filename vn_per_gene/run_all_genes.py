import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import do_one_gene

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    individual_genome_files =glob.glob(join(script_directory,"../vn_data/input/per_gene/*.csv"))
    standardized_clinvar_infile = join(script_directory,"data/standardized_clinvar_result.csv")
    clinvar_df = pd.read_csv(standardized_clinvar_infile)

    individual_genome_files.sort()

    for infile in individual_genome_files:
        base_filename = basename(infile).replace(".csv","")
        outfile_per_genome_counts = join(script_directory,f"data/{base_filename}.per.genome.counts.csv")
        outfile_parsed_INFO = join(script_directory,f"data/{base_filename}.parsed.INFO.csv")
        outfile_linked_clinvar = join(script_directory,f"data/{base_filename}.linked.clinvar.csv")
        outfile_linked_clinvar_noindel = join(script_directory,f"data/{base_filename}.linked.clinvar.noindel.csv")


        #print(standardized_clinvar_infile)

        one_gene_df = pd.read_csv(infile)

        intersection_df= do_one_gene(
            df=one_gene_df, 
            cdf= clinvar_df,
            outfile_per_genome_counts=outfile_per_genome_counts,
            outfile_parsed_INFO=outfile_parsed_INFO,
            outfile_linked_clinvar=outfile_linked_clinvar,
            outfile_linked_clinvar_noindel=outfile_linked_clinvar_noindel 
            )
        print(f"infile:{infile}, intersection_df:{intersection_df.shape}")
        
    pass





