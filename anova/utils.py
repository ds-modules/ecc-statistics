import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns

from ipywidgets import interact, widgets
from utils import *

def box_plots(ames):
    # Manually computing the median sale price for each neighborhood for ordering purposes
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    ames["Neighborhood"] = pd.Categorical(ames["Neighborhood"], categories=neighborhood_medians.index, ordered=True)
    
    # Plot with the ordered x-axis
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=ames, x="Neighborhood", y="SalePrice", hue="Neighborhood", order=neighborhood_medians.index)
    plt.xticks(rotation=45)
    plt.title("Box Plots of Sale Prices Across Neighborhoods")
    plt.show()

def violin_plots(ames):
    # Manually computing the median sale price for each neighborhood for ordering purposes
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    ames["Neighborhood"] = pd.Categorical(ames["Neighborhood"], categories=neighborhood_medians.index, ordered=True)
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=ames, x="Neighborhood", y="SalePrice", hue="Neighborhood", order=neighborhood_medians.index)
    plt.xticks(rotation=45)
    plt.title("Violin Plots of Sale Prices Across Neighborhoods")
    plt.show()

def histogram(ames):
    def plot_histogram(bins):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=ames, x="SalePrice", bins=bins, kde=True, alpha=0.7)
        plt.ylabel("Count")
        plt.title(f"Histogram of Sale Prices (Bins = {bins})")
        plt.show()
    
    interact(plot_histogram, bins=widgets.IntSlider(min=5, max=50, step=5, value=25));