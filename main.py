import numpy as np
from src.etl import (
    load_data, clean_columns, rename_columns,
    remove_duplicate_region_columns, ensure_region_column,
    transform_dates, normalize_regions, deep_cleaning,
    create_master_dataset_simple
)

print("Loading datasets...")
dataframes = load_data()
dataframes = clean_columns(dataframes)
dataframes = rename_columns(dataframes)
dataframes = remove_duplicate_region_columns(dataframes)
dataframes = ensure_region_column(dataframes)
dataframes = transform_dates(dataframes)
dataframes = normalize_regions(dataframes)
dataframes = deep_cleaning(dataframes)

print("\nCreating master dataset (simple concat method)...")
master_df = create_master_dataset_simple(dataframes)

master_df.to_csv('data/processed/master_dataset.csv', index=False)
print("\nMaster dataset exported successfully to data/processed/master_dataset.csv!\n")


print("\n--- STATISTICAL SUMMARY (USING NUMPY) ---")

# Calcular estadísticas de la columna 'total'
total_values = master_df['total'].values

print(f"Mean total: {np.mean(total_values):,.2f}")
print(f"Standard deviation: {np.std(total_values):,.2f}")
print(f"Maximum value: {np.max(total_values):,.2f}")
print(f"Minimum value: {np.min(total_values):,.2f}")

print("--- MASTER DATASET PREVIEW ---")
print(master_df.head())
