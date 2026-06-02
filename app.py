import pandas as pd
import streamlit as st
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Trader Sentiment Dashboard",
    layout="wide"
)

st.title("Trader Performance vs Market Sentiment Dashboard")

st.write(
    "This dashboard analyzes how trader performance changes across "
    "Bitcoin Fear and Greed market sentiment conditions."
)


# Load processed CSV files
@st.cache_data
def load_data():
    merged = pd.read_csv("merged_trader_sentiment_data.csv")
    sentiment_summary = pd.read_csv("sentiment_summary.csv")
    coin_summary = pd.read_csv("coin_summary.csv")
    monthly_summary = pd.read_csv("monthly_summary.csv")
    side_summary = pd.read_csv("side_summary.csv")
    trader_clusters = pd.read_csv("trader_clusters.csv")

    return (
        merged,
        sentiment_summary,
        coin_summary,
        monthly_summary,
        side_summary,
        trader_clusters
    )


merged, sentiment_summary, coin_summary, monthly_summary, side_summary, trader_clusters = load_data()


# Sidebar filters
st.sidebar.header("Filters")

selected_sentiments = st.sidebar.multiselect(
    "Select market sentiment",
    options=sorted(merged["classification"].dropna().unique()),
    default=sorted(merged["classification"].dropna().unique())
)

selected_coins = st.sidebar.multiselect(
    "Select coins",
    options=sorted(merged["Coin"].dropna().unique()),
    default=sorted(merged["Coin"].dropna().unique())[:10]
)

filtered_data = merged[
    (merged["classification"].isin(selected_sentiments)) &
    (merged["Coin"].isin(selected_coins))
]


# Dataset overview
st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trades", f"{len(filtered_data):,}")
col2.metric("Unique Traders", filtered_data["Account"].nunique())
col3.metric("Unique Coins", filtered_data["Coin"].nunique())
col4.metric("Total PnL", f"{filtered_data['closedPnL'].sum():,.2f}")


# Key performance metrics
st.subheader("Key Performance Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average PnL", f"{filtered_data['closedPnL'].mean():,.4f}")
col2.metric("Median PnL", f"{filtered_data['closedPnL'].median():,.4f}")
col3.metric("Win Rate", f"{filtered_data['is_win'].mean() * 100:.2f}%")


# Sentiment performance
st.subheader("Performance by Market Sentiment")

filtered_sentiment_summary = filtered_data.groupby("classification").agg(
    total_trades=("closedPnL", "count"),
    total_pnl=("closedPnL", "sum"),
    average_pnl=("closedPnL", "mean"),
    median_pnl=("closedPnL", "median"),
    win_rate=("is_win", "mean"),
    average_trade_value=("trade_value", "mean")
).reset_index()

filtered_sentiment_summary["win_rate"] = filtered_sentiment_summary["win_rate"] * 100

st.dataframe(filtered_sentiment_summary, use_container_width=True)

fig1 = px.bar(
    filtered_sentiment_summary,
    x="classification",
    y="total_pnl",
    title="Total PnL by Market Sentiment",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    filtered_sentiment_summary,
    x="classification",
    y="win_rate",
    title="Win Rate by Market Sentiment",
    text_auto=".2f"
)

st.plotly_chart(fig2, use_container_width=True)


# Correlation section
st.subheader("Fear & Greed Score vs PnL")

correlation_value = filtered_data[["fear_greed_value", "closedPnL"]].corr().iloc[0, 1]

st.write(
    f"The correlation between Fear & Greed score and PnL is **{correlation_value:.4f}**."
)

st.info(
    "A correlation value close to 0 means sentiment score alone does not strongly explain trader profitability."
)

sample_data = filtered_data.sample(
    min(5000, len(filtered_data)),
    random_state=42
)

fig3 = px.scatter(
    sample_data,
    x="fear_greed_value",
    y="closedPnL",
    title="Fear & Greed Score vs PnL",
    opacity=0.5
)

st.plotly_chart(fig3, use_container_width=True)


# Coin performance
st.subheader("Coin Performance")

filtered_coin_summary = filtered_data.groupby(["Coin", "classification"]).agg(
    total_pnl=("closedPnL", "sum"),
    total_trades=("closedPnL", "count"),
    win_rate=("is_win", "mean")
).reset_index()

filtered_coin_summary["win_rate"] = filtered_coin_summary["win_rate"] * 100

