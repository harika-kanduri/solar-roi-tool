#  Solar ROI & Tariff Optimization Tool

An interactive data-driven application to estimate electricity cost savings, solar ROI, and payback period based on real-world tariff structures across Indian states.

---

##  Features

-  Electricity bill calculation using slab-based tariffs  

-  Solar generation estimation based on location  

-  Monthly & yearly savings calculation  

-  Payback period estimation  

-  20-year savings projection  

-  CO₂ emissions reduction estimation  

-  Smart solar system size recommendation  

---

##  Tech Stack

- Python (Pandas, NumPy)

- Streamlit (UI)

- Data Visualization

---

##  How It Works

The tool:

1. Calculates electricity bill using slab-based tariff logic  

2. Estimates solar energy generation using average sun hours  

3. Computes cost savings after solar installation  

4. Calculates ROI and payback period  

---

##  Screenshots

Interactive dashboard built using Streamlit showcasing solar ROI analysis and insights:

###  Input Panel
![Input Panel](assets/input-panel.png)
###  Results & Key Metrics
![Results](assets/results-metrics.png)
###  Cost Comparison
![Cost Comparison](assets/cost-comparison.png)
###  Savings Over Time
![Savings Chart](assets/savings-chart.png)
###  Environmental Impact
![CO2 Impact](assets/co2-impact.png)

---

##  Run Locally

```bash

git clone <your-repo-link>

cd solar-roi-tool

pip install -r requirements.txt

streamlit run app.py
 