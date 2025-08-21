### Problem Statement
- We are currently holding 100,000 Tesla shares. The PM wants to evaluate whether we should increase our position or reduce it for the next quarter.

### Stakeholder & User
- Decision owner: The PM
- Tool/operator:  The PM(Here we assume the PM knows how to program and run my code.)

### Useful Answer
- Descriptive / Predictive / Causal: The answer should be predictive, as it should states that the Tesla share price will likely raise or drop by a certain percentage.
- Metric or artifact: The answer should be metric as I will report the Expected return over next quarter, the sharpe ratio, and the volatility forecast.

### Assumptions & Constraints
- We assume the rest of the PM's position is unchange, we have access to Tesla’s historical stock prices and market index data, there is no transaction cost, and liquidity.

### Known Unknowns / Risks
- The change of oil price, the investor sentiment around Tesla, and the unpredictable large trades are potential risks

### Lifecycle Mapping
- Goal → Stage → Deliverable mapping bullets
- Goal: Evaluate whether to increase or reduce Tesla position
- Stage: Problem Framing & Scoping (Stage 01)
- Deliverable mapping: Scoping paragraph

### Data Storage
- data/raw/ stores first-hand data which is original and unprocessed, while data/processed/ stores data that is processed in the notebook script and outputted.
- data/raw/ stores mostly csv documents because it is downloaded from other sources, while data/processed stores parquet documents because we can read parquet faster and keep it more compressed.
- "os.getenv('DATA_DIR_RAW', 'data/raw')" Here, we are using the function os.getenv(). This command says if we have the value for 'DATA_DIR_RAW' in the .env, then we use this value; otherwise, we use the default value 'data/raw'.

### Cleaning Strategy
- I first keep the rows that have at least 4 non-null values out of 6. Otherwise, I think that person did not report seriously, so I remove its data. Then, I filled out the nulls at age, income, score and extra_data by using the column-median because I believe they all obey the normal distribution.
