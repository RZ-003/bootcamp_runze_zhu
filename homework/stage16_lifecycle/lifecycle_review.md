# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
|**1. Problem Framing & Scoping**| The problem is to decide if we should invest more in Tesla next quarter. We assumed other portfolio weights stay fixed. The tricky part was short-term noise vs long-term signals, and the success means having a model that can predict reasonably well.|
|**2. Tooling Setup** | I used Python with yfinance, pandas, numpy, matplotlib, and sklearn package. Faced the environment issues but fixed with requirements.txt.|
|**3. Python Fundamentals**| I used the DataFrame ops, loops and functions, and I need to keep improving vectorization and the class struction in python.|
|**4. Data Acquisition / Ingestion** | The data is from yfinance, and saved to CSVs. Next time, I can schedule automatic daily ingestion with logging. |
|**5. Data Storage**| I stored raw data as CSV at data/raw and processed data as parquet data/processed. |
|**6. Data Preprocessing**| I renamed columns and computed returns.|
|**7. Outlier Analysis**| I found outliers with histograms and boxplots.|
|**8. Exploratory Data Analysis (EDA)**| I plotted prices vs return, and some patterns were noisy.|
|**9. Feature Engineering**| I built return and rolling averages, and tested for usefulness by checking correlations. |
|**10. Modeling (Regression / Time Series / Classification)**| I used linear regression, with train/test split, and got the overfitiing and unstable results.|
|**11. Evaluation & Risk Communication**| I measured the model with RMSE.|
|**12. Results Reporting, Delivery Design & Stakeholder Communication**| I orgnized results in notebook with charts, and wrote some concise takeaways.|
|**13. Productization**| I reorganized my model in the model to make it concise and added API interactions.|
|**14. Deployment & Monitoring**| I have not fully deployed and am working on it. |
|**15. Orchestration & System Design**| The workflow is ingest → clean → feature → model → report, and all the steps ran manually. Next time, I can try automate some steps. |
|**16. Lifecycle Review & Reflection**| It is hard to build a useful model to predict the trend in the stock market.|

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  The most difficult stage is feature enginnering because I need to think of useful features.
- Which stage was the most **rewarding**?  The most rewarding stage is the modeling stage.
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages? I think all stages are connected layer by layer. It's like building up a house: only if we have a solid first floor, we can build up the second floor.
- If you repeated this project, what would you **do differently across the lifecycle**?  I will keep mostly the same, but spend more efforts on the feature engineering.
- Which skills do you most want to **strengthen** before your next financial engineering project? Feature engineering skills.

---