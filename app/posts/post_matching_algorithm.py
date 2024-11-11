import heapq

def affinity_difference(post_affinities, resume_affinities):
    all_keywords = set(post_affinities.keys()).union(resume_affinities.keys())
    total_difference = 0

    for keyword in all_keywords:
        post_value = post_affinities.get(keyword, 0)
        resume_value = resume_affinities.get(keyword, 0)
        difference = abs(post_value - resume_value)
        total_difference += difference

    return total_difference

def match_posts_to_resume(posts, resume_affinities, number_of_post_matches=5):
    post_heap = []

    for post_title, post_affinities in posts.items():
        difference_score = affinity_difference(post_affinities, resume_affinities)
        heapq.heappush(post_heap, (difference_score, post_title))

    top_posts = heapq.nsmallest(number_of_post_matches, post_heap)

    return top_posts