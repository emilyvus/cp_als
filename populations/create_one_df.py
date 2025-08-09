import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import process_one_gene
from mylib import get_genome_ids


script_directory = pathlib.Path(__file__).parent.resolve()
if __name__ == "__main__":
    # for each population, change the input and output folders
    individual_genome_files =glob.glob(join(script_directory,"input/KHV/*.csv"))
    outfile = join(script_directory,f"output/KHV/all.csv")

    # individual_genome_files =glob.glob(join(script_directory,"/input/GBR/*.csv"))
    # outfile = join(script_directory,f"output/GBR/all.csv")

    df_list = list()
    for infile in individual_genome_files:
        fname = basename(infile)
        gene_name = fname.split(".")[0]
        one_gene_df = pd.read_csv(infile)

        genome_ids=get_genome_ids(columns=list(one_gene_df.columns))

        odf = process_one_gene(
            df=one_gene_df,
            genome_ids=genome_ids
        )
        
        odf['gene']=gene_name
        df_list.append(odf)
        print(f"infile:{infile},odf:{odf.shape}")

    combined_df = pd.concat(df_list, ignore_index=True)  
    combined_df.to_csv(outfile, index=False)

    print(genome_ids)   
    pass





