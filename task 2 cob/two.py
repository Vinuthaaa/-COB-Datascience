import pandas as pd
data = pd.read_csv('dataset - netflix1.csv')

missingdata = data.isnull().sum()
print(missingdata)

def rem_out(data,col):
    for i in col:
        if pd.api.types.is_numeric_dtype(data[col]):
            a = data[col].quantile(0.25)
            b = data[col].quantile(0.75)
            c = b-a
            lb = a-1.5*c
            ub = b1+1.5*c
            data = data[(data[col] >= lb) & (data[col]<=ub)]
    return data
cols = ["show_id","type","title","director","country","date_added","release_year","rating","duration","listed_in"  ]
data = rem_out(data,cols)
data.to_csv("cleaned.csv", index= False)