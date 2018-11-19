import pandas as pd
import matplotlib.pyplot as plt


def generate_word_frequency_graph(column, title):
    plt.figure(figsize=(12, 8))
    freq = df.description.str.split(expand=True).stack().value_counts().iloc[:30]
    p = freq.plot.barh()
    fig = p.get_figure()
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()
    fig.savefig("graphs/frequency_analysis/" + column + "_frequency_analysis.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)

generate_word_frequency_graph("description", "Most frequent words used to describe wine")
