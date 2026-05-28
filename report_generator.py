"""
Word report generator for MBTI test results.
Uses shared word_utils.Report to produce .docx output.
"""

import sys
sys.path.insert(0, r"D:\Claude Code\_shared")
from word_utils import Report
from docx.shared import Pt, RGBColor


def generate_report(output_path, mbti_type, scores, personality, name=""):
    """
    Generate a professional MBTI report as a Word document.

    Args:
        output_path: str, file path for .docx
        mbti_type: str, 4-letter type (e.g. "INTJ")
        scores: dict, dimension percentages
        personality: dict from personality_db
        name: str, optional user name
    """
    title_text = f"MBTI Personality Report{f': {name}' if name else ''}"
    r = Report(output_path, title=title_text,
               subtitle="Myers-Briggs Type Indicator — Personal Assessment")

    # ── Result ──
    r.h1("Your Personality Type")

    p = r.doc.add_paragraph()
    p.alignment = 1  # center
    run = p.add_run(mbti_type)
    run.bold = True
    run.font.size = Pt(36)
    run.font.color.rgb = RGBColor(0, 51, 102)

    p2 = r.doc.add_paragraph()
    p2.alignment = 1
    run2 = p2.add_run(personality.get("title", ""))
    run2.italic = True
    run2.font.size = Pt(16)
    run2.font.color.rgb = RGBColor(100, 100, 100)

    r.spacer()

    # ── Dimension Breakdown ──
    r.h2("Dimension Breakdown")

    dim_labels = [
        ("EI", "Extraversion (E)  vs  Introversion (I)", "E", "I"),
        ("SN", "Sensing (S)  vs  Intuition (N)", "S", "N"),
        ("TF", "Thinking (T)  vs  Feeling (F)", "T", "F"),
        ("JP", "Judging (J)  vs  Perceiving (P)", "J", "P"),
    ]
    dim_descriptions = {
        "EI": "Where you focus your attention and get energy",
        "SN": "How you take in information",
        "TF": "How you make decisions",
        "JP": "How you deal with the outer world",
    }

    for dim, label, pole_a, pole_b in dim_labels:
        s = scores[dim]
        pct_a = s[pole_a]
        pct_b = s[pole_b]
        bar_len = 25
        bar_a = int(bar_len * pct_a / 100)
        bar_b = bar_len - bar_a

        bar_text = f"{pole_a}: {'█' * bar_a} {pct_a}%    {pole_b}: {'█' * bar_b} {pct_b}%"

        r.h3(label)
        r.p(bar_text)
        r.p(dim_descriptions[dim], italic=True, size=9, color=(120, 120, 120))
        r.spacer()

    r.divider()

    # ── Personality Evaluation ──
    r.h1("Personality Evaluation")

    r.h2("Overview")
    r.p(personality.get("overview", ""))

    r.h2("Key Traits")
    r.p(personality.get("traits", ""))

    r.h2("Work Style & Career")
    r.p(personality.get("work_style", ""))

    r.h2("Strengths")
    for s in personality.get("strengths", "").split(","):
        s = s.strip().rstrip(".")
        if s:
            r.bullet(s)

    r.h2("Areas for Growth")
    for w in personality.get("weaknesses", "").split(","):
        w = w.strip().rstrip(".")
        if w:
            r.bullet(w)

    r.divider()

    # ── Footer ──
    r.p("This report is generated for informational and educational purposes. "
        "MBTI is a personality indicator, not a diagnostic tool. "
        "Personality is complex and cannot be fully captured by any single assessment.",
        size=8, color=(150, 150, 150))

    r.save()
    return output_path
