import pandas as pd
import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import do_one_gene

script_directory = pathlib.Path(__file__).parent.resolve()

infile_all_genes = join(script_directory, "data/all_genes.csv")
df = pd.read_csv(infile_all_genes)
cols = ['POS', 'vn_af', 'c1s']
df=df[cols]

vn_af_stats_all_genes = df['vn_af'].describe().to_dict()
vn_af_stats_all_genes["type"] = "vn_af_stats_all_genes"

c1s_stats_all_genes = df['c1s'].describe().to_dict()
c1s_stats_all_genes["type"] = "c1s_stats_all_genes"

outputfile_all_genes = join(script_directory, "results/variants_stats_all_genes.csv")
odf = pd.DataFrame(
    [
        vn_af_stats_all_genes,
        c1s_stats_all_genes
    ]
)
odf.to_csv(outputfile_all_genes, index=False)


infile_all_genomes = join(script_directory, "data/all_genes.genome.counts.csv")
df = pd.read_csv(infile_all_genomes)
df = df[['vn_genome_ids', 'c1s']]
gdf = df.groupby(['vn_genome_ids']).describe()
gdf.columns = gdf.columns.get_level_values(1)
gdf.reset_index(inplace=True)
outputfile_all_genomes = join(script_directory, "results/variants_stats_all_genomes.csv")
gdf.to_csv(outputfile_all_genomes, index=False)
pass