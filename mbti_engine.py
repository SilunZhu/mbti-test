"""
MBTI scoring engine — handles swapped options and calculates percentages.
"""

DIMENSION_MAP = {
    "EI": ("E", "I"),
    "SN": ("S", "N"),
    "TF": ("T", "F"),
    "JP": ("J", "P"),
}


def score_answers(answers, questions):
    """
    Calculate percentage scores for each MBTI dimension.
    Handles the swap field: when swap=True, option_a maps to pole2, option_b to pole1.

    Args:
        answers: dict of {question_id: "a" or "b"}
        questions: list of question dicts

    Returns:
        dict like {"EI": {"E": 60, "I": 40}, ...}
    """
    # p1 = pole1 (E,S,T,J), p2 = pole2 (I,N,F,P)
    dim_counts = {"EI": {"p1": 0, "p2": 0}, "SN": {"p1": 0, "p2": 0},
                  "TF": {"p1": 0, "p2": 0}, "JP": {"p1": 0, "p2": 0}}

    for q in questions:
        qid = str(q["id"])
        if qid not in answers:
            continue
        choice = answers[qid]
        if choice not in ("a", "b"):
            continue
        swap = q.get("swap", False)
        # If not swapped: a→p1, b→p2. If swapped: a→p2, b→p1
        is_p1 = (choice == "a" and not swap) or (choice == "b" and swap)
        if is_p1:
            dim_counts[q["dimension"]]["p1"] += 1
        else:
            dim_counts[q["dimension"]]["p2"] += 1

    scores = {}
    for dim, (pole_a, pole_b) in DIMENSION_MAP.items():
        p1 = dim_counts[dim]["p1"]
        p2 = dim_counts[dim]["p2"]
        total = p1 + p2
        if total == 0:
            scores[dim] = {pole_a: 50, pole_b: 50}
        else:
            pct_p1 = round(p1 / total * 100)
            scores[dim] = {pole_a: pct_p1, pole_b: 100 - pct_p1}

    return scores


def determine_type(scores):
    """Determine the 4-letter MBTI type from dimension scores."""
    result = ""
    for dim, pole_a, pole_b in [("EI", "E", "I"), ("SN", "S", "N"),
                                 ("TF", "T", "F"), ("JP", "J", "P")]:
        s = scores[dim]
        result += pole_a if s[pole_a] >= s[pole_b] else pole_b
    return result
