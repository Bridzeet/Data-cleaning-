import pandas as pd
raw_csv_data = pd.read_csv(r"C:\Users\Brygida\Desktop\Python\Projekt_Absenteeism\Absenteeism-data.csv")

df = raw_csv_data.copy()
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = df.drop(['ID'], axis = 1)
#print(df)

df['Reason for Absence'].min()
df['Reason for Absence'].max()
pd.unique(df['Reason for Absence'])
len(df['Reason for Absence'].unique())
sorted(df['Reason for Absence'].unique())

reason_columns = pd.get_dummies(df['Reason for Absence'])
reason_columns['check'] = reason_columns.sum(axis=1)
reason_columns = reason_columns.drop(['check'], axis = 1)
reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)
# print(df.columns.values)
# print(reason_columns.columns.values)
df = df.drop(['Reason for Absence'], axis = 1)

reason_type_1 = reason_columns.loc[:, 1:14].max(axis=1)
reason_type_2 = reason_columns.loc[:, 15:17].max(axis=1)
reason_type_3 = reason_columns.loc[:, 18:21].max(axis=1)
reason_type_4 = reason_columns.loc[:, 22:].max(axis=1)

df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis = 1)
# print(df.columns.values)
column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']

df.columns = column_names
# print(df.head())

column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 
                          'Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']

df = df[column_names_reordered]
# print(df.head())

df_reason_mod = df.copy()
# print(df_reason_mod)

df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format = '%d/%m/%Y')

# print(df_reason_mod['Date'][0])
# print(df_reason_mod['Date'][0].month)

list_months = []
# print(list_months)

# print(df_reason_mod.shape)

for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)
    
# print(list_months)
# print(len(list_months))
df_reason_mod['Month Value'] = list_months
# print(df_reason_mod.head(20))

# print(df_reason_mod['Date'][699].weekday())
# print(df_reason_mod['Date'][699])

def date_to_weekday(date_value):
    return date_value.weekday()

df_reason_mod['Day of the Week'] = df_reason_mod['Date'].apply(date_to_weekday)

# print(df_reason_mod.head())


df_reason_date_mod = df_reason_mod.copy()
# print(df_reason_date_mod)

# print(display(df_reason_date_mod))
# print(df_reason_date_mod['Education'].unique())
# print(df_reason_date_mod['Education'].value_counts())
df_reason_date_mod['Education'] = df_reason_date_mod['Education'].map({1:0, 2:1, 3:1, 4:1})
# print(df_reason_date_mod['Education'].unique())
# print(df_reason_date_mod['Education'].value_counts())

df_cleaned = df_reason_date_mod.copy()
df_cleaned.head(10)