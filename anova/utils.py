import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns

from ipywidgets import interact, widgets
from utils import *

def ames_box_plots(ames):
    # Manually computing the median sale price for each neighborhood for ordering purposes
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    ames["Neighborhood"] = pd.Categorical(ames["Neighborhood"], categories=neighborhood_medians.index, ordered=True)
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=ames, x="Neighborhood", y="SalePrice", hue="Neighborhood", order=neighborhood_medians.index)
    plt.xticks(rotation=45)
    plt.title("Box Plots of Sale Prices Across Neighborhoods")
    plt.show()

def ames_violin_plots(ames):
    # Manually computing the median sale price for each neighborhood for ordering purposes
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    ames["Neighborhood"] = pd.Categorical(ames["Neighborhood"], categories=neighborhood_medians.index, ordered=True)
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=ames, x="Neighborhood", y="SalePrice", hue="Neighborhood", order=neighborhood_medians.index)
    plt.xticks(rotation=45)
    plt.title("Violin Plots of Sale Prices Across Neighborhoods")
    plt.show()

def ames_histogram(ames):
    
    def plot_histogram(bins):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=ames, x="SalePrice", bins=bins, kde=True, alpha=0.7)
        plt.ylabel("Count")
        plt.title(f"Histogram of Sale Prices (Bins={bins})")
        plt.show()
    
    interact(plot_histogram, bins=widgets.IntSlider(min=5, max=50, step=5, value=25, description='Bins:'));

def penguins_box_plots(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    def plot_boxplot(variable):
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=penguins, x="species", y=variable, hue="species")
        plt.ylabel(variable.replace('_', ' ').title())
        plt.title(f"Box Plot of {variable} by Species")
        plt.xticks(rotation=45)
        plt.show()
    
    interact(plot_boxplot,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'))

def penguins_violin_plots(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    def plot_violinplot(variable):
        plt.figure(figsize=(12, 6))
        sns.violinplot(data=penguins, x="species", y=variable, hue="species")
        plt.ylabel(variable.replace('_', ' ').title())
        plt.title(f"Violin Plot of {variable} by Species")
        plt.xticks(rotation=45)
        plt.show()
    
    interact(plot_violinplot,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'))

def penguins_histogram(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    def plot_histogram(variable, bins):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=penguins, x=variable, hue="species", bins=bins, kde=True, alpha=0.7)
        plt.ylabel("Count")
        plt.title(f"Overlaid Histogram of {variable} by Species (Bins={bins})")
        plt.show()
    
    interact(plot_histogram,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'),
             bins=widgets.IntSlider(min=5, max=50, step=5, value=25, description='Bins:'))

def penguins_run_anova(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
        
    def run_anova(feature):
        feature_groups = []
        for species in penguins["species"].unique():
            group = penguins[penguins["species"] == species][feature]
            feature_groups.append(group)
        result = stats.f_oneway(*feature_groups)
    
        print(f"ANOVA on: {feature}")
        print(f"F-statistic: {result.statistic:.2f}")
        print(f"p-value: {result.pvalue:.5f}")
    
    # Display interactive dropdown
    widgets.interact(run_anova, feature=widgets.Dropdown(options=quantitative_columns, description="Feature:"))