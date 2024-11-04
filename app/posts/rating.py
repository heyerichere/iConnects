import os
import openai

openai.api_key = os.environ.get('API_KEY')

def rate_resume_for_keywords(resume_text, keywords):
    ratings = {}
    
    for keyword in keywords:
        prompt = f"Rate the relevance of the keyword '{keyword}' based on the following resume on a scale of 1 to 20:\n\n{resume_text}. Basically, you'll be given a some keywords so make sure to give the keyword that strongly matches this resume a 20 and the worst gets a 1. Just mention the number. Don't write any sentence, just the number."
 
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a resume evaluator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=5,
            temperature=0
        )
        
        # Extracting the rating from the API response
        rating = response['choices'][0]['message']['content'].strip()
        
        try:
            rating = float(rating)
            rating = max(1, min(10, rating))
        except ValueError:
            rating = 10  # Default to 10 if there's an issue

        ratings[keyword] = rating
    
    return ratings