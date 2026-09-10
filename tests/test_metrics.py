from metalmind.evaluation import metrics, rubric


class FakeLLM:
    def __init__(self, response):
        self._response = response
        self.total_tokens = 0

    def complete_json(self, system, user):
        return self._response


def test_faithfulness_computes_ratio_of_supported_claims():
    llm = FakeLLM({"claims": [{"claim": "a", "supported": True}, {"claim": "b", "supported": False}]})
    assert metrics.faithfulness(llm, "answer", ["context"]) == 0.5


def test_faithfulness_defaults_to_one_when_no_claims_extracted():
    llm = FakeLLM({"claims": []})
    assert metrics.faithfulness(llm, "answer", ["context"]) == 1.0


def test_context_precision_computes_ratio_of_relevant_passages():
    llm = FakeLLM({"relevance": [True, True, False, False]})
    assert metrics.context_precision(llm, "question", ["a", "b", "c", "d"]) == 0.5


def test_context_precision_empty_context_is_zero():
    llm = FakeLLM({"relevance": []})
    assert metrics.context_precision(llm, "question", []) == 0.0


def test_context_recall_computes_ratio_of_attributed_statements():
    llm = FakeLLM({"statements": [{"statement": "a", "attributed": True}, {"statement": "b", "attributed": True}]})
    assert metrics.context_recall(llm, "ground truth", ["context"]) == 1.0


def test_rubric_score_clamps_to_valid_range():
    assert rubric.rubric_score(FakeLLM({"score": 7}), "q", "a", ["c"]) == 5
    assert rubric.rubric_score(FakeLLM({"score": 0}), "q", "a", ["c"]) == 1
    assert rubric.rubric_score(FakeLLM({"score": 3}), "q", "a", ["c"]) == 3
    assert rubric.rubric_score(FakeLLM({"score": "not-a-number"}), "q", "a", ["c"]) == 3
