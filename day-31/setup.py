'''
PANDAS TERMINOLOGY
series-column
dataframe-db/table


import pandas


data = {
    'Name': ['Rajat', 'Tarun', 'Bobby'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Delhi', 'Pune']
}

df = pandas.DataFrame(data)
csv_file_path = 'data.csv'
with open(csv_file_path, mode='w'):


df.to_csv(csv_file_path, index=False)


print(csv_file_path)
'''