from metalmind.evaluation.token_efficiency import composite_score, normalize


def test_normalize_higher_is_better():
    assert normalize([1.0, 2.0, 3.0], higher_is_better=True) == [0.0, 0.5, 1.0]


def test_normalize_lower_is_better_inverts():
    assert normalize([1.0, 2.0, 3.0], higher_is_better=False) == [1.0, 0.5, 0.0]


def test_normalize_constant_values_returns_midpoint():
    assert normalize([2.0, 2.0, 2.0]) == [0.5, 0.5, 0.5]


def test_composite_score_rewards_high_accuracy_and_low_tokens():
    # Mirrors the paper's global-retrieval story: hybrid wins on accuracy and stays
    # token-competitive, so it should score highest even though vector uses fewer tokens
    # than graph in this toy example.
    accuracy = [0.3, 0.6, 0.9]  # vector, graph, hybrid
    tokens = [6350, 6050, 6160]
    scores = composite_score(accuracy, tokens)

    assert len(scores) == 3
    assert all(1.0 <= s <= 5.0 for s in scores)
    assert scores[2] > scores[1] > scores[0]  # hybrid > graph > vector, as in Table 1
