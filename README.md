# Credit Risk Analysis

This is a beginner-level data analysis project where I explored the German Credit Dataset to understand credit risk and predict whether a loan applicant is likely to default.

It was built as part of my learning journey with **PySpark**, **Pandas**, and **Scikit-learn**.

---

## What This Project Does

I wanted to understand how banks and financial institutions decide whether to approve a loan. Using a real-world dataset, I:

- Explored and cleaned the data to understand what information we have about each applicant
- Applied some basic rules to categorise applicants by risk level
- Trained a simple machine learning model to predict loan default probability
- Looked at which factors (like credit history or loan duration) matter the most

---

## Project Structure

```
credit-risk-analysis/
├── credit_risk_analysis.py       # Main script — run this to see the analysis
├── data/
│   └── german_credit_data.csv    # The dataset
├── credit_risk-analysis/         # Additional project files
├── requirements.txt              # List of required Python libraries
└── README.md
```

---

## Dataset

I used the **German Credit Dataset**, a popular beginner-friendly dataset for learning credit risk modelling. It has information on 1,000 loan applicants — things like their account balance, credit history, employment status, and loan purpose.

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))
- **Records:** 1,000 applicants
- **Goal:** Predict whether an applicant is a good or bad credit risk

---

## Tools and Libraries Used

| What I used | Why |
|---|---|
| Python 3 | Main programming language |
| Pandas | Loading and exploring the data |
| PySpark | Processing data at scale |
| Scikit-learn | Building the machine learning model |
| Matplotlib | Plotting charts and visualisations |

---

## How to Run This Project

I am using Python 3 and a virtual environment to keep things clean.

**Step 1 — Clone the repo:**
```bash
git clone https://github.com/jan-jo/credit-risk-analysis.git
cd credit-risk-analysis
```

**Step 2 — Create a virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

**Step 3 — Install the required libraries:**
```bash
pip install -r requirements.txt
```

**Step 4 — Run the analysis:**
```bash
python credit_risk_analysis.py
```

That's it! The script will load the data, run the analysis, and print the results.

---

## What I Learned

- How to load and clean a real-world dataset using Pandas
- How to use Scikit-learn to train and evaluate a classification model
- How to identify which features have the most impact on predictions
- Basics of working with PySpark for data processing

---

## Things I Want to Improve

- Add a Jupyter Notebook so the analysis is easier to follow step by step
- Try other models like Random Forest or Logistic Regression and compare results
- Add proper comments throughout the code
- Improve visualisations

---

## Author

**Janak Raj Joshi** — Computer Engineering Student  
[github.com/jan-jo](https://github.com/jan-jo) · [jjnkjoshi@gmail.com](mailto:jjnkjoshi@gmail.com)

---

## License

This project is open source and available under the [MIT License](LICENSE).
