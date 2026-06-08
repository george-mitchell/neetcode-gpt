import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        
        answer = np.matmul(X,weights)
        return np.round(answer, 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        
        return np.round(np.mean(np.square(np.subtract(ground_truth, model_prediction))), 5)
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
