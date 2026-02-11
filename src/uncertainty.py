import numpy as np

def uncertainty_score(p_green: np.ndarray) -> np.ndarray:
    return 1.0 - 2.0 * np.abs(p_green - 0.5)
