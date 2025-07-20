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

def do_one_gene(df):
    # compute all counts
    df['c00'] = df.apply(count_each_row, axis=1, substr="0|0")
    df['c10'] = df.apply(count_each_row, axis=1, substr="1|0")
    df['c01'] = df.apply(count_each_row, axis=1, substr="0|1")
    df['c11'] = df.apply(count_each_row, axis=1, substr="1|1")
    df['c1s'] = df['c10'] + df['c01'] +  df['c11']
    df['c_sum'] = df['c00'] + df['c1s']

    pass
