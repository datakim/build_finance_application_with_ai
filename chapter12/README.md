# Chapter 12: Augmenting investment decisions: LLM-guided portfolio allocation

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 4: Building AI for investment strategies

Chapter 12 has an LLM propose monthly allocations across five ETFs from momentum, volatility and point-in-time macro data, then backtests the LLM-guided portfolio against a fixed 20% allocation and logs every decision for human review.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 12.1 | Configuration and portfolio universe | 321 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.2 | Collecting macroeconomic and price data | 322 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.3 | System prompt with explicit constraints | 323 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.4 | Momentum and volatility signals | 324 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.5 | Point-in-time macro extraction | 325 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.6 | Constructing the user prompt | 325 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.7 | LLM API call | 326 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.8 | Utility functions for simulation | 327 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.9 | Main simulation loop | 328 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.10 | Performance calculation | 330 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.11 | Performance comparison panels | 331 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.12 | Diagnostic panels | 331 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |
| 12.13 | Decision log output for human review | 333 | [Chapter12_LLM_portfolio.ipynb](Chapter12_LLM_portfolio.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Put `FRED_API_KEY` and `OPENAI_API_KEY` in the repository's `.env` file. A FRED key is free.
2. Run the notebook from inside this folder. Prices come from `yfinance`. The simulation makes six `gpt-4o-mini` calls at temperature 0.3, so allocations vary from run to run.

## Differences from the printed book

- Listing 12.11 (p. 331) uses `plt`, but no chapter 12 listing imports matplotlib. The notebook imports it.
- The "buy-and-hold" baseline keeps 20% in each ETF every month, so it behaves as a monthly-rebalanced equal-weight portfolio rather than one that drifts with prices.
- Keys come from `.env` rather than the printed placeholders.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Federal Reserve Bank of St. Louis, FRED](https://fred.stlouisfed.org/): the source of the macro series in listing 12.2.
- McKinsey & Company, "Harnessing the power of gen AI in private markets" (January 2026): McKinsey on generative AI in private-markets investing.
- [Chen & Pu, "Autonomous market intelligence: Agentic AI nowcasting predicts stock returns" (2026)](https://arxiv.org/abs/2601.11958): agentic AI nowcasting and stock returns.
- [Black & Litterman, "Global portfolio optimization," FAJ 48(5):28-43 (1992)](https://doi.org/10.2469/faj.v48.n5.28): combining market-equilibrium returns with investor views, a natural frame for views that come from an LLM.
- [Harvey & Liu, "Backtesting," JPM 42(1):13-28 (2015)](https://doi.org/10.3905/jpm.2015.42.1.013): how to discount backtested results for the number of strategies tried.

### Before you trust the backtest

- Glasserman & Lin (2023), [arXiv:2309.17322](https://arxiv.org/abs/2309.17322) — see the chapter 11 README. Any LLM
  whose training cut-off falls after your simulation period can leak future knowledge into
  allocation decisions; run the allocation with anonymised tickers as a check.
- The chapter 10 README lists time-series foundation models and the current evidence on their
  usefulness for return forecasting, if you want to swap the quant signal engine.

---

[All chapters](../README.md) · [Chapter 11](../chapter11/README.md) · [Chapter 13](../chapter13/README.md)
