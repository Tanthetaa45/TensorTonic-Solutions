from collections.abc import Sequence
import numpy as np
def triplet_loss(
    anchor: Sequence[float] | np.ndarray,
    positive: Sequence[float] | np.ndarray,
    negative: Sequence[float] | np.ndarray,
    margin: float = 1.0,
) -> float:
    anchor_arr = np.asarray(anchor, dtype=float)
    positive_arr = np.asarray(positive, dtype=float)
    negative_arr = np.asarray(negative, dtype=float)

    anchor_arr = np.atleast_2d(anchor_arr)
    positive_arr = np.atleast_2d(positive_arr)
    negative_arr = np.atleast_2d(negative_arr)

    positive_distance = np.sum((anchor_arr - positive_arr) ** 2, axis=1)
    negative_distance = np.sum((anchor_arr - negative_arr) ** 2, axis=1)
    loss = np.maximum(0.0, positive_distance - negative_distance + margin)
    return float(np.mean(loss))
    pass