import pandas as pd

df = pd.read_csv("./t_user.csv",iterator=True)
g = df.get_chunk()

print(list(g))
# for row in g.values:
# 	print(row)