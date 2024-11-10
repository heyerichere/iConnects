import heapq


def affinity_difference(post_affinites, resume_affinities):
    keywords = set(post_affinites.keys())
    resume_keywords = set(resume_affinities.keys())
    
    all_keywords = keywords.union(resume_keywords)
    
    total_difference = 0
    
    for keyword in all_keywords:
        post_value = post_affinites.get(keyword, 0)
        resume_value = resume_affinities.get(keyword, 0)
        difference = abs(post_value - resume_value)
        total_difference += difference
    
    return total_difference

def match_posts_to_resume(posts, resume_affinities, number_of_post_matches = 5):
    post_heap = []
    
    for post_title, post_affinites in posts.items():
        difference_score = affinity_difference(post_affinites, resume_affinities)
        heapq.heappush(post_heap, (difference_score, post_title))
    
    top_posts = heapq.nsmallest(number_of_post_matches, post_heap)
    
    return top_posts
