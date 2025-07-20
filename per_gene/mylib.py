import pandas as pd

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
                print (i, elem, "Assign None")

            d[f"INFO:{k}"]= v
        ll.append(d)
    
    info_df = pd.DataFrame(ll)
    df_final = pd.concat([df, info_df], axis=1)
    for col in df_final.columns:
        df_final[col] = pd.to_numeric(df_final[col], errors='ignore')
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
