import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# Load the Excel file
file_path = "./Data/Pen Sales Data.xlsx"
xls = pd.ExcelFile(file_path)

# Load data from sheets
pen_sales_df = pd.read_excel(xls, sheet_name="Pen Sales")
pen_costs_df = pd.read_excel(xls, sheet_name="Pen Costs")

# Convert date columns to datetime
pen_sales_df["Purchase Date"] = pd.to_datetime(pen_sales_df["Purchase Date"])
pen_sales_df["Delivery Date"] = pd.to_datetime(pen_sales_df["Delivery Date"])

# 1️⃣ Sales Over Time Analysis
# monthly_sales = pen_sales_df.groupby(pen_sales_df["Purchase Date"].dt.to_period("M")).size()
# plt.figure(figsize=(10, 5))
# monthly_sales.plot(kind="line", marker="o", linestyle="-", color="b")
# plt.title("Sales Over Time")
# plt.xlabel("Month")
# plt.ylabel("Number of Sales")
# plt.grid()
# plt.show()

# 1️⃣ Sales Over Time Analysis (Monthly Breakdown)
# monthly_sales = pen_sales_df.groupby(pen_sales_df["Purchase Date"].dt.strftime('%Y-%m')).size()
monthly_sales = pen_sales_df.groupby(pen_sales_df["Purchase Date"].dt.strftime('%m')).size()
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o", linestyle="-", color="b")
plt.title("Sales Over Time (Monthly)")
plt.xlabel("Month")
plt.ylabel("Number of Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 1️⃣ Sales Over Time Analysis (Daily in May)
# may_sales = pen_sales_df[pen_sales_df["Purchase Date"].dt.month == 5]  # Filter May sales
# daily_sales = may_sales.groupby(pen_sales_df["Purchase Date"].dt.day).size()
# plt.figure(figsize=(10, 5))
# daily_sales.plot(kind="line", marker="o", linestyle="-", color="b")
# plt.title("Daily Sales in May")
# plt.xlabel("Day of Month")
# plt.ylabel("Number of Sales")
# plt.xticks(range(1, 32))
# plt.grid()
# plt.show()

# 2️⃣ Average Shipping Cost by Item
avg_shipping_cost = pen_sales_df.groupby("Item")["Shipping Cost"].mean().sort_values()
plt.figure(figsize=(10, 5))
avg_shipping_cost.plot(kind="barh", color="purple")
plt.title("Average Shipping Cost by Item")
plt.xlabel("Average Shipping Cost")
plt.ylabel("Pen Type")
plt.show()

# 3️⃣ Top-Selling Pens
item_counts = pen_sales_df["Item"].value_counts()
print(item_counts)
plt.figure(figsize=(10, 5))
item_counts.plot(kind="barh", color="green")
plt.title("Top-Selling Pens")
plt.xlabel("Number of Sales")
plt.ylabel("Pen Type")
plt.gca().invert_yaxis()
plt.show()

# 4️⃣ Average Delivery Time per Item
pen_sales_df["Delivery Time"] = (pen_sales_df["Delivery Date"] - pen_sales_df["Purchase Date"]).dt.days
avg_delivery_time = pen_sales_df.groupby("Item")["Delivery Time"].mean().sort_values()
plt.figure(figsize=(10, 5))
avg_delivery_time.plot(kind="bar", color="orange")
plt.title("Average Delivery Time by Pen Type")
plt.xlabel("Pen Type")
plt.ylabel("Average Delivery Time (Days)")
plt.xticks(rotation=45, ha="right")
plt.show()

# 5️⃣ Sentiment Analysis from Reviews
pen_sales_df["Review Text"] = pen_sales_df["Review"].str.split("|").str[1]
positive_words = ["love", "great", "good", "amazing", "excellent", "best"]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]
positive_count = pen_sales_df["Review Text"].str.contains("|".join(positive_words), case=False, na=False).sum()
negative_count = pen_sales_df["Review Text"].str.contains("|".join(negative_words), case=False, na=False).sum()

# Plot Sentiment Analysis Pie Chart
plt.figure(figsize=(6, 6))
plt.pie([positive_count, negative_count], labels=["Positive Reviews", "Negative Reviews"], autopct="%1.1f%%", colors=["blue", "red"], startangle=140)
plt.title("Sentiment Analysis of Reviews")
plt.show()
