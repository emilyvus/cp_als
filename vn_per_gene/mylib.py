import pandas as pd
from typing import List

vn_genome_ids = [
    'HG02513', 'HG02138', 'HG02075', 'HG02031', 'HG02084', 'HG02047', 'HG01597', 'HG01849', 'HG02023', 'HG01846', 'HG02081', 
    'HG01599', 'HG01866', 'HG02064', 'HG02069', 'HG02087', 'HG02017', 'HG01864', 'HG01868', 'HG01596', 'HG02072', 'HG02079', 
    'HG01600', 'HG02140', 'HG01841', 'HG02020', 'HG01878', 'HG02085', 'HG01598', 'HG01872', 'HG02073', 'HG01845', 'HG02032', 
    'HG02088', 'HG01840', 'HG01855', 'HG02050', 'HG01844', 'HG02067', 'HG02133', 'HG02127', 'HG02512', 'HG02040', 'HG01859', 
    'HG02078', 'HG02070', 'HG02029', 'HG02116', 'HG01842', 'HG01867', 'HG02060', 'HG01843', 'HG02028', 'HG01861', 'HG01869', 
    'HG01865', 'HG01848', 'HG02048', 'HG02130', 'HG01595', 'HG01860', 'HG01853', 'HG02139', 'HG02121', 'HG01858', 'HG02058', 
    'HG02076', 'HG02131', 'HG02522', 'HG02019', 'HG01851', 'HG02016', 'HG01874', 'HG02057', 'HG02521', 'HG02035', 'HG02025', 
    'HG02128', 'HG01862', 'HG02134', 'HG02082', 'HG02122', 'HG01870', 'HG02136', 'HG01852', 'HG02137', 'HG01850', 'HG01857', 
    'HG02061', 'HG02142', 'HG01863', 'HG02026', 'HG01871', 'HG02141', 'HG01873', 'HG02049', 'HG02086', 'HG02113', 'HG01847'
    ]

def count_each_row(row, substr):
    count = 0  # first, initialize count to zero
    for cell in row:
        if pd.isna(cell):
            continue # if the cell is None, go to the next cell in the row
        if not isinstance(cell, str):
            continue # if the cell is not a string, go to the next cell in the row
        if cell == substr:
            count = count + 1 # if the cell matches the inpug substring, then increases the count by 1
            
    return count # return the total count

from copy import deepcopy

def do_one_gene(df, cdf, outfile_per_genome_counts, outfile_parsed_INFO, outfile_linked_clinvar):
    # Count per genome id, c00, c10, c01, c11, c1s
    gdf = df[vn_genome_ids]
    tdf = gdf.transpose() 

    # compute all counts
    tdf['c00'] = tdf.apply(count_each_row, axis=1, substr="0|0")
    tdf['c10'] = tdf.apply(count_each_row, axis=1, substr="1|0")
    tdf['c01'] = tdf.apply(count_each_row, axis=1, substr="0|1")
    tdf['c11'] = tdf.apply(count_each_row, axis=1, substr="1|1")
    tdf['c1s'] = tdf['c10'] + tdf['c01'] +  tdf['c11']
    tdf['c_sum'] = tdf['c00'] + tdf['c1s']

    tdf_new = tdf.reset_index().rename(columns={'index': 'vn_genome_ids'})
    tdf_new = tdf_new[['vn_genome_ids', 'c00', 'c10', 'c01', 'c11', 'c1s', 'c_sum']]
    tdf_new.to_csv(outfile_per_genome_counts, index=False)

    # compute all counts
    df['c00'] = df.apply(count_each_row, axis=1, substr="0|0")
    df['c10'] = df.apply(count_each_row, axis=1, substr="1|0")
    df['c01'] = df.apply(count_each_row, axis=1, substr="0|1")
    df['c11'] = df.apply(count_each_row, axis=1, substr="1|1")
    df['c1s'] = df['c10'] + df['c01'] +  df['c11']
    df['c_sum'] = df['c00'] + df['c1s']

    # parse INFO field
    df = parse_info_field(df=df)

    # Apply the function to each row and create the new column
    df['l00'] = df.apply(lambda row: find_matching_columns(row, ["0|0"]), axis=1)
    df['l01'] = df.apply(lambda row: find_matching_columns(row, ["0|1"]), axis=1)
    df['l10'] = df.apply(lambda row: find_matching_columns(row, ["1|0"]), axis=1)
    df['l11'] = df.apply(lambda row: find_matching_columns(row, ["1|1"]), axis=1)
    df['l1_all'] = df.apply(lambda row: find_matching_columns(row, ["0|1", "1|0", "1|1"]), axis=1)

    df.drop(columns=vn_genome_ids, inplace=True)
    df.to_csv(outfile_parsed_INFO, index=False)

    # Link gene df and clinvar by position
    intersection_df = pd.merge(df, cdf, how='inner', left_on='POS', right_on='new_GRCh38Location')
    intersection_df.to_csv(outfile_linked_clinvar, index=False)
    pass

def parse_info_field(df):
    series = df['INFO'].str.split(';')
    ll = list()
    for i, elem in enumerate (series):
        d=dict()
        for item in elem:
            if "=" in item:
                k,v = item.split("=")
            else:
                k,v = item, None

            d[f"INFO:{k}"]= v
        ll.append(d)
    
    info_df = pd.DataFrame(ll)
    df_final = pd.concat([df, info_df], axis=1)
    return df_final

def find_matching_columns(row, value_to_match):
    matching_cols = []
    for col_name, col_value in row.items():
        for v in value_to_match:
            if col_value == v:
                matching_cols.append(col_name)
    
    matching_cols.sort()
    return ",".join(matching_cols)
