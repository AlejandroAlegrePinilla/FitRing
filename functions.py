import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_and_clean_csv(file_path):
    """
    Función para cargar un archivo CSV, limpiar el nombre de las columnas y mostrar las primeras filas del DataFrame.
    
    Parámetros:
        file_path (str): La ruta del archivo CSV.

    Retorna:
        pd.DataFrame: El DataFrame cargado y limpio.
    """
    # Cargar el archivo CSV
    df = pd.read_csv(file_path)
    
    # Establecer opciones de visualización
    pd.set_option("display.max_columns", None)
    
    # Limpiar los nombres de las columnas (minúsculas, sin espacios)
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    
    # Mostrar las primeras filas
    return df

def check_nulls_and_duplicates(df):
    """
    Función para identificar valores nulos y duplicados en un DataFrame.
    
    Parámetros:
        df (pd.DataFrame): El DataFrame a analizar.
        
    Retorna:
        dict: Un diccionario con dos claves:
              - 'nulls': Un DataFrame con el conteo de valores nulos por columna.
              - 'duplicates': El número total de filas duplicadas en el DataFrame.
    """
    # Identificar nulos en cada columna
    nulls_summary = df.isnull().sum().reset_index()
    nulls_summary.columns = ['Column', 'Null Count']
    nulls_summary = nulls_summary[nulls_summary['Null Count'] > 0]  # Filtra columnas con nulos
    
    # Identificar filas duplicadas
    duplicates_count = df.duplicated().sum()
    
    # Devolver los resultados en un diccionario
    return {
        'nulls': nulls_summary,
        'duplicates': duplicates_count
    }

def convert_columns_to_type(df, columns, dtype):
    """
    Convierte las columnas especificadas de un DataFrame al tipo de dato indicado.
    
    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene las columnas a convertir.
    columns (list): Una lista de nombres de las columnas a convertir.
    dtype (str): El tipo de dato al cual se convertirán las columnas (e.g., 'int64', 'float64').

    Retorna:
    pd.DataFrame: El DataFrame con las columnas convertidas al tipo especificado.
    """
    for column in columns:
        df[column] = df[column].astype(dtype)
    return df

def get_top_n_groups_by_sum(df, group_by_column, sum_column, n=5):
    """
    Función para agrupar un DataFrame por una columna, sumar los valores de otra columna 
    y retornar los N principales grupos ordenados por la suma.

    Parámetros:
        df (pd.DataFrame): El DataFrame original.
        group_by_column (str): Nombre de la columna por la cual agrupar.
        sum_column (str): Nombre de la columna cuyos valores serán sumados.
        n (int): Número de grupos principales a retornar. Por defecto es 5.

    Retorna:
        pd.DataFrame: DataFrame con los principales N grupos ordenados por la suma de los valores.
    """
    # Agrupar por la columna especificada y sumar los valores de la columna sum_column
    group_sums = df.groupby(group_by_column)[sum_column].sum().reset_index()
    
    # Ordenar por la suma en orden descendente y seleccionar los primeros N grupos
    top_n_groups = group_sums.sort_values(by=sum_column, ascending=False).head(n)
    
    return top_n_groups

def get_top_n_groups_by_mean(df, group_by_column, mean_columns, n=5):
    """
    Función para agrupar un DataFrame por una columna, calcular la media de varias columnas 
    y retornar los N principales grupos ordenados por la media de una de esas columnas.

    Parámetros:
        df (pd.DataFrame): El DataFrame original.
        group_by_column (str): Nombre de la columna por la cual agrupar.
        mean_columns (list): Lista de nombres de las columnas sobre las que calcular la media.
        n (int): Número de grupos principales a retornar. Por defecto es 5.

    Retorna:
        pd.DataFrame: DataFrame con los principales N grupos ordenados por la media de una columna.
    """
    # Agrupar por la columna especificada y calcular la media de las columnas seleccionadas
    group_means = df.groupby(group_by_column)[mean_columns].mean().reset_index()
    
    # Ordenar por la primera columna de la lista 'mean_columns' en orden descendente
    top_n_groups = group_means.sort_values(by=mean_columns[0], ascending=False).head(n)
    
    return top_n_groups

def get_top_n_groups_by_percentage(df, group_by_column, numerator_column, n=5):
    """
    Función para agrupar un DataFrame por una columna (por ejemplo, país), calcular el porcentaje
    de valores en una columna específica (por ejemplo, obesos) sobre el número total de filas
    por grupo, y retornar los N principales grupos ordenados por el porcentaje.

    Parámetros:
        df (pd.DataFrame): El DataFrame original.
        group_by_column (str): Nombre de la columna por la cual agrupar (por ejemplo, país).
        numerator_column (str): Nombre de la columna cuyos valores serán el numerador (por ejemplo, obesos).
        n (int): Número de grupos principales a retornar. Por defecto es 5.

    Retorna:
        pd.DataFrame: DataFrame con los principales N grupos ordenados por el porcentaje.
    """
    # Agrupar por la columna especificada (ej. 'country') y calcular la suma de obesos (numerador)
    # y el conteo de filas por país (denominador)
    group_sums = df.groupby(group_by_column).agg(
        total_numerator=(numerator_column, 'sum'),  # Suma de obesos por país
        total_denominator=(group_by_column, 'size')  # Número de filas por país
    ).reset_index()
    
    # Calcular el porcentaje de obesos
    group_sums['percentage'] = (group_sums['total_numerator'] / group_sums['total_denominator']) * 100
    
    # Ordenar por el porcentaje en orden descendente y seleccionar los primeros N grupos
    top_n_groups = group_sums.sort_values(by='percentage', ascending=False).head(n)
    
    return top_n_groups

