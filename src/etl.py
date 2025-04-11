import pandas as pd
import os

# Ruta base absoluta de tu proyecto
BASE_PATH = r"C:\Users\Germán\Desktop\PROYECTOEVOLVE\PROYECTOEVOLVE"

# Ruta a la carpeta data
DATA_PATH = os.path.join(BASE_PATH, 'data', 'raw')

# CSV files with meaningful names
csv_files = {
    "hotel_occupancy": "61766.csv",
    "camping_occupancy": "62492.csv",
    "tourist_accommodation": "73753.csv",
    "average_occupancy": "2017.csv",
    "total_accommodations": "67192.csv",
    "average_stay": "61767.csv"
}

# Load all dataframes
def load_data():
    dataframes = {}
    for name, file in csv_files.items():
        path = os.path.join(DATA_PATH, file)
        df = pd.read_csv(path, encoding='latin1', sep=';')
        dataframes[name] = df
    return dataframes

# Clean column names
def clean_columns(dataframes):
    for name, df in dataframes.items():
        df.columns = (
            df.columns.str.strip()
                      .str.lower()
                      .str.replace(' ', '_')
                      .str.replace('á', 'a')
                      .str.replace('é', 'e')
                      .str.replace('í', 'i')
                      .str.replace('ó', 'o')
                      .str.replace('ú', 'u')
                      .str.replace('ñ', 'n')
                      .str.replace('ç', 'c')
                      .str.replace('ï»¿', '')
        )
    return dataframes

# Rename columns to English
def rename_columns(dataframes):
    columns_mapping = {
        'comunidades_y_ciudades_autonomas': 'region',
        'comunidades_y_ciudades_autã³nomas': 'region',
        'totales_territoriales': 'region',
        'total_nacional': 'region',
        'viajeros_y_pernoctaciones': 'travellers_overnight_stays',
        'viajeros': 'travellers',
        'pernoctaciones': 'overnight_stays',
        'estancia_media_dias': 'average_stay_days',
        'ocupacion_promedio_(%)': 'occupancy_rate',
        'empleo_personal': 'employed_staff',
        'anio': 'year',
        'mes': 'month',
        'periodo': 'period',
        'total': 'total'
    }

    for name, df in dataframes.items():
        existing_cols = df.columns
        rename_dict = {col: new_col for col, new_col in columns_mapping.items() if col in existing_cols}
        df.rename(columns=rename_dict, inplace=True)

    return dataframes

def remove_duplicate_region_columns(dataframes):
    for name, df in dataframes.items():
        region_cols = [col for col in df.columns if col == 'region']
        if len(region_cols) > 1:
            # Nos quedamos solo con la primera columna 'region'
            cols_to_keep = df.columns.drop(region_cols[1:])  # Quitamos duplicadas
            df = df[cols_to_keep]
            dataframes[name] = df
    return dataframes

def ensure_region_column(dataframes):
    for name, df in dataframes.items():
        if 'region' not in df.columns:
            df['region'] = 'total national'
        dataframes[name] = df
    return dataframes

# Transform date columns
def transform_dates(dataframes):
    for name, df in dataframes.items():
        if 'period' in df.columns:
            df['year'] = df['period'].str[:4].astype(int)
            df['month'] = df['period'].str[-2:].astype(int)
    return dataframes

# Normalize region names
def normalize_regions(dataframes):
    for name, df in dataframes.items():
        if 'region' in df.columns:
            try:
                # Convertimos todo a string sí o sí
                df['region'] = df['region'].astype(str)
                df['region'] = df['region'].fillna('total national')
                df['region'] = df['region'].str.strip().str.lower()

                df['region'] = df['region'].str.replace('á', 'a')\
                                            .str.replace('é', 'e')\
                                            .str.replace('í', 'i')\
                                            .str.replace('ó', 'o')\
                                            .str.replace('ú', 'u')\
                                            .str.replace('ñ', 'n')

                df['region'] = df['region'].replace({
                    'castilla - la mancha': 'castilla-la mancha'
                })

            except Exception as e:
                print(f"Error cleaning region column in dataset {name}: {e}")
                continue  # Salta a otro dataset sin romper el flujo

    return dataframes

