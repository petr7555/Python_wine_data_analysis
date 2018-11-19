import pandas as pd
import matplotlib.pyplot as plt


def generate_points_to_price_relation():
    x = [i for i in range(80, 101)]
    y = [df.loc[df['points'] == i]["price"].mean() for i in range(80, 101)]
    fig, ax = plt.subplots()
    ax.set_title("How do points correspond to the price?")
    ax.set_xlabel("Points")
    ax.set_ylabel("Average price [$]")
    plt.plot(x, y)
    plt.show()
    fig.savefig("graphs/relations/" + "points_price" + "_relation.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)

generate_points_to_price_relation()
