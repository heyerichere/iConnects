import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
)

def rate_resume_for_keywords(resume_text, keywords):
    ratings = {}

    for keyword in keywords:
        prompt = (
            f"Rate the relevance of the keyword '{keyword}' based on the following resume on a scale of 1 to 20:\n\n"
            f"{resume_text}. Give a number where 20 means the keyword strongly matches this resume, "
            f"and 1 means it does not match at all. Only the number, please."
        )


        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a resume evaluator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=5,
            temperature=0
        )

        rating = response.choices[0].message.content.strip()

        try:
            rating = float(rating)
            rating = max(1, min(20, rating))
        except ValueError:
            rating = 10

        ratings[keyword] = rating

    return ratings