import pandas as pd
import numpy as np
from os import path
import os
# import mysql.connector
from sqlalchemy import create_engine

n_rows = 1_000_000
n_cols = 100

filename = "csv_files/analysis_1.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("FOOBAR")

for i in range(1, 3):
    filename = 'analysis_%d.csv' % i
    file_path = path.join('csv_files', filename)
    df = pd.DataFrame(np.random.uniform(0, 100, size=(n_rows, n_cols)), columns=['col%d' % i for i in range(n_cols)])
    print('Saving', file_path)
    df.to_csv(file_path, index=False)
df.head()

engine = create_engine('mysql+mysqldb://user:password@server:3306/BigData', echo = False)
df.to_sql(name = 'my_table', con = engine, if_exists = 'append', index = False)