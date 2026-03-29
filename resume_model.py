from __future__ import annotations

import math
import re
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sample_data import GLOBAL_SKILLS, ROLE_SKILLS, TRAINING_DATA


@dataclass
class ResumeInsights:
    predicted_role: str
    confidence: float
    role_scores: list[tuple[str, float]]
    matched_skills: list[str]
    missing_skills: list[str]
    experience_years: int | None
    education_signals: list[str]
    resume_strength: int
    improvement_tips: list[str]


def build_model() -> Pipeline:
    texts = [item["text"] for item in TRAINING_DATA]
    labels = [item["role"] for item in TRAINING_DATA]
    model = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=1,
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    max_iter=2000,
                    multi_class="auto",
                ),
            ),
        ]
    )
    model.fit(texts, labels)
    return model


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def extract_skills(text: str) -> list[str]:
    normalized = normalize_text(text)
    return [skill for skill in GLOBAL_SKILLS if skill in normalized]


def extract_experience_years(text: str) -> int | None:
    patterns = [
        r"(\d+)\+?\s+years? of experience",
        r"experience of\s+(\d+)\+?\s+years?",
        r"(\d+)\+?\s+years? experience",
        r"over\s+(\d+)\s+years?",
    ]
    lowered = text.lower()
    for pattern in patterns:
        match = re.search(pattern, lowered)
        if match:
            return int(match.group(1))
    return None


def extract_education_signals(text: str) -> list[str]:
    lowered = text.lower()
    signals = []
    for keyword in ["b.tech", "bachelor", "master", "phd", "m.tech", "computer science", "statistics"]:
        if keyword in lowered:
            signals.append(keyword.title())
    return signals


def compute_resume_strength(
    confidence: float,
    matched_skills: list[str],
    experience_years: int | None,
    education_signals: list[str],
) -> int:
    score = 35
    score += min(len(matched_skills) * 4, 30)
    score += min(int(confidence * 25), 25)
    if experience_years:
        score += min(experience_years * 2, 10)
    if education_signals:
        score += min(len(education_signals) * 2, 8)
    return max(0, min(score, 100))


def build_improvement_tips(
    target_role: str,
    matched_skills: list[str],
    missing_skills: list[str],
    experience_years: int | None,
    education_signals: list[str],
) -> list[str]:
    tips = []
    if len(matched_skills) < 5:
        tips.append("Add a stronger technical skills section with role-specific tools and platforms.")
    if missing_skills:
        tips.append(
            "Include evidence for these relevant keywords: "
            + ", ".join(missing_skills[:5])
            + "."
        )
    if experience_years is None:
        tips.append("Mention your total years of experience clearly so recruiters can assess seniority faster.")
    if not education_signals:
        tips.append("Add education details or certifications that support your data background.")
    if target_role in {"Data Scientist", "Machine Learning Engineer"}:
        tips.append("Quantify ML impact with metrics like accuracy lift, latency reduction, or revenue influence.")
    else:
        tips.append("Show business impact with measurable outcomes such as KPI improvement or reporting time saved.")
    return tips[:4]


def analyze_resume(model: Pipeline, resume_text: str, target_role: str | None = None) -> ResumeInsights:
    probabilities = model.predict_proba([resume_text])[0]
    roles = list(model.classes_)
    scored_roles = sorted(zip(roles, probabilities), key=lambda item: item[1], reverse=True)
    predicted_role, confidence = scored_roles[0]

    role_for_gap_analysis = target_role or predicted_role
    matched_skills = extract_skills(resume_text)
    required_skills = ROLE_SKILLS.get(role_for_gap_analysis, [])
    missing_skills = [skill for skill in required_skills if skill not in matched_skills]
    experience_years = extract_experience_years(resume_text)
    education_signals = extract_education_signals(resume_text)
    strength = compute_resume_strength(confidence, matched_skills, experience_years, education_signals)
    tips = build_improvement_tips(
        role_for_gap_analysis,
        matched_skills,
        missing_skills,
        experience_years,
        education_signals,
    )

    return ResumeInsights(
        predicted_role=predicted_role,
        confidence=confidence,
        role_scores=[(role, round(score * 100, 2)) for role, score in scored_roles],
        matched_skills=matched_skills,
        missing_skills=missing_skills[:8],
        experience_years=experience_years,
        education_signals=education_signals,
        resume_strength=math.floor(strength),
        improvement_tips=tips,
    )
