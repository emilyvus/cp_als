import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import process_one_gene
from mylib import get_genome_ids

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":

    # For each population, change the input and output folder 

    #individual_genome_files =glob.glob(join(script_directory,"input/KHV*.csv"))
    #outfile = join(script_directory,f"output/KHV/all.csv")
    
    #individual_genome_files =glob.glob(join(script_directory,"input/GBR/*.csv"))
    #outfile = join(script_directory,f"output/GBR/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/ASW/*.csv"))
    #outfile = join(script_directory,f"output/ASW/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/ACB/*.csv"))
    #outfile = join(script_directory,f"output/ACB/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/BEB/*.csv"))
    #outfile = join(script_directory,f"output/BEB/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/CDX/*.csv"))
    #outfile = join(script_directory,f"output/CDX/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/CLM/*.csv"))
    #outfile = join(script_directory,f"output/CLM/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/ESN/*.csv"))
    #outfile = join(script_directory,f"output/ESN/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/FIN/*.csv"))
    #outfile = join(script_directory,f"output/FIN/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/GWD/*.csv"))
    #outfile = join(script_directory,f"output/GWD/all.csv")
    
    #individual_genome_files =glob.glob(join(script_directory,"input/GIH/*.csv"))
    #outfile = join(script_directory,f"output/GIH/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/CHB/*.csv"))
    #outfile = join(script_directory,f"output/CHB/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/CHS/*.csv"))
    #outfile = join(script_directory,f"output/CHS/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/IBS/*.csv"))
    #outfile = join(script_directory,f"output/IBS/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/ITU/*.csv"))
    #outfile = join(script_directory,f"output/ITU/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/JPT/*.csv"))
    #outfile = join(script_directory,f"output/JPT/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/LWK/*.csv"))
    #outfile = join(script_directory,f"output/LWK/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/MSL/*.csv"))
    #outfile = join(script_directory,f"output/MSL/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/MXL/*.csv"))
    #outfile = join(script_directory,f"output/MXL/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/PEL/*.csv"))
    #outfile = join(script_directory,f"output/PEL/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/PUR/*.csv"))
    #outfile = join(script_directory,f"output/PUR/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/PJL/*.csv"))
    #outfile = join(script_directory,f"output/PJL/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/STU/*.csv"))
    #outfile = join(script_directory,f"output/STU/all.csv")

    #individual_genome_files =glob.glob(join(script_directory,"input/TSI/*.csv"))
    #outfile = join(script_directory,f"output/TSI/all.csv")

    individual_genome_files =glob.glob(join(script_directory,"input/YRI/*.csv"))
    outfile = join(script_directory,f"output/YRI/all.csv")


    df_list = list()
    for infile in individual_genome_files:
        fname = basename(infile)
        gene_name = fname.split(".")[0]
        one_gene_df = pd.read_csv(infile)

        genome_ids = get_genome_ids(list(one_gene_df.columns))

        odf = process_one_gene(
            df=one_gene_df,
            genome_ids= genome_ids
        )
        odf['gene']=gene_name
        df_list.append(odf)
        print(f"infile:{infile},odf:{odf.shape}")


    combined_df = pd.concat(df_list, ignore_index=True)  
    combined_df.to_csv(outfile, index=False)   
    
    print(genome_ids)
    pass





