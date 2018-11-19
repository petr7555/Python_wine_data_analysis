import pandas as pd
import matplotlib.pyplot as plt


def generate_histogram(column, title, range, labels):
    plt.figure(figsize=(12, 8))
    x = df[df[column].notnull()][column]
    bins = int(range[1] - range[0])
    plt.hist(x, bins, facecolor='green', alpha=0.75, range=range)
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.savefig("graphs/histograms/" + column + "_histogram.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)
columns = ["points", "price"]
titles = ["Points\nThe number of points WineEnthusiast rated the wine on a scale of 1-100 ",
          "Price\nThe cost for a bottle of the wine"]
labels = [["Points", "Counts"], ["Price", "Counts"]]
generate_histogram(columns[0], titles[0], (80, 100), labels[0])
mu = df[columns[1]].mean()
generate_histogram(columns[1], titles[1], (0, mu + 50), labels[1])
