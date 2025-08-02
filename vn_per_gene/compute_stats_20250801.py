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

#1. Which gene has the most variants?
df1 = df[["gene","POS"]].groupby(["gene"]).count()
df1.reset_index(inplace=True)
outfile1 = join(script_directory,"20250801/variants_count_per_gene.csv")
df1.rename(columns={"POS":"variant_count"},inplace=True)
df1=df1.sort_values(by=["variant_count"],ascending=False).reset_index(drop=True)
df1.to_csv(outfile1,index=False)

#2. Per genome, what is the total # of variants (for all genes)?
per_genome_variant_count =df[vn_genome_ids].sum(axis=0)
df2= pd.DataFrame(per_genome_variant_count)
df2.reset_index(inplace=True)
df2.rename(columns={'index':'genome',0:'variant_count'}, inplace=True)
df2=df2.sort_values(by=["variant_count"],ascending=False).reset_index(drop=True)
outfile2 = join(script_directory,"20250801/variants_count_per_genome.csv")
df2.to_csv(outfile2,index=False)

#3. For the top 10 genes:
#3a: Find average number of variants per genome, for each gene (10*99 #'s)
#3b: Find average number of variants per genome, for all genes (99 #'s)

top_genes = ["SOD1","FUS", "C9ORF72", "TARDP", "ERBB4", "ATXN2", "ALS2", "NEK1","FIG4", "SETX"]
#3a:
df3 = df[df["gene"].isin(top_genes)][vn_genome_ids+["gene"]]
df3a=df3.groupby(["gene"]).mean()
df3a.reset_index(inplace=True)
outfile3a = join(script_directory,"20250801/variants_avg_per_genome_per_gene_top_genes.csv")
df3a.to_csv(outfile3a,index=False)

#3b:

per_genome_variant_avg = df[df["gene"].isin(top_genes)][vn_genome_ids].mean(axis=0)
df3b= pd.DataFrame(per_genome_variant_avg)
df3b.reset_index(inplace=True)
df3b.rename(columns={'index':'genome',0:'variant_avg'}, inplace=True)
df3b=df3b.sort_values(by=["variant_avg"],ascending=False).reset_index(drop=True)
outfile3b = join(script_directory,"20250801/variants_avg_per_genome_top_genes.csv")
df3b.to_csv(outfile3b,index=False)

pass
