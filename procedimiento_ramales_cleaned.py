# -*- coding: utf-8 -*-
"""
Ramal Filtering Tool for GPS Data — Developed for SEMOVI
Author: Diego Magaña
Date: April 2024
"""

import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv('ruta_3_marzo.csv')  # Replace with your local path if needed

# Get total number of columns and their names
total_columns = len(df.columns)
column_names = df.columns.tolist()

# Ensure 'Placa' field is treated as string
df['Placa'] = df['Placa'].astype(str)

# Get all unique values in the 'Placa' column
unique_plates = df['Placa'].unique().tolist()

# Print column metadata and unique vehicle IDs
print("Total columns:", total_columns)
print("Column names:", column_names)
print("Unique values in 'Placa' column:", unique_plates)

# Filter records by specific vehicle IDs
filtered_records = df[df['Placa'].isin([
    '30014', '30033', '30083', '30093', '30140', '30229', '30244', '30265', '30287', '30298',
    '30303', '30366', '30437', '30459', '30514', '30516', '30517', '30547', '30627', '30653',
    '30654', '30711', '30816'
])]

# Save filtered records to a new CSV file
filtered_records.to_csv('filtered_records.csv', index=False)

# Save unique vehicle IDs to a separate CSV
df_unique_plates = pd.DataFrame(unique_plates, columns=['Placa'])
df_unique_plates.to_csv('unique_plates.csv', index=False)
