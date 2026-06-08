import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        mx = max(z)
        return np.round(np.divide(np.exp(z - mx), np.sum(np.exp(z - mx))), 4)
