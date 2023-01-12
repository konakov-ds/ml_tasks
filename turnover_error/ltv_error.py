import numpy as np


def ltv_error(y_true: np.array, y_pred: np.array) -> float:
    """
    asymmetric loss function penalizing for over-prediction
    """
    error = ((np.log(1 + y_pred) * (y_pred - y_true))**2).sum()
    
    return error
