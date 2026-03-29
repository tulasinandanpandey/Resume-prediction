# AI Resume Prediction App

A Streamlit app that predicts the best-fit data role for a resume and highlights skill gaps.

## Features

- Predicts likely roles such as Data Scientist, Data Analyst, Data Engineer, Machine Learning Engineer, and Business Analyst
- Accepts pasted text or uploaded `TXT`, `PDF`, and `DOCX` resumes
- Detects role-relevant skills, estimates prediction confidence, and scores resume strength
- Highlights missing keywords for a target role and suggests improvements

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: AI resume prediction app"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Choose `New app`.
4. Select your GitHub repository and set the main file path to `app.py`.
5. Deploy.

## Notes

- The model is trained locally from bundled sample resume text for demo and portfolio use.
- For better accuracy, replace `sample_data.py` with a larger labeled resume dataset.
