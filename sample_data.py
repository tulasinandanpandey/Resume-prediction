TRAINING_DATA = [
    {
        "role": "Data Scientist",
        "text": """
        Built machine learning models for churn prediction, customer segmentation, and forecasting.
        Strong Python, pandas, numpy, scikit-learn, statistics, experimentation, feature engineering,
        SQL, Jupyter, model evaluation, and data visualization with matplotlib and seaborn.
        Deployed classification pipelines and presented insights to product and business teams.
        """,
    },
    {
        "role": "Data Scientist",
        "text": """
        Developed NLP solutions, recommendation systems, and predictive analytics using Python.
        Experienced with regression, classification, clustering, A/B testing, hypothesis testing,
        TensorFlow, PyTorch, scikit-learn, SQL, and storytelling through dashboards.
        """,
    },
    {
        "role": "Data Scientist",
        "text": """
        Led end-to-end data science projects, from data cleaning and EDA to model deployment.
        Skilled in machine learning, feature selection, statistics, deep learning, Python, SQL,
        Power BI, experimentation design, and business impact analysis.
        """,
    },
    {
        "role": "Data Analyst",
        "text": """
        Created KPI dashboards, automated reports, cleaned data, and delivered business insights.
        Strong SQL, Excel, Tableau, Power BI, data wrangling, visualization, reporting,
        descriptive analytics, stakeholder communication, and trend analysis.
        """,
    },
    {
        "role": "Data Analyst",
        "text": """
        Performed SQL analysis, built reports in Power BI, validated data quality, and tracked KPIs.
        Hands-on with Excel, dashboards, business intelligence, ad hoc analysis, and data storytelling.
        """,
    },
    {
        "role": "Data Analyst",
        "text": """
        Analyzed sales and marketing performance, designed dashboards, and delivered weekly reporting.
        Experienced in Excel, SQL, Tableau, Power BI, data cleaning, pivots, and insight generation.
        """,
    },
    {
        "role": "Machine Learning Engineer",
        "text": """
        Built scalable ML services, deployed models with Docker and FastAPI, and maintained CI/CD.
        Strong Python, MLOps, model serving, AWS, APIs, feature stores, monitoring,
        scikit-learn, TensorFlow, PyTorch, and production system design.
        """,
    },
    {
        "role": "Machine Learning Engineer",
        "text": """
        Productionized recommendation and computer vision models using Kubernetes, Docker, and cloud services.
        Experienced in Python, ML pipelines, model deployment, monitoring, data pipelines, and APIs.
        """,
    },
    {
        "role": "Machine Learning Engineer",
        "text": """
        Engineered robust ML infrastructure with automated training jobs, experiment tracking,
        deployment pipelines, FastAPI services, cloud architecture, and model observability.
        """,
    },
    {
        "role": "Data Engineer",
        "text": """
        Designed ETL pipelines, batch and streaming workflows, and cloud data warehouses.
        Skilled in Spark, Airflow, Python, SQL, dbt, Kafka, data modeling, AWS, and pipeline orchestration.
        """,
    },
    {
        "role": "Data Engineer",
        "text": """
        Built reliable ELT systems, optimized warehouse models, and managed ingestion pipelines.
        Hands-on with SQL, Airflow, dbt, Snowflake, Spark, AWS, and data architecture.
        """,
    },
    {
        "role": "Data Engineer",
        "text": """
        Developed scalable data platforms with ETL, orchestration, transformation testing,
        schema design, distributed processing, and cloud storage optimization.
        """,
    },
    {
        "role": "Business Analyst",
        "text": """
        Gathered requirements, created reports, tracked KPIs, and aligned business and technical teams.
        Strong Excel, SQL, dashboarding, stakeholder management, documentation, and process analysis.
        """,
    },
    {
        "role": "Business Analyst",
        "text": """
        Conducted market and operational analysis, documented business processes, and supported strategic planning.
        Experienced in reporting, Excel, Power BI, KPI definition, and requirement gathering.
        """,
    },
    {
        "role": "Business Analyst",
        "text": """
        Interpreted business needs into analytical requirements, built reports, and communicated insights.
        Skilled in process mapping, stakeholder communication, SQL, Excel, and performance analysis.
        """,
    },
]


ROLE_SKILLS = {
    "Data Scientist": [
        "python",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "statistics",
        "machine learning",
        "deep learning",
        "nlp",
        "sql",
        "a/b testing",
        "feature engineering",
        "forecasting",
        "clustering",
    ],
    "Data Analyst": [
        "sql",
        "excel",
        "tableau",
        "power bi",
        "reporting",
        "dashboard",
        "data visualization",
        "analysis",
        "business intelligence",
        "kpi",
        "data cleaning",
    ],
    "Machine Learning Engineer": [
        "python",
        "docker",
        "kubernetes",
        "fastapi",
        "aws",
        "mlops",
        "tensorflow",
        "pytorch",
        "model deployment",
        "ci/cd",
        "api",
        "monitoring",
    ],
    "Data Engineer": [
        "spark",
        "airflow",
        "dbt",
        "sql",
        "python",
        "etl",
        "elt",
        "kafka",
        "snowflake",
        "aws",
        "data modeling",
        "pipelines",
    ],
    "Business Analyst": [
        "excel",
        "sql",
        "documentation",
        "stakeholder management",
        "requirements gathering",
        "process analysis",
        "reporting",
        "power bi",
        "kpi",
    ],
}


GLOBAL_SKILLS = sorted({skill for skills in ROLE_SKILLS.values() for skill in skills})
