# recommendations/utils.py
def calculate_jaccard_index(set1, set2):
    # Calculate Jaccard Index
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def calculate_jaccard_recommendations(user_id, users_data):
    user_data = next((user for user in users_data if user['id'] == user_id), None)
    age_difference = 15
    if user_data:
        user_interests = set(user_data['interests'].keys())
        recommendations = []
    
        for other_user in users_data:
            if abs(user_data['age']-other_user['age'])>age_difference:
                continue
            if other_user['id'] != user_id:
                other_interests = set(other_user['interests'].keys())
                jaccard_index = calculate_jaccard_index(user_interests, other_interests)
                
                # You can adjust this threshold based on your requirements
                if jaccard_index >= 0.5:
                    recommendations.append(other_user)
        return recommendations[:5]  # Return the top 5 recommendations
    
    return []
