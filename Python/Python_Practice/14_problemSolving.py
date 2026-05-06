# Given a dataset of student scores:
    # normalize values (min-max scaling)
    # split into train/test (80/20)



import numpy as np


def min_max_scaling(scores):
    min_score = np.min(scores)
    max_score = np.max(scores)
    
    if max_score - min_score == 0:
        return np.zeros_like(scores)  # Avoid division by zero
    
    scaled_scores = (scores - min_score) / (max_score - min_score)
    return scaled_scores


def train_test_split(scores, test_size=0.2):
    np.random.shuffle(scores)
    split_index = int(len(scores) * (1 - test_size))
    train_scores = scores[:split_index]
    test_scores = scores[split_index:]
    return train_scores, test_scores


# Example usage:
student_scores = np.array([85, 90, 78, 92, 88, 95, 80, 82])
normalized_scores = min_max_scaling(student_scores)
print("Normalized Scores:", normalized_scores)

train_scores, test_scores = train_test_split(normalized_scores, test_size=0.2)
print("Train Scores:", train_scores)
print("Test Scores:", test_scores)


