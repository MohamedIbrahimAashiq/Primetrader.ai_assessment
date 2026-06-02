# 📊 Trader Performance Analysis Using Bitcoin Fear & Greed Sentiment

## 👤 Author

**Mohamed Ibrahim Aashiq**

---

## 🗂️ Project Overview

This project analyzes the relationship between trader performance and Bitcoin market sentiment using the Fear & Greed Index and historical trading data from Hyperliquid.

The main goal was to understand how different market sentiment conditions affect trading outcomes and to identify useful patterns that can support better trading decisions.

The project includes:

- 🧹 Data cleaning and preprocessing
- 📈 Sentiment-based performance analysis
- 🔗 Correlation analysis
- 🪙 Coin-level analysis
- ⚖️ Buy vs. Sell comparison
- 📅 Monthly performance analysis
- 🤖 Trader clustering using K-Means
- 🖥️ Interactive Streamlit dashboard

---

## 📁 Datasets Used

### 1. Historical Trader Data

This dataset contains trading activity from Hyperliquid, including:

- Account
- Coin
- Execution Price
- Trade Size
- Buy/Sell Side
- Closed PnL
- Timestamp

---

### 2. Bitcoin Fear & Greed Index

This dataset contains daily market sentiment information:

- Date
- Fear & Greed Score
- Sentiment Classification

| Score Range | Sentiment       |
|-------------|-----------------|
| 0 – 24      | 😨 Extreme Fear |
| 25 – 49     | 😟 Fear         |
| 50          | 😐 Neutral      |
| 51 – 74     | 😀 Greed        |
| 75 – 100    | 🤑 Extreme Greed|

---

## ⚙️ Project Workflow

### Step 1 – 🧹 Data Cleaning

Both datasets were cleaned by:

- Removing unnecessary whitespace
- Converting timestamps to datetime format
- Handling missing values
- Converting numeric columns to proper data types

---

### Step 2 – 🔗 Data Integration

The trader dataset was merged with the Fear & Greed dataset using trade dates, allowing each trade to be linked with the market sentiment present on that day.

---

### Step 3 – 🛠️ Feature Engineering

Additional features were created:

- Trade Value
- Win/Loss Indicator
- Month
- Fear & Greed Numerical Score

These features helped support deeper analysis.

---

### Step 4 – 🔍 Exploratory Data Analysis

#### Market Sentiment Distribution

Understanding trading activity across:

- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

#### Performance by Sentiment

Metrics analyzed:

- Total PnL
- Average PnL
- Win Rate
- Trade Count

---

### Step 5 – 📉 Correlation Analysis

The relationship between the Fear & Greed score and trader profitability was analyzed.

**Result:**

> Correlation ≈ **0.008** — indicating a very weak linear relationship between sentiment score and profitability.

---

### Step 6 – 🏆 Top Trader Analysis

Identified:

- Top 10 profitable traders during Fear
- Top 10 profitable traders during Greed
- Performance comparison across sentiment conditions

---

### Step 7 – 🪙 Coin Performance Analysis

Coin-level performance was analyzed under different sentiment conditions.

Metrics:

- Total PnL
- Trade Count
- Win Rate

A heatmap was used to visualize the results.

---

### Step 8 – ⚖️ Buy vs. Sell Analysis

Compared BUY and SELL trades across different market sentiment conditions.

---

### Step 9 – 📅 Monthly Performance Analysis

Monthly trends were analyzed to observe changes in trader profitability over time.

---

### Step 10 – 🤖 Trader Clustering

K-Means clustering was applied using:

- Total PnL
- Average PnL
- Trade Count
- Win Rate
- Average Trade Value

This grouped traders into distinct behavioral categories.

---

## 💡 Key Findings

- Trader performance varies significantly under different market sentiment conditions.
- Extreme Greed periods generated the highest trading activity.
- The Fear & Greed score alone does not strongly predict trader profitability.
- Some traders consistently perform better during Fear periods.
- Coin performance varies across different sentiment conditions.
- Buy and Sell trades behave differently depending on market sentiment.
- Trader clustering revealed distinct trading behavior patterns.

---

## 📌 Business Recommendations

1. **📊 Use sentiment as a supporting indicator** — not as the sole trading signal.
2. **👁️ Monitor Fear-period outperformers** — track traders who consistently profit during Fear markets.
3. **🛡️ Apply stronger risk management** during Extreme Greed periods.
4. **🪙 Focus on high-performing coins** that historically do well under specific sentiment conditions.
5. **🔄 Combine signals** — pair sentiment analysis with trade size, leverage, and broader market conditions for better decisions.

---

## 🖥️ Streamlit Dashboard

An interactive Streamlit dashboard was developed to visualize the analysis results.

**Features include:**

- 🔍 Market sentiment filtering
- 🪙 Coin filtering
- 📊 Performance metrics
- 🔗 Correlation analysis
- 🗺️ Coin performance analysis
- ⚖️ Buy vs. Sell comparison
- 📅 Monthly performance trends
- 🤖 Trader clustering
- 🏆 Top trader analysis

---

## 📸 Dashboard Screenshots

### Dashboard Overview
![Dashboard Overview](/images/img-1.png)

### Market Sentiment Performance
![Market Sentiment Performance](images/img-2.png)

### Fear & Greed Correlation and Coin Analysis
![Correlation Analysis](images/img-3.png)

### Coin Performance and Buy vs. Sell Analysis
![Coin Performance](images/img-4.png)

### Monthly Performance Analysis
![Monthly Analysis](images/img-5.png)

### Trader Clustering
![Trader Clustering](images/img-6.png)

### Top Traders by Sentiment
![Top Traders](images/img-7.png)

---

## 📂 Project Files

```text
analysis1.ipynb         ← Main analysis notebook
app.py                  ← Streamlit dashboard app
requirements.txt        ← Python dependencies

historical_data.csv     ← Raw trader data from Hyperliquid
fear_greed_index.csv    ← Bitcoin Fear & Greed Index data

merged_trader_sentiment_data.csv
sentiment_summary.csv
coin_summary.csv
monthly_summary.csv
side_summary.csv
trader_clusters.csv
```

---

## ▶️ Running the Notebook

Install dependencies:

```bash
pip install -r requirements.txt
```

Open and run all cells in:

```text
analysis1.ipynb
```

This will generate the following processed CSV files:

```text
merged_trader_sentiment_data.csv
sentiment_summary.csv
coin_summary.csv
monthly_summary.csv
side_summary.csv
trader_clusters.csv
```

---

## 🚀 Running the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser automatically.

---

## ✅ Conclusion

This project explored how Bitcoin market sentiment relates to trader performance using real trading data and the Fear & Greed Index. The analysis showed that sentiment categories provide useful insights into trading behavior, while the numerical sentiment score alone has a very weak relationship with profitability. The results can help support sentiment-aware trading strategies and better risk management decisions.
