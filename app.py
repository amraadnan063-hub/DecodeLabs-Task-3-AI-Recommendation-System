
import streamlit as st
from recommender import recommend_careers

st.set_page_config(
    page_title="AI Career Recommender",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Career Recommendation System")

st.write(
    "Discover suitable career paths based on your technical skills."
)

st.divider()

st.subheader("Enter Your Skills")

user_input = st.text_input(
    "Enter at least 3 skills separated by commas",
    placeholder="Python, Machine Learning, Data Analysis"
)

if st.button("Recommend Careers"):

    if not user_input.strip():
        st.warning("Please enter your skills!")

    else:
        user_skills = [
            skill.strip()
            for skill in user_input.split(",")
            if skill.strip()
        ]

        if len(user_skills) < 3:
            st.warning("Please enter at least 3 skills!")

        else:
            results = recommend_careers(user_skills)

            if results is not None:

                st.subheader("Your Career Recommendations")

                if not results.empty:

                    if results["recommendation_type"].iloc[0] == "Trending Fallback":
                        st.info(
                            "No matching skills found. "
                            "Showing default career suggestions instead."
                        )

                    for _, row in results.iterrows():

                        score = row["similarity_score"] * 100

                        st.success(row["job_role"])

                        st.progress(float(row["similarity_score"]))

                        st.write(f"Match Score: {score:.2f}%")

                        st.caption(row["recommendation_type"])

st.divider()

st.caption("DecodeLabs Project 3 | Batch 2026")

