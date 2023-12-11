# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 01:13:34 2023

@author: ACER
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_energy_csv(file_path):
    """Read the CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def extract_energy_data(df, series_name):
    """Extract data for a specific series name."""
    return df[df['Series Name'] == series_name]

def apply_energy_plot_style(title=None, x_label=None, y_label=None):
    """Apply a common style to the plots."""
    if title:
        plt.title(title)
    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    plt.legend()

def plot_energy_multiline(data, x_values, title=None):
    """
    Create a multiline graph for the provided data.

    Parameters:
    - data: DataFrame, data for multiple countries
    - x_values: list, x-axis values (e.g., years)
    - title: str or None, title of the graph (optional)
    """
    plt.figure(figsize=(12, 8))
    
    for index, row in data.iterrows():
        plt.plot(x_values, row[4:], label=row['Country Name'], marker='o')

    # Apply the common style
    apply_energy_plot_style(title, 'Year', 'Energy Imports as a Percentage of Energy Use (2001-2010)')

    # Print the values used for the plot
    print("Values used for multiline graph:")
    print("x_values:", x_values)
    for index, row in data.iterrows():
        print(f"{row['Country Name']}:", row[4:])

    # Show the plot
    plt.show()

def plot_energy_bar(data, x_values, title=None, country_names=None):
    """
    Create a bar plot for the provided data.

    Parameters:
    - data: DataFrame, data for specific countries
    - x_values: list, x-axis values (e.g., years)
    - title: str or None, title of the graph (optional)
    - country_names: list or None, names of the countries (optional)
    """
    plt.figure(figsize=(12, 8))

    for country_name in country_names:
        country_data = data[data['Country Name'] == country_name]
        plt.bar(x_values, country_data.iloc[0, 4:], label=country_name)

    # Apply the common style
    apply_energy_plot_style(title, 'Year', 'Energy Imports as a Percentage of Energy Use (2001-2010)')

    # Print the values used for the plot
    print("Values used for bar plot:")
    print("x_values:", x_values)
    for country_name in country_names:
        country_data = data[data['Country Name'] == country_name]
        print(f"{country_name}:", country_data.iloc[0, 4:])

    # Show the plot
    plt.show()

def plot_pie_chart(data, title, country_name):
    """
    Create a pie chart for the provided data.

    Parameters:
    - data: DataFrame, data for a specific country
    - title: str, title of the pie chart
    - country_name: str, name of the country
    """
    plt.figure(figsize=(8, 8))
    plt.pie(data.iloc[0, 4:], labels=data.columns[4:], autopct='%1.1f%%', startangle=90)
    plt.title(f'Energy imports, net (% of energy use) in {country_name}')
    # Print the values used for the pie chart
    print("Values used for pie chart:")
    print(f"{country_name}:", data.iloc[0, 4:])
    # Show the pie chart
    plt.show()

def main():
    """Main function to demonstrate the usage of the visualization functions."""
    # Example usage for multiline graph
    file_path = r"C:\Users\ACER\Downloads\Energy imports, net (% of energy use).csv"
    df = read_energy_csv(file_path)

    series_name = 'Energy imports, net (% of energy use)'
    countries_data = extract_energy_data(df, series_name)

    x_values = df.columns[4:]
    title_multiline = 'Energy imports, net (% of energy use) - All Countries'

    plot_energy_multiline(countries_data, x_values, title_multiline)

    # Example usage for bar plot (United States and United Kingdom)
    selected_countries = ['United States', 'United Kingdom']
    title_bar_multiple_countries = 'Energy imports, net (% of energy use) - United States and United Kingdom'

    plot_energy_bar(df, x_values, title_bar_multiple_countries, country_names=selected_countries)

    # Example usage for pie chart (United States)
    # Example usage for pie chart (United States)
    us_data = df[df['Country Name'] == 'United States']
    title_pie_us = 'Energy imports, net (% of energy use) in United States'

    plot_pie_chart(us_data, title_pie_us, 'United States')

    # Example usage for pie chart (India)
    india_data = df[df['Country Name'] == 'India']
    title_pie_india = 'Energy imports, net (% of energy use) in India'

    plot_pie_chart(india_data, title_pie_india, 'India')

# Call the main function
if __name__ == "__main__":
    main()
