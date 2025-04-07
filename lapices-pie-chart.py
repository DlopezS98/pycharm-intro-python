import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"

df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

# Usuario | El comentario u opinion del usuario
reviews = df_pen_sales["Review"]
# print(reviews)

positive_words = ["love", "great", "good", "amazing", "excellent", "best" ]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

positive_review_count = reviews.str.contains("|".join(positive_words), case=False, na=False).sum()
negative_review_count = reviews.str.contains("|".join(negative_words), case=False, na=False).sum()
# for review in reviews:
#     for positive_word in positive_words:
#         if positive_word.lower() in review.lower():
#             positive_review_count += 1
#             break

print("CANTIDAD DE REVIEWS POSITIVOS: " + str(positive_review_count))
print("CANTIDAD DE REVIEWS NEGATIVOS: " + str(negative_review_count))


plt.figure(figsize=(6, 6))
plt.pie([positive_review_count, negative_review_count], labels=["Review Positivo", "Review Negativo"], autopct="%1.1f%%", colors=["green", "red"], startangle=140)
plt.title("Opinion de los productos")
plt.show()