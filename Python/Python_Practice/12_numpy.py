# Without using built-in NumPy functions:
    #     implement dot product
    #     Then compare with NumPy’s result.



def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length")
    
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    
    return result


# Example usage:
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
custom_dot = dot_product(vec1, vec2)
print("Custom Dot Product:", custom_dot)


import numpy as np
np_dot = np.dot(vec1, vec2)
print("NumPy Dot Product:", np_dot)

