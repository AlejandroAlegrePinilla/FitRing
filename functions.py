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

def get_top_n_groups(df, group_by_column, count_column, n=5):
    """
    Función para agrupar un DataFrame por una columna, contar las ocurrencias y retornar los N principales grupos.
    
    Parámetros:
        df (pd.DataFrame): El DataFrame original.
        group_by_column (str): Nombre de la columna por la cual agrupar.
        count_column (str): Nombre de la columna para contar las ocurrencias.
        n (int): Número de grupos principales a retornar. Por defecto es 5.

    Retorna:
        pd.DataFrame: DataFrame con los principales N grupos ordenados por la cantidad de ocurrencias.
    """
    # Agrupar por la columna especificada y contar las ocurrencias
    group_counts = df.groupby(group_by_column).size().reset_index(name=count_column)
    
    # Ordenar por el conteo en orden descendente y seleccionar los primeros N grupos
    top_n_groups = group_counts.sort_values(by=count_column, ascending=False).head(n)
    
    return top_n_groups

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