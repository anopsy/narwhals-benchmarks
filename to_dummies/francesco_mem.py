import narwhals as nw
from pyarrow import csv

table = csv.read_csv("/workspaces/narwhals/analysis_df.csv")

@nw.narwhalify
def encode_one_v1(df, col):
    oh = df[col].to_dummies()
    return oh

@nw.narwhalify
def encode_more_v1(df, cols):
    for col in cols:
        oh = df[col].to_dummies()
        df = nw.concat([df, oh], how="horizontal")
    return df

col1 = "hours"
col2 = "language"
col3 = "country"
col4 = "city"
cols = [col1, col2, col3, col4]

t1 = encode_one_v1(table,col1)
t2 = encode_one_v1(table,col2)
t3 = encode_one_v1(table,col3)
t4 = encode_more_v1(table,cols)