import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fair_die_means(n_samples, sample_size, population):
    sample_means = [np.mean(np.random.choice(population, size=sample_size)) for _ in range(n_samples)]

    plt.figure(figsize=(12, 6))
    sns.histplot(x=sample_means, bins=25, binrange=(1,6.0001), color='red')
    plt.axvline(np.mean(sample_means), color='green', linestyle='dashed')
    plt.title("Distribution of Sample Means (n=5 die rolls)")
    plt.xlabel("Sample Means")
    plt.ylabel("Frequency")
    
    plt.text(np.mean(sample_means)+0.15, 990, f"Mean: {np.mean(sample_means):.2f}", color='green')
    plt.text(4.5, 825, "Approximately\nnormal", fontsize=24, color='black')
    plt.show()

def fair_die_variances(n_samples, sample_size, population):
    sample_variances = [np.var(np.random.choice(population, size=sample_size), ddof=1) for _ in range(n_samples)]

    plt.figure(figsize=(12, 6))
    sns.histplot(x=sample_variances, bins=30, color='red', edgecolor='black', stat='frequency')
    plt.axvline(np.mean(sample_variances), color='green', linestyle='dashed')
    plt.title("Distribution of Sample Variances (n=5 die rolls)")
    plt.xlabel("Sample Variances")
    plt.ylabel("Frequency")
    
    plt.text(np.mean(sample_variances)+0.1, 3250, f"Mean: {np.mean(sample_variances):.2f}", color='green')
    plt.text(6, 3100, "Skewed", fontsize=20, color='black')
    plt.show()

def fair_die_proportions(n_samples, sample_size, population):
    sample_proportions = [np.sum(np.random.choice(population, size=sample_size) % 2 == 1) / sample_size for _ in range(n_samples)]

    plt.figure(figsize=(12, 6))
    sns.histplot(x=sample_proportions, bins=6, color='red', edgecolor='black', stat='frequency')
    plt.axvline(np.mean(sample_proportions), color='green', linestyle='dashed')
    plt.title("Distribution of Sample Proportions (n=5 die rolls)")
    plt.xlabel("Sample Proportions")
    plt.ylabel("Frequency")
    
    plt.text(np.mean(sample_proportions)+0.02, 18800, f"Mean: {np.mean(sample_proportions):.3f}", color='green')
    plt.text(0.75, 15000, "Approximately\nnormal", fontsize=20, color='black')
    plt.show()