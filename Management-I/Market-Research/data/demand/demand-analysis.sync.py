# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

data = './schools-bogota-20250517.csv'

df = pd.read_csv(data)

print(df.info())
print(df.head())

# %%
column_indeces = [2,3,11,14,15,16,17,19,22,26]

new_df = df.iloc[:, column_indeces]

print(new_df.info())
print(new_df)

# %%
print(new_df['niveles'].unique())

search_text = 'SECUNDARIA'

condition = new_df['niveles'].str.contains(search_text, na=False)
df_filtered = new_df[condition]

print(new_df['especialidad'].unique())

search_text = 'ACADÉMICA'

condition = df_filtered['especialidad'].str.contains(search_text, na=False)
df_filtered = df_filtered[condition]

print(new_df['grados'].unique())

regex_pattern = r'\b(?:8|9|10)\b'

condition_regex = df_filtered['grados'].str.contains(regex_pattern, na=False, regex=True)
df_filtered = df_filtered[condition_regex]

print(new_df['prestador_de_Servicio'].unique())

search_text = 'PERSONA NATURAL'

condition = df_filtered['prestador_de_Servicio'].str.contains(search_text, na=False)
df_filtered = df_filtered[condition]

del df_filtered['prestador_de_Servicio']

# %%
df_filtered.info()

print(df_filtered['modelos_Educativos'].unique())

search_text = 'EXTRAEDAD'

condition = df_filtered['modelos_Educativos'].str.contains(search_text, case=False, na=True)
df_filtered = df_filtered[~condition]

search_text = 'A'

condition = df_filtered['calendario'].str.contains(search_text, na=False)
df_filtered = df_filtered[condition]

del df_filtered['calendario']

# %%
df_filtered.info()
df_filtered

# %%
df_filtered.to_csv('filtered.csv', index=False)
