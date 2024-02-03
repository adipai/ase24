import pandas as pd

data = pd.read_csv("../../Data/soybean.csv")
cols = data.columns
new_dataframe_dict = {}

final_list = []
for col in cols:

    col_vals = data[col]
    new_col_vals = []
    for i in range(len(col_vals)):
        new_col_vals.append(col_vals[i].strip())
    
    final_list.append(new_col_vals)

for i in range(len(cols)):

    col_name = cols[i]
    if(col_name not in new_dataframe_dict):
        new_dataframe_dict[col_name] = final_list[i]

new_dataframe = pd.DataFrame(new_dataframe_dict)
print(new_dataframe)
new_dataframe.to_csv("../../Data/soybean_new.csv", index=False)


