import pandas as pd
import matplotlib.pyplot as plt


def generate_country_to_price_relation():
    x = list(pd.value_counts(df["country"]).iloc[:5].index)
    y = [df.loc[df['country'] == country]["price"].mean() for country in x]
    fig, ax = plt.subplots()
    ax.set_title("Average price in countries")
    ax.set_ylabel("Average price (in US dollars)")
    plt.title("Which country has the most expensive wine?")
    ax.set_ylim(0, 60)
    rects = ax.bar(x, y, color=['red', 'blue', 'green', 'yellow', 'orange'])
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '$%d' % int(height),
                ha='center', va='bottom')
    plt.show()
    fig.savefig("graphs/relations/" + "country_price" + "_relation.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)
y = []
generate_country_to_price_relation()