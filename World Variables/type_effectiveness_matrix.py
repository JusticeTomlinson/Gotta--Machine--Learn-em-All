import pandas as pd

type_effectiveness_matrix = pd.read_csv("type_effectiveness.csv")
type_effectiveness_matrix.reset_index(drop=True, inplace=True)

print(type_effectiveness_matrix.rows)
