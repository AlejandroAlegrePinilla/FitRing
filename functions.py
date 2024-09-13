import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_and_clean_csv(file_path):
    """
    Function to load a CSV file and clean its columns.
    """
   
    df = pd.read_csv(file_path)
    
    # Set the display option to show all columns
    pd.set_option("display.max_columns", None)

    # Clean the column names by making them lowercase, stripping whitespace and replacing spaces with underscores
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    

def check_nulls_and_duplicates(df):
    """
    Function to identify null values and duplicate rows in a DataFrame.
    """
    # Identify null values in each column
    # Create a boolean mask to identify null values in each column
    # Sum the boolean mask to get the count of null values per column
    # Reset the index to convert the Series to a DataFrame
    nulls_summary = df.isnull().sum().reset_index()
    # Rename the columns of the DataFrame
    nulls_summary.columns = ['Column', 'Null Count']
    # Filter the DataFrame to only include columns with null values
    nulls_summary = nulls_summary[nulls_summary['Null Count'] > 0]

    # Identify duplicate rows
    # Use the duplicated method to identify duplicate rows
    # Sum the boolean mask to get the total number of duplicate rows
    duplicates_count = df.duplicated().sum()

    # Return the results in a dictionary
    return {
        'nulls': nulls_summary,
        'duplicates': duplicates_count
    }

def convert_columns_to_type(df, columns, dtype):
    """
    Converts columns in a DataFrame to the specified data type.
    """
    # Iterate through the list of columns and convert each one to the specified dtype
    for column in columns:
        # Use the astype method to convert the column to the specified data type
        df[column] = df[column].astype(dtype)
    # Return the DataFrame with the converted columns
    return df

def get_top_n_groups_by_sum(df, group_by_column, sum_column, n=5):
    """
    Function to group a DataFrame by a column, sum the values of another column and return the top N groups ordered by the sum.
    """
    # Group the DataFrame by the specified column and sum the values of the specified column
    group_sums = df.groupby(group_by_column)[sum_column].sum().reset_index()
    
    # Sort the DataFrame by the sum in descending order and select the top N groups
    top_n_groups = group_sums.sort_values(by=sum_column, ascending=False).head(n)
    
    return top_n_groups


def get_top_n_groups_by_mean(df, group_by_column, mean_columns, n=5):
    """
    Function to group a DataFrame by a column, calculate the mean of multiple columns
    and return the top N groups ordered by the mean of one of those columns.
    """
    # Group the DataFrame by the specified column and calculate the mean of the specified columns
    group_means = df.groupby(group_by_column)[mean_columns].mean().reset_index()

    # Sort the DataFrame by the mean of the first column in the list 'mean_columns' in descending order
    top_n_groups = group_means.sort_values(by=mean_columns[0], ascending=False).head(n)

    # Return the DataFrame with the top N groups
    return top_n_groups

def get_top_n_groups_by_percentage(df, group_by_column, numerator_column, n=5):
    """
    Function to group a DataFrame by a column, calculate the percentage of values in a specific column
    and return the top N groups ordered by the percentage.
    """
    # Group the DataFrame by the specified column
    group_sums = df.groupby(group_by_column).agg(
        # Calculate the sum of the numerator column (obese)
        total_numerator=(numerator_column, 'sum'), 
        # Calculate the total number of rows per group (denominator)
        total_denominator=(group_by_column, 'size')
    ).reset_index()
    
    # Calculate the percentage of the numerator column
    group_sums['percentage'] = (group_sums['total_numerator'] / group_sums['total_denominator']) * 100
    
    # Sort the DataFrame by the percentage in descending order and select the top N groups
    top_n_groups = group_sums.sort_values(by='percentage', ascending=False).head(n)
    
    return top_n_groups


def plot_obesity_percentage(top_n_groups):
    """
    Function to plot the obesity percentage by country in a horizontal bar chart.
    """
    # Set the style of the plots
    sns.set(style="whitegrid")
    
    # Create the horizontal bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x='percentage', y='country', data=top_n_groups, palette='viridis')
    
    # Add titles and labels
    plt.title('Top Countries by Obesity Percentage', fontsize=16)
    plt.xlabel('Obesity Percentage (%)', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    
    # Show the values on the bars
    for index, value in enumerate(top_n_groups['percentage']):
        plt.text(value, index, f'{value:.2f}%', va='center', fontsize=10)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_bar_with_values(df, x_column, y_column, title, xlabel, ylabel, color='skyblue'):
    """
    Function to create a bar chart with values on the bars.
    """
    # Create the figure and set the size
    plt.figure(figsize=(10,6))
    
    # Create the bar chart
    bars = plt.bar(df[x_column], df[y_column], color=color)
    
    # Add title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # Add the values on the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom', fontsize=12)
    
    # Show the plot
    plt.show()

def plot_bar_without_values(df, x_column, y_column, title, xlabel, ylabel, color='skyblue'):
    """
    Function to create a bar chart with values on the bars.
    """
    # Create the figure and set the size
    plt.figure(figsize=(10,6))
    
    # Create the bar chart
    bars = plt.bar(df[x_column], df[y_column], color=color)
    
    # Add title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # Show the plot
    plt.show()


def plot_bar_without_values_2(data, x_col, y_col, title, xlabel, ylabel, ax, color='b'):
    """
    Function to create a bar chart with values on the bars using an existing axes.  
    """
    # Create the bar chart
    ax.bar(data[x_col], data[y_col], color=color)
    # Add title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def plot_age_distribution(df, country, age_bins, age_labels):
    """
    Function to plot the age distribution in a pie chart for a specific country.
    """
    # Create a new column with the age groups
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    
    # Count the number of individuals in each age group for the specific country
    age_group_counts = df[df["country"] == country]['age_group'].value_counts().sort_index()
    
    # Plot the age distribution in a pie chart
    plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'{country} Age Distribution')
    plt.show()

def plot_population_pyramid(df, country, age_bins, age_labels):
    """
    Function to plot the population pyramid for a specific country.SS
    """
    # Filter the DataFrame for the specific country
    df_country = df[df["country"] == country].copy()
    
    # Create the age group column
    df_country['age_group'] = pd.cut(df_country['age'], bins=age_bins, labels=age_labels, right=False)
    
    # Count the number of individuals in each age group for each gender
    age_gender_counts = df_country.groupby(['age_group', 'sex']).size().unstack().fillna(0)
    
    # Make sure the gender columns are in the correct order
    if 'Male' not in age_gender_counts.columns:
        age_gender_counts['Male'] = 0
    if 'Female' not in age_gender_counts.columns:
        age_gender_counts['Female'] = 0
    
    # Create the population pyramid plot
    plt.figure(figsize=(10, 8))
    plt.barh(age_gender_counts.index, age_gender_counts['Male'], color='blue', label='Male', edgecolor='black')
    plt.barh(age_gender_counts.index, -age_gender_counts['Female'], color='pink', label='Female', edgecolor='black')
    
    # Add title and labels
    plt.xlabel('Number of People')
    plt.ylabel('Age Group')
    plt.title(f'Population Pyramid for {country}')
    plt.legend()
    
    # Adjust the plot
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
