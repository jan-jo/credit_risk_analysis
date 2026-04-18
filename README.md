Credit Risk Analysis
A data analysis project that applies rule-based and machine learning techniques to the German Credit Dataset to assess credit risk and predict the probability of loan default.
Built with PySpark, Pandas, and Scikit-learn.

Overview
Credit risk assessment is a critical process in financial institutions to determine whether a loan applicant is likely to default. This project explores the German Credit Dataset to perform exploratory data analysis (EDA), engineer relevant features, and build a predictive classification model for loan default probability.
Key objectives:

Perform exploratory data analysis on applicant financial attributes
Apply rule-based logic to categorise credit risk levels
Train and evaluate a machine learning model to predict loan default
Identify the most influential features driving credit risk


Project Structure
credit-risk-analysis/
├── credit_risk_analysis.py       # Main analysis and modelling script
├── data/
│   └── german_credit_data.csv    # German Credit Dataset
├── credit_risk-analysis/         # Additional project files
├── requirements.txt              # Python dependencies
└── README.md

Dataset
This project uses the German Credit Dataset, a widely used benchmark dataset in credit risk modelling. It contains 1,000 records of loan applicants with attributes such as account status, credit history, loan purpose, employment duration, and personal demographics.

Source: UCI Machine Learning Repository
Records: 1,000
Target variable: Credit risk classification (Good / Bad)


Tech Stack
CategoryToolsData ProcessingPySpark, PandasMachine LearningScikit-learnVisualisationMatplotlibLanguagePython 3.x

Getting Started
Prerequisites

Python 3.8 or higher
Java 8+ (required for PySpark)

Installation
1. Clone the repository:
bashgit clone https://github.com/jan-jo/credit-risk-analysis.git
cd credit-risk-analysis
2. Create and activate a virtual environment:
bashpython3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
3. Install dependencies:
bashpip install -r requirements.txt
Running the Analysis
bashpython credit_risk_analysis.py
The script will perform EDA, apply feature engineering, train the model, and print evaluation metrics to the console.

Results
The model achieves competitive performance on the test set. Key evaluation metrics include accuracy, precision, recall, and F1-score. Feature importance analysis highlights credit history, account balance, and loan duration as the strongest predictors of default risk.

Detailed results and visualisations are generated when the script is run.


Future Improvements

Add a Jupyter Notebook for interactive EDA and visualisation
Experiment with additional models (Random Forest, XGBoost, Logistic Regression)
Build a simple REST API to serve predictions
Add cross-validation and hyperparameter tuning


Author
Janak Raj Joshi
github.com/jan-jo · jjnkjoshi@gmail.com

License
This project is open source and available under the MIT License.
