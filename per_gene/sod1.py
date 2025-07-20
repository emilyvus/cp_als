import pandas as pd
import pathlib
from os.path import join, basename
from mylib import count_each_row
from mylib import parse_info_field

script_directory = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    print(script_directory)
    infile = join(script_directory, "../vn_data/input/per_gene/SOD1.chr21.csv")
    outfile_parsed_INFO = join(script_directory, "data/SOD1/SOD1.chr21.parsed.INFO.csv")
    df = pd.read_csv(infile)

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

    
    pass