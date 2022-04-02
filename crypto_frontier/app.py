import efficient_frontier
import streamlit as st

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    df = efficient_frontier.load_data(path="./data/Funds.csv")
    df, fund_names, fund_means = efficient_frontier.pre_process_data(df)
    df, risk, returns = efficient_frontier.efficient_frontier(df, fund_names, fund_means, n_portfolios=100)

    efficient_frontier.plot_frontier(risk, returns)
    plt.show()

st.title("CryptoFrontier")
n_portfolios = st.slider('Choose number of generated portfolios', 20, 500)
df = efficient_frontier.load_data(path="./data/Funds.csv")
df, fund_names, fund_means = efficient_frontier.pre_process_data(df)
df, risk, returns = efficient_frontier.efficient_frontier(df, fund_names, fund_means, n_portfolios=n_portfolios)

fig, ax = plt.subplots()
ax.scatter(risk, returns)
ax.set_xlabel("Risk (%)")
ax.set_ylabel("Returns (%)")

st.pyplot(fig)