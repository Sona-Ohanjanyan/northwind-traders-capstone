# 🚢 Northwind Traders Capstone Project

## 📊 Project Overview
This capstone project features an end-to-end data analysis and executive dashboard for **Northwind Traders**, built using **Power BI**, **Python**, and **SQL/CSV datasets**.

## 🔍 Key Components & Features
1. **Executive Overview Dashboard:** High-level KPIs, revenue trends, and regional performance.
2. **Product Performance Analysis:** Detailed drill-downs into product categories and sales volumes.
3. **Statistical Thinking & Hypothesis Testing:**
   * **Correlation Analysis:** Evaluated the relationship between discount rates and unit prices ($r = 0.3955$).
   * **Independent T-Test:** Compared unit prices between discounted and non-discounted sales.
   * **Result:** $T\text{-statistic} = 5.9482$, $P\text{-value} = 5.24 \times 10^{-9}$. We reject the null hypothesis ($H_0$), confirming a statistically significant relationship showing higher-priced items receive discounts more frequently to boost sales.

## 🛠️ Tech Stack
* **Visualization:** Power BI Desktop
* **Statistical Analysis:** Python (`pandas`, `scipy.stats`)
* **Data Processing:** CSV / Relational Database (Northwind)
