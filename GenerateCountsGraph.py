import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def generate_graph(column, title):
    ncount = len(df)

    plt.figure(figsize=(12, 8))
    ax = sns.countplot(x=column, data=df, order=pd.value_counts(df[column]).iloc[:5].index)

    plt.title(title)

    # Make twin axis
    ax2 = ax.twinx()

    # Switch so count axis is on right, frequency on left
    ax2.yaxis.tick_left()
    ax.yaxis.tick_right()

    # Also switch the labels over
    ax.yaxis.set_label_position('right')
    ax2.yaxis.set_label_position('left')

    ax2.set_ylabel('Frequency [%]')
    ax.set_xlabel(None)

    for p in ax.patches:
        x = p.get_bbox().get_points()[:, 0]
        y = p.get_bbox().get_points()[1, 1]
        # Set the alignment of the text
        ax.annotate('{:.1f}%'.format(100. * y / ncount), (x.mean(), y),
                    ha='center', va='bottom')

    # Use a LinearLocator to ensure the correct number of ticks
    ax.yaxis.set_major_locator(ticker.LinearLocator(11))

    # Fix the frequency range to 0-100
    ax2.set_ylim(0, 100)

    # Use a MultipleLocator to ensure a tick spacing of 10
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

    # Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
    ax2.grid(None)
    plt.savefig("graphs/value_counts/" + column + "_value_counts.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)
columns = ["country", "province", "region_1", "region_2", "variety", "winery"]
titles = ["The country that the wine is from",
          "The province or state that the wine is from",
          "The wine growing area in a province or state",
          "More specific regions specified within a wine growing area",
          "The type of grapes used to make the wine",
          "The winery that made the wine"]
for i in range(len(columns)):
    generate_graph(columns[i], titles[i])
