# Telco Customer Churn & Retention Analysis

![Customer Churn Dashboard](image_fb60bc.png)

A comprehensive Power BI dashboard and exploratory data analysis project built to investigate customer churn patterns, identify high-risk demographic and contract segments, and provide actionable retention insights for telecommunications businesses.

---

## 📊 Project Overview
Customer churn is a critical metric for subscription-based businesses. This project analyzes a Telco dataset to uncover the primary drivers behind customer cancellation. By leveraging data cleaning scripts in Python and an interactive Power BI dashboard, the project highlights key vulnerability windows—such as early-stage tenure and month-to-month contracts—allowing decision-makers to implement targeted retention strategies.

---

## 🛠️ Tech Stack & Tools
* **Data Processing:** Python, Pandas (Handling missing values in `TotalCharges`)
* **Data Visualization & Dashboarding:** Power BI Desktop
* **Data Modeling & Metrics:** DAX (Data Analysis Expressions) for calculated measures (`Churn Rate`, `Total Churned`, `Total Customers`)
* **Version Control:** Git & GitHub

---

## 📈 Key Dashboard Components & Metrics
* **Core KPIs:** Total Customers, Total Churned, and overall Churn Rate percentage.
* **Contract Analysis:** Visualizes how month-to-month contracts drive the vast majority of churn compared to 1-year and 2-year commitments.
* **Payment & Service Impact:** Evaluates cancellation rates across different payment methods (e.g., electronic checks) and internet service tiers (e.g., Fiber Optic).
* **Tenure Timeline:** Tracks customer lifespan via a line chart to isolate the high-risk window within the first 90 days.
* **Interactive Slicers:** Dynamic filtering capabilities for demographic attributes such as Senior Citizen status, Dependents, and Gender.

---

## 📂 Project Structure
```text
├── Telco_Customer_Churn_Analysis.pbix    # Interactive Power BI Dashboard file
├── customer_churn_analysis.py            # Python data preprocessing & cleaning script
├── image_fb60bc.png                      # Dashboard preview image
└── README.md                             # Project documentation
