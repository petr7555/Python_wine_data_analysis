import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def best_value():
    df["Result"] = df["points"] / df["price"]
    largest = df.nlargest(20, "Result").sort_values(by=["Result"], ascending=False)

    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x="Result", y="variety", data=largest)
    for p in ax.patches:
        x = p.get_bbox().get_points()[:, 0]
        y = p.get_bbox().get_points()[1, 1]
        # Set the allignment of the text
        ax.annotate(str(x[1]), (x[1]+0.2, y-0.1),
                    ha='left', va='bottom')
        plt.title("Which wines are the best for the smallest price?")
        ax.set_xlabel("Points/price")

    plt.show()
    plt.savefig("graphs/relations/" + "best_value_wines.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)

best_value()
