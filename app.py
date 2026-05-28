"""
MBTI Personality Test — Flask Web App
"""

import json
import tempfile
import os

from flask import Flask, render_template, request, send_file

from questions import get_questions
from mbti_engine import score_answers, determine_type
from personality_db import get_personality
from report_generator import generate_report

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    n = request.args.get("n", "25")
    if n not in ("25", "50"):
        n = "25"
    questions = get_questions(int(n))
    return render_template("test.html", questions=questions, question_count=int(n))


@app.route("/result", methods=["POST"])
def result():
    question_count = int(request.form.get("question_count", 25))
    questions = get_questions(question_count)

    answers = {}
    for q in questions:
        key = f"q{q['id']}"
        val = request.form.get(key, "")
        if val in ("a", "b"):
            answers[str(q["id"])] = val

    scores = score_answers(answers, questions)
    mbti_type = determine_type(scores)
    personality = get_personality(mbti_type)

    dim_descriptions = {
        "EI": "Extraversion vs Introversion",
        "SN": "Sensing vs Intuition",
        "TF": "Thinking vs Feeling",
        "JP": "Judging vs Perceiving",
    }
    dim_meanings = {
        "EI": "Where you focus your attention and get energy",
        "SN": "How you take in information and perceive the world",
        "TF": "How you make decisions and evaluate information",
        "JP": "How you approach structure and the outer world",
    }

    dims = []
    for dim, (pole_a, pole_b) in [("EI", ("E", "I")), ("SN", ("S", "N")),
                                    ("TF", ("T", "F")), ("JP", ("J", "P"))]:
        dims.append({
            "dim": dim,
            "description": dim_descriptions[dim],
            "meaning": dim_meanings[dim],
            "pole_a": pole_a,
            "pole_b": pole_b,
            "pct_a": scores[dim][pole_a],
            "pct_b": scores[dim][pole_b],
        })

    return render_template(
        "result.html",
        mbti_type=mbti_type,
        personality=personality,
        scores=scores,
        scores_json=json.dumps(scores),
        dimensions=dims,
        question_count=question_count,
    )


@app.route("/download", methods=["POST"])
def download():
    mbti_type = request.form.get("mbti_type", "XXXX")
    scores = json.loads(request.form.get("scores", "{}"))
    personality = get_personality(mbti_type)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    tmp_path = tmp.name
    tmp.close()

    try:
        generate_report(tmp_path, mbti_type, scores, personality)
        return send_file(
            tmp_path,
            as_attachment=True,
            download_name=f"MBTI_Report_{mbti_type}.docx",
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    finally:
        # Clean up temp file after sending
        pass


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
