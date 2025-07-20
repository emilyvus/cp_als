import pandas as pd
import pathlib
from os.path import join, basename
from mylib import count_each_row
from mylib import parse_info_field

script_directory = pathlib.Path(__file__).parent.resolve()

def test():
    # Sample DataFrame
    data = {'ID': [1, 2], 'Quantity': [2, 3], 'Item': ['Apple', 'Banana']}
    df = pd.DataFrame(data)

    def expand_row(row):
        rows_to_add = []
        for i in range(row['Quantity']):
            rows_to_add.append({'ID': row['ID'], 'Item': row['Item'], 'Instance': i + 1})
        return rows_to_add

    # Apply the function and concatenate the results
    expanded_rows = df.apply(expand_row, axis=1)
    df_new = pd.DataFrame([item for sublist in expanded_rows for item in sublist])
    pass

from copy import deepcopy
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
        'GRCh37Chromosome', 'GRCh37Location', 'GRCh38Chromosome',
        'GRCh38Location', 
        #'VariationID', 'AlleleID(s)', 
        'dbSNP ID',
        'Canonical SPDI', 
        #'Variant type', 
        'Molecular consequence',
        'Germline classification', 'Germline date last evaluated',
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
    rdf_chained = rdf.reset_index().rename(columns={'index': 'original_index'})

    rdf_chained.to_csv(outfile, index=False)
    pass