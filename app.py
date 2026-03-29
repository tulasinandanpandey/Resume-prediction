from __future__ import annotations

from io import BytesIO

import streamlit as st

from resume_model import analyze_resume, build_model
from sample_data import ROLE_SKILLS


st.set_page_config(
    page_title="AI Resume Predictor",
    page_icon="📄",
    layout="wide",
)


CUSTOM_CSS = """
<style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(14, 165, 233, 0.18), transparent 32%),
            radial-gradient(circle at top right, rgba(16, 185, 129, 0.15), transparent 28%),
            linear-gradient(135deg, #f5f7fb 0%, #eef7f4 100%);
    }
    .hero {
        padding: 1.8rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #0f172a, #134e4a);
        color: white;
        box-shadow: 0 18px 60px rgba(15, 23, 42, 0.20);
        margin-bottom: 1.2rem;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }
    .chip {
        display: inline-block;
        margin: 0.15rem 0.35rem 0.15rem 0;
        padding: 0.4rem 0.7rem;
        border-radius: 999px;
        font-size: 0.9rem;
        background: #e2f3ff;
        color: #0c4a6e;
        border: 1px solid #bae6fd;
    }
    .chip-missing {
        background: #fff1f2;
        color: #9f1239;
        border: 1px solid #fecdd3;
    }
</style>
"""


@st.cache_resource
def load_model():
    return build_model()


def read_uploaded_file(uploaded_file) -> str:
    suffix = uploaded_file.name.lower().split(".")[-1]
    file_bytes = uploaded_file.getvalue()

    if suffix == "txt":
        return file_bytes.decode("utf-8", errors="ignore")
    if suffix == "pdf":
        try:
            from pypdf import PdfReader
        except ModuleNotFoundError as exc:
            raise ValueError("PDF support needs the `pypdf` package. Run `pip install -r requirements.txt`.") from exc
        reader = PdfReader(BytesIO(file_bytes))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if suffix == "docx":
        try:
            from docx import Document
        except ModuleNotFoundError as exc:
            raise ValueError("DOCX support needs the `python-docx` package. Run `pip install -r requirements.txt`.") from exc
        doc = Document(BytesIO(file_bytes))
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    raise ValueError("Unsupported file format. Please upload a TXT, PDF, or DOCX resume.")


def render_skill_chips(skills: list[str], missing: bool = False) -> None:
    if not skills:
        st.write("None detected yet.")
        return
    class_name = "chip chip-missing" if missing else "chip"
    html = "".join([f'<span class="{class_name}">{skill}</span>' for skill in skills])
    st.markdown(html, unsafe_allow_html=True)


def main() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero">
            <h1 style="margin-bottom:0.4rem;">AI Resume Prediction App</h1>
            <p style="font-size:1.05rem; opacity:0.95; margin-bottom:0.3rem;">
                Upload or paste a resume to predict the best-fit data role, score resume strength,
                and see skill gaps recruiters may notice.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    model = load_model()

    with st.sidebar:
        st.header("Prediction Settings")
        target_role = st.selectbox("Target role", ["Auto-detect"] + list(ROLE_SKILLS.keys()))
        st.caption("Choose a target role to focus the skill-gap analysis.")
        st.markdown("---")
        st.subheader("Supported Formats")
        st.write("TXT, PDF, DOCX")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("Resume Input")
        uploaded_file = st.file_uploader("Upload resume", type=["txt", "pdf", "docx"])
        pasted_text = st.text_area("Or paste resume text", height=320, placeholder="Paste the resume content here...")

    with col2:
        st.subheader("Role Skill Blueprint")
        role_to_preview = target_role if target_role != "Auto-detect" else "Data Scientist"
        st.write(f"Top keywords for `{role_to_preview}`")
        render_skill_chips(ROLE_SKILLS[role_to_preview])

    resume_text = ""
    if uploaded_file is not None:
        try:
            resume_text = read_uploaded_file(uploaded_file)
        except Exception as exc:
            st.error(str(exc))
            return
    elif pasted_text.strip():
        resume_text = pasted_text.strip()

    if st.button("Predict Resume Fit", type="primary", use_container_width=True):
        if not resume_text.strip():
            st.warning("Add a resume first by upload or paste.")
            return

        insights = analyze_resume(
            model=model,
            resume_text=resume_text,
            target_role=None if target_role == "Auto-detect" else target_role,
        )

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Predicted Role", insights.predicted_role)
        metric2.metric("Confidence", f"{insights.confidence * 100:.1f}%")
        metric3.metric("Resume Strength", f"{insights.resume_strength}/100")

        left, right = st.columns([1.05, 0.95])

        with left:
            st.subheader("Role Probability")
            chart_data = {role: score for role, score in insights.role_scores}
            st.bar_chart(chart_data, horizontal=True)

            st.subheader("Detected Skills")
            render_skill_chips(insights.matched_skills)

            st.subheader("Missing Skills For Target")
            render_skill_chips(insights.missing_skills, missing=True)

        with right:
            st.subheader("Resume Signals")
            experience_label = (
                f"{insights.experience_years} years"
                if insights.experience_years is not None
                else "Not clearly stated"
            )
            education_label = ", ".join(insights.education_signals) if insights.education_signals else "No strong signal found"
            st.markdown(f'<div class="metric-card"><strong>Experience:</strong> {experience_label}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card" style="margin-top:0.8rem;"><strong>Education:</strong> {education_label}</div>', unsafe_allow_html=True)

            st.subheader("Improvement Tips")
            for tip in insights.improvement_tips:
                st.write(f"- {tip}")

        with st.expander("Extracted Resume Text Preview"):
            st.write(resume_text[:3000] if resume_text else "No text extracted.")


if __name__ == "__main__":
    main()
