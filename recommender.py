
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_careers(user_skills, top_n=3):

    # Step 1: Load dataset
    data = pd.read_csv("raw_skills.csv")

    data["skills"] = data["skills"].fillna("").str.lower()

    # Step 2: Create user profile
    user_profile = " ".join(user_skills).lower()

    # Step 3: TF-IDF Vectorization
    vectorizer = TfidfVectorizer()

    item_vectors = vectorizer.fit_transform(data["skills"])

    user_vector = vectorizer.transform([user_profile])

    # Step 4: Cold Start Handling
    if user_vector.nnz == 0:

        print("Cold Start Detected!")

        fallback_roles = [
            "Software Engineer",
            "Data Analyst",
            "Web Developer"
        ]

        fallback = data[
            data["job_role"].isin(fallback_roles)
        ].copy()

        fallback["similarity_score"] = 0.0

        fallback["recommendation_type"] = "Trending Fallback"

        return fallback.head(top_n)[
            ["job_role", "similarity_score", "recommendation_type"]
        ]

    # Step 5: Cosine Similarity
    scores = cosine_similarity(
        user_vector, item_vectors
    ).flatten()

    # Step 6: Ranking
    data["similarity_score"] = scores

    data["recommendation_type"] = "Personalized Match"

    # Step 7: Sorting
    recommendations = data.sort_values(
        by="similarity_score",
        ascending=False
    )

    # Step 8: Top 3 Filtering
    recommendations = recommendations.head(top_n)

    return recommendations[
        ["job_role", "similarity_score", "recommendation_type"]
    ]


if __name__ == "__main__":

    print("AI Career Recommendation System")
    print("      ")

    skills = input(
        "Enter at least 3 skills separated by commas: "
    )

    user_skills = [
        skill.strip() for skill in skills.split(",")
        if skill.strip()
    ]

    if len(user_skills) < 3:

        print("Please enter at least 3 skills!")

    else:

        results = recommend_careers(user_skills)

        print("\nCareer Recommendations:\n")

        print(results.to_string(index=False))
