import cx_Oracle
import pandas as pd
import numpy as np
import json
import sys

# Fixing 64x client version error: https://trustsu.com/python/databaseerror-dpi-1047-cannot-locate-a-64-bit-oracle-client-library-the-specified-module-could-not-be-found-2/
# Try
print('FAST EXTRACTOR\nCreated by Artyom Pak\n')
try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_3")
except:
    pass

# Importing json
try:
    with open('settings.txt', 'r') as f:
        s = f.read()
except:
    template = r"""{
                    "host":"",
                    "db":"",
                    "uid":"",
                    "pwd":"",
                    "schema":""
                    }
                """
    
    with open('settings.txt', 'w') as f:
        f.write(template)
    input('Find settings.txt\n\nPRESS ANY KEY TO EXIT')
    sys.exit()
    
credentials = json.loads(s)

# Variables
connstrg = f"{credentials['uid']}/{credentials['pwd']}@{credentials['host']}:1521/{credentials['db']}"
schema = f"ALTER SESSION SET current_schema = {credentials['schema']}"
sql = str(input('Enter you sql-query: '))


# Creating connection
conn = cx_Oracle.connect(connstrg)

# Executing SQL-statements
cur = conn.cursor()
cur.execute(schema)
cur.execute(sql)

# List for DB output
result = []

# Iteration
for i in cur.fetchall():
    result.append(i)

# Converting to array
result = np.array(result)

# Converting to DataFrame
final = pd.DataFrame(result, columns=[i[0] for i in cur.description])  # i[0] first element of the tuple

# Closing
cur.close()
conn.close()

# Exporting
final.to_excel(f"~/Downloads/extracted_1.xlsx", merge_cells=False, index=False)
