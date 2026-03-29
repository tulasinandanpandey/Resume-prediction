# AI Resume Prediction App

An industry-style data science project that analyzes resumes, predicts the most relevant data role, and highlights skill gaps that can affect recruiter screening.

This app is designed as a portfolio-ready project for data science, machine learning, and analytics profiles. It combines natural language processing, resume keyword analysis, and a clean Streamlit interface to simulate a lightweight AI hiring assistant.

## Why This Project Matters

Recruiters and hiring teams often scan resumes in seconds. Candidates may have strong experience but still miss the keywords, structure, or signals that align with a target role. This project helps solve that problem by:

- Predicting the most likely job fit from resume content
- Surfacing strengths and missing role-specific skills
- Estimating resume quality through an interpretable scoring layer
- Giving actionable suggestions to improve resume relevance

## Key Features

- Multi-role prediction for:
  - Data Scientist
  - Data Analyst
  - Machine Learning Engineer
  - Data Engineer
  - Business Analyst
- Resume input through:
  - Plain text paste
  - `TXT` upload
  - `PDF` upload
  - `DOCX` upload
- NLP-based role prediction using `TF-IDF + Logistic Regression`
- Resume strength scoring based on:
  - model confidence
  - detected technical skills
  - experience signals
  - education signals
- Skill-gap analysis for selected target roles
- Improvement suggestions to make resumes more recruiter-friendly
- Streamlit UI with a polished dashboard layout for local use and cloud deployment

## Tech Stack

- Python
- Streamlit
- scikit-learn
- pypdf
- python-docx

## Model Approach

The current version uses a lightweight supervised text-classification pipeline:

1. Resume text is converted into TF-IDF features.
2. A Logistic Regression classifier predicts the most relevant role.
3. Additional rule-based signals extract:
   - skills
   - education clues
   - years of experience
4. The app combines these outputs into a resume strength score and improvement tips.

This makes the app fast, explainable, and easy to deploy.

## Project Structure

```text
.
|-- app.py
|-- resume_model.py
|-- sample_data.py
|-- requirements.txt
|-- .streamlit/
|   `-- config.toml
`-- README.md
```

## Local Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/tulasinandanpandey/Resume-prediction.git
cd Resume-prediction
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Deployment

This project is ready for deployment on Streamlit Community Cloud.

### Deploy on Streamlit Community Cloud

1. Push the code to your GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click `New app`.
4. Select the repository: `tulasinandanpandey/Resume-prediction`
5. Set the main file path to `app.py`
6. Open `Advanced settings` and choose Python `3.12`
7. Click `Deploy`

## Resume and Portfolio Value

This project is suitable to showcase on a resume under machine learning, data science, or analytics projects.

Example project description:

> Built an AI-powered resume screening application using Python, Streamlit, and scikit-learn to classify resumes into data roles, identify skill gaps, and generate recruiter-oriented feedback.

Example impact bullets:

- Developed an NLP-based resume classification pipeline using TF-IDF and Logistic Regression for multi-role prediction across core data career paths
- Built a recruiter-style scoring workflow to evaluate resume strength using keyword matching, experience extraction, and education signals
- Deployed an interactive Streamlit app supporting `TXT`, `PDF`, and `DOCX` resume uploads for real-time resume analysis

## Current Limitations

- The model is trained on a bundled demo dataset rather than a large real-world labeled resume corpus
- Predictions are useful for portfolio demonstration and prototype workflows, but not production hiring decisions
- Resume parsing is rule-assisted and can miss unusual formatting or highly visual resume layouts

## Recommended Next Improvements

- Train on a larger labeled resume dataset
- Add more job families and specialization tracks
- Save the trained model as an artifact for faster startup
- Add admin analytics, job-description matching, and ATS score comparison
- Deploy with a public app link and add screenshots to this README

## Author

Created as a data science and machine learning portfolio project by [Tulasi Nandan Pandey](https://github.com/tulasinandanpandey).
