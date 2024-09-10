import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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