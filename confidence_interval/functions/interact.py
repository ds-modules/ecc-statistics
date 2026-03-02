"""
Interact module for the Confidence Interval notebook.
Provides the interactive widget for exploring how sample size and confidence level
affect the width of a confidence interval for the mean.
"""

import numpy as np
from scipy import stats
import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display


def _update_ci_plot(population, n, confidence_level, out):
    """Draw a sample, compute CI, and plot histogram with CI and width."""
    with out:
        out.clear_output(wait=True)
        sample = np.random.choice(population, size=n, replace=False)
        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1)

        alpha = 1 - confidence_level
        z = stats.norm.ppf(1 - alpha / 2)
        se = sample_std / np.sqrt(n)
        ci_low = sample_mean - z * se
        ci_high = sample_mean + z * se
        width = ci_high - ci_low

        fig, ax = plt.subplots(figsize=(10, 5.5), facecolor="white")
        ax.set_facecolor("#fafafa")

        bins = min(28, max(6, n // 4))
        n_hist, _, patches = ax.hist(
            sample, bins=bins, color="#4a90d9", edgecolor="white", linewidth=1.2,
            density=True, alpha=0.85, label="Sample distribution"
        )
        ax.axvspan(ci_low, ci_high, alpha=0.18, color="#c44e52", zorder=0)
        ax.axvline(ci_low, color="#c44e52", linestyle="-", linewidth=2.5, label=f"{int(confidence_level * 100)}% CI")
        ax.axvline(ci_high, color="#c44e52", linestyle="-", linewidth=2.5)
        ax.axvline(sample_mean, color="#2d2d2d", linestyle="--", linewidth=2, label=f"Sample mean = {sample_mean:.2f}")

        ax.set_xlabel("Study hours", fontsize=12, color="#333")
        ax.set_ylabel("Density", fontsize=12, color="#333")
        ax.tick_params(colors="#555", labelsize=10)
        ax.set_ylim(bottom=0)
        ymax = ax.get_ylim()[1]
        xmin, xmax = ax.get_xlim()
        # Stack Lower/Upper CI in upper-left so they never overlap
        ci_text = f"Lower CI = {ci_low:.2f}\nUpper CI = {ci_high:.2f}"
        ax.text(xmin + (xmax - xmin) * 0.02, ymax * 0.94, ci_text, fontsize=10, color="#c44e52",
                ha="left", va="top", fontweight="bold", linespacing=1.4,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#c44e52", alpha=0.95))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.2f}"))
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(True, axis="y", alpha=0.35, linestyle="--")
        ax.legend(loc="upper right", frameon=True, fancybox=True, shadow=True, fontsize=10)

        title = f"Sample size n = {n}   →   {int(confidence_level * 100)}% CI = ({ci_low:.2f}, {ci_high:.2f})   →   Width = {width:.2f} hours"
        ax.set_title(title, fontsize=12, color="#333", pad=12)
        plt.tight_layout()
        plt.show()


def interact_ci(population):
    """Run the interactive widget: histogram, CI lines, and width update with n and confidence level."""
    n_slider = widgets.IntSlider(
        min=10, max=200, step=10, value=40,
        description="Sample size (n):",
        style={"description_width": "140px"},
        layout=widgets.Layout(width="320px"),
    )
    level_slider = widgets.FloatSlider(
        min=0.80, max=0.99, step=0.01, value=0.95,
        description="Confidence level:",
        style={"description_width": "140px"},
        layout=widgets.Layout(width="320px"),
    )
    out = widgets.Output()

    def on_change(change=None):
        _update_ci_plot(population, n_slider.value, level_slider.value, out)

    n_slider.observe(on_change, names="value")
    level_slider.observe(on_change, names="value")

    box = widgets.VBox([widgets.HBox([n_slider, level_slider]), out])
    display(box)
    on_change()
