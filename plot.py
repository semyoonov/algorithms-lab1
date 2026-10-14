import os
import pandas as pd
import matplotlib.pyplot as plt

def save_plot(df, scenario, x_col, xlabel, title, filename):
    plt.figure(figsize=(9, 5))
    data = df[df["scenario"] == scenario]

    for algo, group in data.groupby("algorithm"):
        plt.plot(group[x_col], group["time_sec"], marker="o", label=algo)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(xlabel)
    plt.ylabel("Время (секунды)")
    plt.title(title)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"plots/{filename}", dpi=200)
    plt.close()

def generate_plots():
    os.makedirs("plots", exist_ok=True)
    df = pd.read_csv("data/results.csv")
    save_plot(df, "equal_sizes", "n", "Размер N (при M = N)", "M = N", "equal_sizes.png")
    save_plot(df, "fixed_m", "n", "Размер N (при M = 50)", "M << N (M = 50)", "fixed_m.png")
    save_plot(df, "varying_ratio", "ratio", "Отношение N / M", "Зависимость от N / M", "varying_ratio.png")