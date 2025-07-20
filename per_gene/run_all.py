import glob
import pathlib
import pandas as pd
from os.path import join, basename

from mylib import vn_genomes
from mylib import count_1_per_genome
from mylib import do_one_gene
from mylib import find_matching_columns

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    infiles = glob.glob(join(script_directory, "../vn_data/input/per_gene/*.csv"))
    clinvar_infile = join(script_directory, "data/standardized_clinvar_result.csv")
    cdf = pd.read_csv(clinvar_infile)

    infiles.sort()
    for infile in infiles:
        base_filename = basename(infile).replace(".csv", "")
        outfile_parsed_INFO = join(script_directory, f"data/{base_filename}.parsed.INFO.csv")
        outfile_linked_clinvar = join(script_directory, f"data/{base_filename}.linked_clinvar.csv")
        outfile_count_1_per_genome = join(script_directory, f"data/{base_filename}.count1.per.genome.csv")

        df = pd.read_csv(infile)
        mdf = do_one_gene(
            df=df,
            cdf=cdf,
            outfile_parsed_INFO=outfile_parsed_INFO,
            outfile_linked_clinvar=outfile_linked_clinvar
        )

        tdf = count_1_per_genome(df=df, outfile_count_1_per_genome=outfile_count_1_per_genome)
        print(f"infile: {infile}, mdf.shape: {mdf.shape}, tdf.shape: {tdf.shape}")
        pass
    
