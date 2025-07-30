import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import process_one_gene

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    individual_genome_files =glob.glob(join(script_directory,"../vn_data/input/per_gene/*.csv"))
    individual_genome_files.sort()

    outfile = join(script_directory,f"data/all.csv")
    df_list = list()
    for infile in individual_genome_files:
        fname = basename(infile)
        gene_name = fname.split(".")[0]

        one_gene_df = pd.read_csv(infile)

        odf= process_one_gene(
            df=one_gene_df, 
        )
        odf['gene'] = gene_name
        
        df_list.append(odf)
        print(f"infile:{infile}, odf:{odf.shape}")

    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(outfile, index=False)  
    pass