# Clean and translate values
def clean_and_translate_values(dataframes):
    for name, df in dataframes.items():
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].str.strip().str.lower()
                df[col] = df[col].replace({
                    'total nacional': 'total national',
                    'viajero': 'traveller',
                })
    return dataframes

# Drop irrelevant columns
def drop_irrelevant_columns(dataframes):
    columns_to_remove = ['operation', 'residencia', 'travellers_overnight_stays',
                         'totales_territoriales', 'total_nacional']
    for name, df in dataframes.items():
        cols_to_drop = [col for col in df.columns if col in columns_to_remove]
        df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    return dataframes

# Final cleaning
def final_cleaning(dataframes):
    for name, df in dataframes.items():
        columns_to_drop = [col for col in df.columns if 'nivel' in col or 'operacion' in col]
        df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        df.fillna(0, inplace=True)
    return dataframes

# Export clean data to CSV
def export_clean_data(dataframes):
    output_path = os.path.join(DATA_PATH, 'data', 'processed')
    os.makedirs(output_path, exist_ok=True)
    for name, df in dataframes.items():
        output_file = os.path.join(output_path, f"{name}_clean.csv")
        df.to_csv(output_file, index=False)

def deep_cleaning(dataframes):
    for name, df in dataframes.items():

        # Clean special characters in column names explicitly
        df.columns = (
            df.columns.str.lower()
                      .str.strip()
                      .str.replace('á', 'a')
                      .str.replace('é', 'e')
                      .str.replace('í', 'i')
                      .str.replace('ó', 'o')
                      .str.replace('ú', 'u')
                      .str.replace('ñ', 'n')
                      .str.replace('ç', 'c')
                      .str.replace('ã³', 'o')
                      .str.replace('ï»¿', '')
        )

        # Rename explicitly incorrect column names
        df.rename(columns={
            'operacion': 'operation',
            'operacia3n': 'operation',
            'comunidades_y_ciudades_autonomas': 'region',
            'comunidades_y_ciudades_auta3nomas': 'region'
        }, inplace=True)

        # Drop constant or irrelevant columns
        irrelevant_cols = ['operation', 'residencia', 'travellers_overnight_stays']
        constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
        df.drop(columns=constant_cols + irrelevant_cols, inplace=True, errors='ignore')

        # Clean numeric columns
        numeric_cols = ['total']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        # Fix period formatting
        if 'period' in df.columns:
            df['period'] = df['period'].str.replace('m', '-')

        # Correct strange text values
        df.replace({
            'encuesta de ocupacion hotelera': 'hotel occupancy survey',
            'total nacional': 'total national',
            'viajero': 'traveller'
        }, inplace=True)

        # Replace zeroes or missing values in "region" (CORRECCIÓN FINAL AQUÍ)
        if 'region' in df.columns:
            df['region'] = df['region'].replace(['0', 0, ''], 'total national')
            df['region'].fillna('total national', inplace=True)

    return dataframes

def create_master_dataset_simple(dataframes, start_year=2022, end_year=2025):
    dfs = []

    for name, df in dataframes.items():
        # Nos quedamos solo con columnas importantes
        keep_cols = [col for col in df.columns if col in ['year', 'month', 'region', 'total']]
        
        temp_df = df[keep_cols].copy()

        # Añadimos la columna source para saber de dónde viene cada fila
        temp_df['source'] = name

        # Filtramos por años deseados
        temp_df = temp_df[(temp_df['year'] >= start_year) & (temp_df['year'] <= end_year)]

        dfs.append(temp_df)

    # Concatenamos todos
    master_df = pd.concat(dfs, ignore_index=True)

    # Creamos period
    master_df['period'] = master_df.apply(lambda row: f"{int(row['year']):04d}-{int(row['month']):02d}", axis=1)

    # Reemplazar NaN en region por 'total national'
    master_df['region'] = master_df['region'].fillna('total national')


    return master_df
