import numpy as np


def turnover_error(y_true: np.array, y_pred: np.array) -> float:
    """
    asymmetric loss function penalizing for underprediction
    """
    error = (((y_pred - y_true) / y_pred)**2).sum()
    return error