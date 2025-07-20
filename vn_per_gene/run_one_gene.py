import pandas as pd
from os.path import join, basename
import os
from mylib import do_one_gene

script_directory = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(f"Script dir: {script_directory}")
    infile = join(script_directory, "../vn_data/input/per_gene/ALS2.chr2.csv")
    print(infile)

    one_gene_df = pd.read_csv(infile)
    do_one_gene(df=one_gene_df)
    pass