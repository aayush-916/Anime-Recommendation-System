import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load your dataset
df = pd.read_csv("anime_data.csv")
process_data = pd.read_csv("preprocessed_anime_dataset.csv")
# Combine features

df['combined_features'] = process_data['processed_content']

# Create the TF-IDF matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the anime that matches the title
    idx = df.index[df['Name'] == title].tolist()
    
    if not idx:
        return []  # Handle the case where the anime title doesn't exist
    
    idx = idx[0]  # Assuming you want the first match

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the 5 most similar anime
    anime_indices = [i[0] for i in sim_scores[1:6]]

    # Return the top 5 most similar anime
    return df[['Name', 'Score', 'Genres']].iloc[anime_indices]

