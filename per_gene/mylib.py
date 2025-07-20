import pandas as pd
from os.path import join

def do_one_gen(df, cdf, outfile_parsed_INFO, outfile_linked_clinvar):
    # compute all counts
    df['c00'] = df.apply(count_each_row, axis=1, substr="0|0")
    df['c10'] = df.apply(count_each_row, axis=1, substr="1|0")
    df['c01'] = df.apply(count_each_row, axis=1, substr="0|1")
    df['c11'] = df.apply(count_each_row, axis=1, substr="1|1")
    df['c1s'] = df['c10'] + df['c01'] +  df['c11']
    df['c_sum'] = df['c00'] + df['c1s']

    # parse INFO field
    df_final = parse_info_field(df=df)
    # save to file
    df_final.to_csv(outfile_parsed_INFO, index=False)
    mdf = pd.merge(df, cdf, how='inner', left_on='POS', right_on='new_GRCh38Location')
    mdf.to_csv(outfile_linked_clinvar, index=False)
    return mdf

def parse_info_field(df: pd.DataFrame):
    series = df['INFO'].str.split(';')
    ll = list()
    for i, elem in enumerate (series):
        d=dict()
        for item in elem:
            if "=" in item:
                k,v = item.split("=")
            else:
                k,v = item, None
                #print (i, elem, "Assign None")

            d[f"INFO:{k}"]= v
        ll.append(d)
    
    info_df = pd.DataFrame(ll)
    df_final = pd.concat([df, info_df], axis=1)
    # for col in df_final.columns:
    #     df_final[col] = pd.to_numeric(df_final[col], errors='ignore')
    return df_final

# Function to count substring in a row, looping through all cell in the row
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
