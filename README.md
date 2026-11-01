
# AI Career Recommendation System

## Project Overview
AI Career Recommendation System is a content-based recommendation application developed as part of DecodeLabs Industrial Training Kit – Batch 2026.

The system recommends suitable career paths based on users' technical skills using TF-IDF vectorization and Cosine Similarity.

## Features
- Accepts a minimum of 3 user skills.
- Uses Content-Based Filtering.
- Converts skills into numerical vectors using TF-IDF.
- Calculates similarity using Cosine Similarity.
- Ranks career recommendations by similarity score.
- Displays the Top 3 career recommendations.
- Handles the Cold Start Problem through fallback suggestions.
- Interactive web interface using Streamlit.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Project Structure

AI-Recommendation-System/
- raw_skills.csv
- recommender.py
- app.py
- requirements.txt
- README.md

## Installation

1. Clone the repository:

   git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder:

   cd AI-Recommendation-System

3. Create a virtual environment:

   python -m venv venv

4. Activate the environment (Windows):

   .\venv\Scripts\Activate.ps1

5. Install dependencies:

   pip install -r requirements.txt

6. Run the application:

   streamlit run app.py

## How It Works

1. User enters at least three technical skills.
2. The system loads career roles from raw_skills.csv.
3. TF-IDF converts career skills into numerical vectors.
4. Cosine Similarity compares the user's profile with career profiles.
5. Results are sorted by similarity score.
6. The system displays the Top 3 career recommendations.

## Cold Start Handling

If the user's entered skills do not match the dataset vocabulary, the system provides default career suggestions instead of personalized recommendations.

## Testing

The application was tested with:

- AI and Machine Learning skills.
- Web Development skills.
- Cloud and DevOps skills.
- Data Science skills.
- Unknown skills for Cold Start handling.
- Fewer than three skills for input validation.

## Project Information

Project: Project 3 – AI Recommendation Logic  
Training: DecodeLabs Industrial Training Kit  
Batch: 2026

## Author

Developed as part of DecodeLabs Industrial Training Kit – Batch 2026.
