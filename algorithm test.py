import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def recommend_similar_books(csv_file_path, user_book_title, num_recommendations=5):
    df = pd.read_csv(csv_file_path)
    if user_book_title not in df['title'].values:
        print(f"\n'{user_book_title}' is not found in the CSV file.")
        return
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['summary'])
    user_book_index = df[df['title'] == user_book_title].index[0]
    cosine_similarities = linear_kernel(tfidf_matrix[user_book_index],
                                        tfidf_matrix).flatten()
    similar_books_indices = cosine_similarities.argsort()[::-1]
    print(f"\nRecommended books similar to {user_book_title}:")
    recommended_count = 0
    for index in similar_books_indices:
        recommended_book = df.loc[index, 'title']
        if recommended_book != user_book_title:
            print(f"{recommended_count + 1}. {recommended_book}")
            recommended_count += 1
            if recommended_count == num_recommendations:
                break


csv_file_path = data.csv
user_input_title = input("\nEnter the title of the book you have read: ")
recommend_similar_books(csv_file_path, user_input_title, num_recommendations=5)
