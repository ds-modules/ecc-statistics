import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

import ipywidgets as widgets


def ames_box_plots(ames):
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    neighborhoods = neighborhood_medians.index.tolist()
    midpoint = len(neighborhoods) // 2

    def plot_half(half):
        subset = neighborhoods[:midpoint] if half == "First Half" else neighborhoods[midpoint:]
        filtered_ames = ames[ames["Neighborhood"].isin(subset)]
        fig = px.box(filtered_ames, x="Neighborhood", y="SalePrice", color="Neighborhood",
                     category_orders={"Neighborhood": subset},
                     title=f"Box Plots of Sale Prices ({half})")
        fig.update_layout(xaxis_tickangle=-45)
        fig.show()

    widgets.interact(plot_half, half=widgets.ToggleButtons(options=["First Half", "Second Half"], description="Show:"))


def ames_violin_plots(ames):
    neighborhood_medians = ames.groupby("Neighborhood", observed=True)["SalePrice"].median().sort_values(ascending=False)
    neighborhoods = neighborhood_medians.index.tolist()
    midpoint = len(neighborhoods) // 2

    def plot_half(half):
        subset = neighborhoods[:midpoint] if half == "First Half" else neighborhoods[midpoint:]
        filtered_ames = ames[ames["Neighborhood"].isin(subset)]
        fig = px.violin(filtered_ames, x="Neighborhood", y="SalePrice", color="Neighborhood", box=True,
                        category_orders={"Neighborhood": subset},
                        title=f"Violin Plots of Sale Prices ({half})")
        fig.update_layout(xaxis_tickangle=-45)
        fig.show()

    widgets.interact(plot_half, half=widgets.ToggleButtons(options=["First Half", "Second Half"], description="Show:"))


def ames_histogram(ames):
    def plot_histogram(bins):
        fig = px.histogram(ames, x="SalePrice", nbins=bins, marginal="rug", title=f"Histogram of Sale Prices (Bins={bins})")
        fig.update_layout(bargap=0.05)
        fig.show()

    widgets.interact(plot_histogram, bins=widgets.IntSlider(min=5, max=50, step=5, value=25, description='Bins:'))


def penguins_box_plots(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

    def plot_boxplot(variable):
        fig = px.box(penguins, x="species", y=variable, color="species",
                     title=f"Box Plot of {variable} by Species")
        fig.update_layout(xaxis_tickangle=-45)
        fig.show()

    widgets.interact(plot_boxplot,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'))


def penguins_violin_plots(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

    def plot_violinplot(variable):
        fig = px.violin(penguins, x="species", y=variable, color="species", box=True,
                        title=f"Violin Plot of {variable} by Species")
        fig.update_layout(xaxis_tickangle=-45)
        fig.show()

    widgets.interact(plot_violinplot,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'))


def penguins_histogram(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    def plot_histogram(variable, bins):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=penguins, x=variable, hue="species", bins=bins, kde=True, alpha=0.7)
        plt.ylabel("Count")
        plt.title(f"Overlaid Histogram of {variable} by Species (Bins={bins})")
        plt.show()
    
    widgets.interact(plot_histogram,
             variable=widgets.Dropdown(options=quantitative_columns, description='Variable:'),
             bins=widgets.IntSlider(min=5, max=50, step=5, value=25, description='Bins:'))


def penguins_run_anova(penguins):
    quantitative_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

    def run_anova(feature):
        feature_groups = [penguins[penguins["species"] == sp][feature] for sp in penguins["species"].unique()]
        result = stats.f_oneway(*feature_groups)

        print(f"ANOVA on: {feature}")
        print(f"F-statistic: {result.statistic:.2f}")
        print(f"p-value: {result.pvalue:.5f}")

    widgets.interact(run_anova, feature=widgets.Dropdown(options=quantitative_columns, description="Feature:"))
