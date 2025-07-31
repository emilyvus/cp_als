import pandas as pd
import glob
import pathlib
import pandas as pd
from os.path import join, basename
import os
from mylib import vn_genome_ids

script_directory = pathlib.Path(__file__).parent.resolve()
infile_all_genes = join(script_directory,"data/all.csv")

df = pd.read_csv(infile_all_genes)

# compute across: all genes/genomes, vn_af, and c1s stats
cols = ['POS','vn_af','c1s']
df1 = df[cols]

vn_af_stats_all_genes  = df1['vn_af'].describe().to_dict()
vn_af_stats_all_genes["type"]="genome_per_variants_vn_af"

c1s_stats_all_genes  = df1['c1s'].describe().to_dict()
c1s_stats_all_genes["type"]="genome_per_variants_c1s"
outputfile_all_genes = join(script_directory,"results/genome_per_variants.csv")
odf = pd.DataFrame(
    [
        vn_af_stats_all_genes,
        c1s_stats_all_genes
    ]

)
odf.to_csv(outputfile_all_genes,index=False)

# across all genes & all genomes and positions, compute the variant stats
gdf = df[vn_genome_ids].describe()
gdf.reset_index(names=['stats'],inplace=True)
outputfile_all_genes_genome = join(script_directory,"results/variants_per_genome.csv")
gdf.to_csv(outputfile_all_genes_genome, index=False)
pass

# per gene, what is the avg # of variants per position across all genomes?

df2 = df[['gene','c1s']]
gdf2 = df2.groupby(['gene']).describe()
gdf2.columns = gdf2.columns.get_level_values(1)
gdf2.reset_index(inplace=True)
outputfile_per_gene_c1s = join(script_directory,"results/per_gene_genome_per_variants_c1s.csv")
gdf2.to_csv(outputfile_per_gene_c1s,index=False)


df3 = df[['gene','vn_af']]
gdf3 = df2.groupby(['gene']).describe()
gdf3.columns = gdf3.columns.get_level_values(1)
gdf3.reset_index(inplace=True)
outputfile_per_gene_vn_af = join(script_directory,"results/per_gene_genome_per_variants_vn_af.csv")
gdf3.to_csv(outputfile_per_gene_vn_af,index=False)

# per gene, what is the avg # of variants per genome across all positions?
df4= df[['gene'] +vn_genome_ids]
gdf4 = df4.groupby(['gene']).describe()
#gdf4.columns = gdf4.columns.get_level_values(1)
#gdf4.reset_index(inplace=True)
outputfile_per_gene_per_genome = join(script_directory,"results/per_gene_per_genome_count.csv")
gdf4.to_csv(outputfile_per_gene_per_genome)

pass