def plot_obesity_percentage(top_n_groups):
    """
    Función para graficar el porcentaje de obesidad por país en un gráfico de barras horizontal.
    
    Parámetros:
        top_n_groups (pd.DataFrame): El DataFrame con columnas ['country', 'percentage'].
    """
    # Establecer el estilo de los gráficos
    sns.set(style="whitegrid")
    
    # Crear el gráfico de barras horizontal
    plt.figure(figsize=(10, 6))
    sns.barplot(x='percentage', y='country', data=top_n_groups, palette='viridis')
    
    # Añadir títulos y etiquetas
    plt.title('Top Countries by Obesity Percentage', fontsize=16)
    plt.xlabel('Obesity Percentage (%)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    
    # Mostrar los valores en las barras
    for index, value in enumerate(top_n_groups['percentage']):
        plt.text(value, index, f'{value:.2f}%', va='center', fontsize=10)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

def plot_bar_with_values(df, x_column, y_column, title, xlabel, ylabel, color='skyblue'):
    """
    Función para crear un gráfico de barras con valores sobre las barras.
    
    :param df: DataFrame con los datos a graficar
    :param x_column: Columna del DataFrame para el eje X (categorías)
    :param y_column: Columna del DataFrame para el eje Y (valores)
    :param title: Título del gráfico
    :param xlabel: Etiqueta para el eje X
    :param ylabel: Etiqueta para el eje Y
    :param color: Color de las barras (opcional, por defecto 'skyblue')
    """
    plt.figure(figsize=(10,6))
    
    # Crear el gráfico de barras
    bars = plt.bar(df[x_column], df[y_column], color=color)
    
    # Añadir título y etiquetas
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # Añadir los valores sobre las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom', fontsize=12)
    
    # Mostrar el gráfico
    plt.show()

def plot_bar_without_values(df, x_column, y_column, title, xlabel, ylabel, color='skyblue'):
    """
    Función para crear un gráfico de barras con valores sobre las barras.
    
    :param df: DataFrame con los datos a graficar
    :param x_column: Columna del DataFrame para el eje X (categorías)
    :param y_column: Columna del DataFrame para el eje Y (valores)
    :param title: Título del gráfico
    :param xlabel: Etiqueta para el eje X
    :param ylabel: Etiqueta para el eje Y
    :param color: Color de las barras (opcional, por defecto 'skyblue')
    """
    plt.figure(figsize=(10,6))
    
    # Crear el gráfico de barras
    bars = plt.bar(df[x_column], df[y_column], color=color)
    
    # Añadir título y etiquetas
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # Mostrar el gráfico
    plt.show()


def plot_bar_without_values_2(data, x_col, y_col, title, xlabel, ylabel, ax, color='b'):
    ax.bar(data[x_col], data[y_col], color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def plot_age_distribution(df, country, age_bins, age_labels):
    """
    Función para plotear la distribución de edades en un gráfico de pastel para un país específico.
    
    Parámetros:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        country (str): El país para el cual se quiere visualizar la distribución de edades.
        age_bins (list): Lista de los límites de los rangos de edad.
        age_labels (list): Lista de etiquetas para los rangos de edad.
    
    Retorna:
        None: Muestra un gráfico de pastel.
    """
    # Crear la columna de grupo de edad
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    
    # Contar la cantidad de individuos en cada grupo de edad para el país especificado
    age_group_counts = df[df["country"] == country]['age_group'].value_counts().sort_index()
    
    # Crear el gráfico de pastel
    plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'{country} Age Distribution')
    plt.show()

def plot_population_pyramid(df, country, age_bins, age_labels):
    """
    Función para plotear la pirámide de población para un país específico.
    
    Parámetros:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        country (str): El país para el cual se quiere visualizar la pirámide de población.
        age_bins (list): Lista de los límites de los rangos de edad.
        age_labels (list): Lista de etiquetas para los rangos de edad.
    
    Retorna:
        None: Muestra un gráfico de la pirámide de población.
    """
    # Filtrar el DataFrame para el país especificado
    df_country = df[df["country"] == country].copy()
    
    # Crear la columna de grupo de edad
    df_country['age_group'] = pd.cut(df_country['age'], bins=age_bins, labels=age_labels, right=False)
    
    # Contar la cantidad de individuos en cada grupo de edad por género
    age_gender_counts = df_country.groupby(['age_group', 'sex']).size().unstack().fillna(0)
    
    # Asegurarse de que las columnas de género estén en el orden correcto
    if 'Male' not in age_gender_counts.columns:
        age_gender_counts['Male'] = 0
    if 'Female' not in age_gender_counts.columns:
        age_gender_counts['Female'] = 0
    
    # Crear el gráfico de la pirámide de población
    plt.figure(figsize=(10, 8))
    plt.barh(age_gender_counts.index, age_gender_counts['Male'], color='blue', label='Male', edgecolor='black')
    plt.barh(age_gender_counts.index, -age_gender_counts['Female'], color='pink', label='Female', edgecolor='black')
    
    # Añadir títulos y etiquetas
    plt.xlabel('Number of People')
    plt.ylabel('Age Group')
    plt.title(f'Population Pyramid for {country}')
    plt.legend()
    
    # Ajustar el gráfico
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()