st.dataframe(filtered_coin_summary, use_container_width=True)

top_coins = (
    filtered_data.groupby("Coin")["closedPnL"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

fig4 = px.bar(
    top_coins,
    x="Coin",
    y="closedPnL",
    title="Top 20 Coins by Total PnL",
    text_auto=".2s"
)

st.plotly_chart(fig4, use_container_width=True)


# Buy vs Sell analysis
st.subheader("Buy vs Sell Performance")

filtered_side_summary = filtered_data.groupby(["classification", "Side"]).agg(
    total_trades=("closedPnL", "count"),
    total_pnl=("closedPnL", "sum"),
    win_rate=("is_win", "mean")
).reset_index()

filtered_side_summary["win_rate"] = filtered_side_summary["win_rate"] * 100

st.dataframe(filtered_side_summary, use_container_width=True)

fig5 = px.bar(
    filtered_side_summary,
    x="classification",
    y="total_pnl",
    color="Side",
    barmode="group",
    title="Buy vs Sell PnL by Sentiment"
)

st.plotly_chart(fig5, use_container_width=True)


# Monthly performance
st.subheader("Monthly Sentiment Performance")

filtered_monthly_summary = filtered_data.groupby(["month", "classification"]).agg(
    total_pnl=("closedPnL", "sum"),
    total_trades=("closedPnL", "count")
).reset_index()

fig6 = px.line(
    filtered_monthly_summary,
    x="month",
    y="total_pnl",
    color="classification",
    markers=True,
    title="Monthly PnL by Market Sentiment"
)

st.plotly_chart(fig6, use_container_width=True)


# Trader clustering
st.subheader("Trader Clustering")

st.write(
    "Trader clusters group accounts based on trading behavior such as total PnL, "
    "trade count, win rate, and trade value."
)

st.dataframe(trader_clusters, use_container_width=True)

fig7 = px.scatter(
    trader_clusters,
    x="total_trades",
    y="total_pnl",
    color="cluster",
    hover_data=["Account", "win_rate", "average_trade_value"],
    title="Trader Clusters Based on Trading Behavior"
)

st.plotly_chart(fig7, use_container_width=True)


# Top traders
st.subheader("Top Traders by Sentiment")

selected_sentiment_for_traders = st.selectbox(
    "Select sentiment",
    options=sorted(filtered_data["classification"].dropna().unique())
)

top_traders = (
    filtered_data[filtered_data["classification"] == selected_sentiment_for_traders]
    .groupby("Account")
    .agg(
        total_pnl=("closedPnL", "sum"),
        total_trades=("closedPnL", "count"),
        win_rate=("is_win", "mean")
    )
    .reset_index()
)

top_traders["win_rate"] = top_traders["win_rate"] * 100

top_traders = top_traders.sort_values(
    "total_pnl",
    ascending=False
).head(10)

st.dataframe(top_traders, use_container_width=True)

fig8 = px.bar(
    top_traders,
    x="Account",
    y="total_pnl",
    title=f"Top 10 Traders During {selected_sentiment_for_traders}",
    text_auto=".2s"
)

st.plotly_chart(fig8, use_container_width=True)


# Business insights
st.subheader("Key Findings and Business Insights")

st.markdown(
    """
    - Trader performance changes across different market sentiment conditions.
    - The numerical Fear & Greed score has a very weak direct relationship with trader PnL.
    - This means sentiment score alone is not enough to explain trader profitability.
    - Some traders perform better during Fear periods, while others perform better during Greed periods.
    - Coin-level performance varies across different sentiment regimes.
    - Buy and Sell trades behave differently depending on market sentiment.
    - Trader clustering helps identify different trader behavior groups and risk profiles.
    """
)

st.subheader("Trading Strategy Recommendations")

st.markdown(
    """
    1. Use market sentiment as a supporting indicator, not as the only trading signal.
    2. Study accounts that consistently perform well during Fear markets.
    3. Apply stronger risk control during Extreme Greed periods because trading activity is higher.
    4. Focus on coins that historically perform well under specific sentiment conditions.
    5. Combine sentiment with trade size, coin selection, leverage, and trader behavior for better decisions.
    """
)


# Download filtered data
st.subheader("Download Filtered Data")

csv = filtered_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered dataset",
    data=csv,
    file_name="filtered_trader_sentiment_data.csv",
    mime="text/csv"
)
