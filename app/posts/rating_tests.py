import os
from rating import rate_resume_for_keywords
from post_matching_algorithm import match_posts_to_resume
from pdf_to_text import to_text

resume_text = to_text("/Users/adjei.net/Desktop/iConnects/app/static/images/resume.pdf")

keywords = ["Python", "machine learning", "JavaScript", "data analysis", "cloud computing"]

print("Keyword Ratings:")
ratings = rate_resume_for_keywords(resume_text, keywords)
for keyword, rating in ratings.items():
    print(f"{keyword}: {rating}")

posts = {
    "Data Scientist Position": {"Python": 20, "machine learning": 15, "data analysis": 10},
    "Frontend Developer": {"JavaScript": 18, "HTML": 15, "CSS": 15},
    "Cloud Engineer": {"cloud computing": 20, "Python": 15, "DevOps": 10},
    "Full-Stack Developer": {"Python": 18, "JavaScript": 18, "data analysis": 5},
    "Machine Learning Engineer": {"machine learning": 20, "Python": 15, "data analysis": 10}
}

print("\nTop Post Matches:")
matched_posts = match_posts_to_resume(posts, ratings, number_of_post_matches=3)
for score, title in matched_posts:
    print(f"{title} with difference score: {score}")
