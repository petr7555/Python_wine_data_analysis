import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def worst_value():
    df["Result"] = df["points"]/df["price"]
    smallest = df.nsmallest(20, "Result").sort_values(by=["Result"],  ascending=True)

    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x="Result", y="variety", data=smallest)
    for p in ax.patches:
        x = p.get_bbox().get_points()[:, 0]
        y = p.get_bbox().get_points()[1, 1]
        # Set the allignment of the text
        ax.annotate(str(round(x[1], 3)), (x[1]+0.001, y-0.02),
                    ha='left', va='bottom')
        plt.title("Which wines are the worst for the biggest price?")
        ax.set_xlabel("Points/price")

    plt.show()
    plt.savefig("graphs/relations/" + "worst_value_wines.png")


path = "C:\\Users\\janikp\\AppData\\Local\\Programs\\Python\\Python37-32\\Projekt 2\\input\\winemag-data_first150k_id.csv"
df = pd.read_csv(path)

worst_value()
