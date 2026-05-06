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





