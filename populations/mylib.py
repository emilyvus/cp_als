import pandas as pd
from typing import List

def get_genome_ids(columns):
    removed_columns = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
    genome_ids = [col for col in columns if col not in removed_columns]
    return genome_ids

def count_each_row(row, substr):
    count = 0
    for cell in row:
        if pd.isna(cell):
            continue
        if not isinstance(cell,str):
            continue
        if cell == substr:
            count = count + 1
    
    return count

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
            
            d[f"INFO:{k}"]=v
        ll.append(d)
    
    info_df = pd.DataFrame(ll)
    df_final = pd.concat([df, info_df],axis=1)
    return df_final

def find_matching_columns(row, value_to_match):
    matching_cols = []
    for col_name, col_value in row.items():
        for v in value_to_match:
            if col_value ==v:
                matching_cols.append(col_name)
    
    matching_cols.sort()
    return",".join(matching_cols)

def process_one_gene(df,genome_ids):
    df['c00'] = df.apply(count_each_row, axis = 1, substr="0|0")
    df['c01'] = df.apply(count_each_row, axis = 1, substr="0|1")
    df['c10'] = df.apply(count_each_row, axis = 1, substr="1|0")
    df['c11'] = df.apply(count_each_row, axis = 1, substr="1|1")
    df['c1s']= df ['c10']+df['c01']+df['c11']
    df['c_sum']=df['c00']+df['c1s']
    df['vn_af']=df['c1s']/df['c_sum']
    
    df['genome'] = df.apply(lambda row: find_matching_columns(row,["0|1", "1|0", "1|1"]),axis=1)
    df.drop(columns=['ID','QUAL'], inplace=True)
    
    df = df.replace(['0|0'],0)
    df = df.replace(['1|0','0|1','1|1'],1)
    
    for col in genome_ids:
        df[col]=df[col].astype(int)
    

    df = parse_info_field(df=df)
    df = df.loc[df['INFO:EAS_AF'].astype(float) <= 0.3]
    df = df.loc[df['INFO:VT'] != 'INDEL']


    return df
               
    


   
