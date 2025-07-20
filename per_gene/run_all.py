import glob
import pathlib
import pandas as pd
from copy import deepcopy
from os.path import join, basename

from mylib import count_1_per_genome
from mylib import do_one_gene

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    individual_genome_files = glob.glob(join(script_directory, "../vn_data/input/per_gene/*.csv"))
    standardized_clinvar_infile = join(script_directory, "data/standardized_clinvar_result.csv")
    # load stanardized Clinvar into a data frame
    clinvar_df = pd.read_csv(standardized_clinvar_infile)

    individual_genome_files.sort()

    for infile in individual_genome_files:
        base_filename = basename(infile).replace(".csv", "")
        outfile_parsed_INFO = join(script_directory, f"data/{base_filename}.parsed.INFO.csv")
        outfile_linked_clinvar = join(script_directory, f"data/{base_filename}.linked_clinvar.csv")
        outfile_count_1_per_genome = join(script_directory, f"data/{base_filename}.count1.per.genome.csv")

        one_gene_df = pd.read_csv(infile)
        orig_one_gene_df = deepcopy(one_gene_df)
        
        intersection_df = do_one_gene(
            df=one_gene_df,
            cdf=clinvar_df,
            outfile_parsed_INFO=outfile_parsed_INFO,
            outfile_linked_clinvar=outfile_linked_clinvar
        )

        tdf = count_1_per_genome(df=orig_one_gene_df, outfile_count_1_per_genome=outfile_count_1_per_genome)
        print(f"infile: {infile}, mdf.shape: {intersection_df.shape}, tdf.shape: {tdf.shape}")
        pass
    
