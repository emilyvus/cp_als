import pandas as pd
import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import do_one_gene

script_directory = pathlib.Path(__file__).parent.resolve()


# Create a list of DataFrames
def test():
    df_list = []
    df_list.append(pd.DataFrame({'col1': [1, 2], 'col2': ['A', 'B']}))
    df_list.append(pd.DataFrame({'col1': [3, 4], 'col2': ['C', 'D']}))
    df_list.append(pd.DataFrame({'col1': [5, 6], 'col2': ['E', 'F']}))

# Concatenate the DataFrames
    combined_df = pd.concat(df_list, ignore_index=True)

    print(combined_df)

    pass 

per_genome_counts =glob.glob(join(script_directory,"data/*.per.genome.counts.csv"))
df_list=list()
for infile in per_genome_counts:
    print(infile)
    df = pd.read_csv(infile)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)
print(combined_df.shape)

outputfile = join(script_directory,"data/all_genes.per.genome.counts.csv")
combined_df.to_csv(outputfile,index=False)