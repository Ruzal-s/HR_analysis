# 📊 HR Analytics Dashboard & Attrition Analysis

## 📋 Project Overview
This project delivers a comprehensive data-driven analysis of workforce metrics to understand the root causes of employee turnover. By combining data processing, exploratory data analysis (EDA), and interactive business intelligence, the project uncovers key attrition drivers—specifically analyzing the impact of working **overtime**, **departmental structures**, and individual **job roles**.

## 💡 Key Business Metrics
*   **Total Employees:** 882
*   **Total Attrition:** 150 employees left the organization
*   **Overall Attrition Rate:** 17% (0.17)

## 🛠️ Tech Stack & Tools
*   **Database Management:** SQL (Data querying and structural joins)
*   **Exploratory Data Analysis:** Python (Pandas, Matplotlib, Seaborn)
*   **Business Intelligence & Dashboarding:** Power BI Desktop

## 📈 Data-Driven Insights
*   **The Overtime Threshold:** Employees who work **Overtime ("Yes")** show a staggering **100% attrition rate** in isolated visual buckets, signaling massive burnout risk. 
*   **Department Breakdown:** The **Sales** department has the highest overall attrition rate at **over 20%**, closely followed by **Human Resources (~19%)**. The **Research & Development** department maintains the healthiest workforce retention (~14%).
*   **Critical Job Roles:** While the overall department trends are useful, breaking data down by specific roles reveals the real risk zones. **Sales Representatives** experience the highest vulnerability with an attrition rate approaching **40%**. Conversely, Directors and Managers show the highest stability.
*   **Demographic Vulnerability:** The **18–25 age group** experiences the highest relative attrition rate (~30%), which steadily declines as age brackets increase.

## 🚀 Recommendations & Action Plans
1.  **Sales Representative Support:** Restructure commission, onboarding, or workload balances for Sales Representatives to counter their near 40% departure rate.
2.  **Overtime Mitigation Strategies:** Implement an automated tracking system to flag employees consistently logging overtime to prevent rapid turnover.
3.  **Early Career Mentorship:** Build targeted engagement and retention programs tailored specifically to employees aged 18–25 to stabilize early tenure groups.

## 📁 Repository Structure
```text
├── data/                  # Raw and processed HR datasets (CSV/Excel files)
├── images/                # Exported data visualizations and dashboard screenshots
├── powerbi/               # Power BI Desktop files (.pbix) including the main dashboard
├── python/                # Jupyter Notebooks and Python scripts for EDA and chart plotting
└── sql/                   # Database schemas and analytical SQL queries
```

## ⚙️ How to View the Dashboard
1. Navigate to the `powerbi/` folder.
2. Open the `.pbix` file using **Power BI Desktop**.
3. Use the dynamic **Gender**, **Department**, and **Overtime** filters on the right pane to drill deeper into the dataset interactively.
