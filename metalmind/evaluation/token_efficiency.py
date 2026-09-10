import numpy as np


def normalize(values: list, higher_is_better: bool = True) -> list:
    arr = np.array(values, dtype=float)
    lo, hi = arr.min(), arr.max()
    if hi - lo < 1e-9:
        return [0.5] * len(values)
    norm = (arr - lo) / (hi - lo)
    if not higher_is_better:
        norm = 1 - norm
    return norm.tolist()


def composite_score(
    accuracy_scores: list,
    token_counts: list,
    accuracy_weight: float = 0.7,
    token_weight: float = 0.3,
    out_min: float = 1.0,
    out_max: float = 5.0,
) -> list:
    """Paper §Retrieval performance: normalize retrieval accuracy and token consumption to
    [0, 1], combine with a 70/30 weighting favoring accuracy, then apply a sigmoid
    transform to spread the composite scores across a non-linear 1-5 range."""
    norm_accuracy = normalize(accuracy_scores, higher_is_better=True)
    norm_tokens = normalize(token_counts, higher_is_better=False)

    raw = [accuracy_weight * a + token_weight * t for a, t in zip(norm_accuracy, norm_tokens)]
    centered = [(r - 0.5) * 6 for r in raw]  # spread the 0..1 composite before squashing
    sigmoid = [1 / (1 + np.exp(-c)) for c in centered]
    return [out_min + s * (out_max - out_min) for s in sigmoid]
