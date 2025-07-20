from mylib import do_one_gen
import pandas as pd
import pathlib
from os.path import join, basename
import glob

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    infiles = glob.glob(join(script_directory, "../vn_data/input/per_gene/*.csv"))
    clinvar_infile = join(script_directory, "data/standardized_clinvar_result.csv")
    cdf = pd.read_csv(clinvar_infile)

    infiles.sort()
    for infile in infiles:
        #infile = join(script_directory, "../vn_data/input/per_gene/SOD1.chr21.csv")
        base_filename = basename(infile).replace(".csv", "")
        outfile_parsed_INFO = join(script_directory, f"data/{base_filename}.parsed.INFO.csv")
        outfile_linked_clinvar = join(script_directory, f"data/{base_filename}.linked_clinvar.csv")
        df = pd.read_csv(infile)
        mdf = do_one_gen(
            df=df,
            cdf=cdf,
            outfile_parsed_INFO=outfile_parsed_INFO,
            outfile_linked_clinvar=outfile_linked_clinvar
        )
        print(f"infile: {infile}, mdf.shape: {mdf.shape}")
        pass
    
