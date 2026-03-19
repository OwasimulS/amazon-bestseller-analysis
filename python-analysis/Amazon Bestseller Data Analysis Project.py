import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("bestsellers with categories.csv") #read the csv file
df["Review_Range"] = pd.cut(df["Reviews"], bins=[0,10000,20000,30000, 40000, 50000, 60000, 70000, 80000, 90000]) #create a new column with the review range, split into 3 bnsi
result = df.groupby("Review_Range")["User Rating"].mean().reset_index() #group by the review range and calculate the mean of the user rating
result = result.sort_values("Review_Range") #sort the result by the review range

result.plot(x="Review_Range", y="User Rating", kind="bar", legend=False, figsize=(10,6)) #plot the result as a bar chart
plt.title("Number of Reviews vs Average Rating")
plt.xlabel("Review Range")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.ylim(4.0, 5.0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("reviews_vs_rating.png")
plt.show()


df["Price_Range"]=pd.cut(df["Price"], bins=[0,10,20,30,40,50,60,70,80,90,100,110]) #create a new column with the price range, split into multiple
price_result = df.groupby("Price_Range")["User Rating"].mean().reset_index() #group by the price range and calculate the mean of the user rating
price_result = price_result.sort_values("Price_Range") #sort the result by the price range

price_result.plot(x="Price_Range", y="User Rating", kind="bar", legend=False, figsize=(10,6)) #plot the result as a bar chart
plt.title("Price vs Average Rating")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.ylim(4.0, 5.0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()