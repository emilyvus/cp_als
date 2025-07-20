import pathlib
import pandas as pd
from os.path import join
from copy import deepcopy

script_directory = pathlib.Path(__file__).parent.resolve()
def expand_row(row):
    t = row['GRCh38Location'].split("-")
    rows_to_add = list()
    for i in range(int(t[0]), int(t[1]) + 1):
        new_row = deepcopy(row)
        new_row['new_GRCh38Location'] = i
        rows_to_add.append(new_row)

    return rows_to_add

if __name__ == "__main__":
    infile = join(script_directory, "data/clinvar_result.txt")
    outfile = join(script_directory, "data/standardized_clinvar_result.csv")
    df = pd.read_csv(infile, sep='\t')

    columns_to_keep = [
        'Name', 'Gene(s)', 'Protein change', 'Condition(s)', 
        #'Accession',
        #'GRCh37Chromosome', 'GRCh37Location', 
        'GRCh38Chromosome',
        'GRCh38Location', 
        #'VariationID', 'AlleleID(s)', 
        #'dbSNP ID',
        #'Canonical SPDI', 
        #'Variant type', 
        #'Molecular consequence',
        'Germline classification', 
        'Germline date last evaluated',
        'Germline review status', 
        #'Somatic clinical impact',
        #'Somatic clinical impact date last evaluated',
        #'Somatic clinical impact review status', 'Oncogenicity classification',
        #'Oncogenicity date last evaluated', 'Oncogenicity review status'
    ]
    df = df[columns_to_keep]

    df = df[~df['GRCh38Location'].isna()]
    df_with_minus = df[df['GRCh38Location'].str.contains("-")]
    df_without_minus = df[~df['GRCh38Location'].str.contains("-")]
    df_without_minus['new_GRCh38Location'] = df_without_minus['GRCh38Location']

    expanded_rows = df_with_minus.apply(expand_row, axis=1) 
    cdf_new = pd.DataFrame([item for sublist in expanded_rows for item in sublist])
    rdf = pd.concat([df_without_minus, cdf_new], axis=0)
    rdf_chained = rdf.reset_index().rename(columns={'index': 'orig_clinvar_idx'})

    rdf_chained.to_csv(outfile, index=False)
    pass