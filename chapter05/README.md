# Chapter 5: End-to-end credit scoring for financial applications: A real-world AI approach

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 2: Building AI for credit risk

Chapter 5 builds an end-to-end credit scoring system on a 100,000-row sample of the American Express default-prediction data: a SQL data mart orchestrated by Airflow, data cleaning and exploration, WoE/IV feature selection, XGBoost with cross-validation, and conversion of probabilities into scorecard points.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 5.1 | A simplified SQL script to unify BFSI partial marts | 95 | [sql/credit_data_mart.sql](sql/credit_data_mart.sql) |
| 5.2 | A minimal Airflow DAG for BFSI monthly merges | 97 | [airflow_dag_credit_pipeline.py](airflow_dag_credit_pipeline.py) |
| 5.3 | Environment setup and library imports | 101 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.4 | Loading the local BFSI dataset | 102 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.5 | Summary function | 103 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.6 | Data cleaning steps: dropping, encoding, imputing | 104 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.7 | Target distribution via Plotly donut chart | 105 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.8 | Categorical feature countplots | 107 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.9 | Numeric histograms colored by target | 108 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.10 | WoE and IV for categorical features | 111 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.11 | WoE and IV for numeric features | 112 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.12 | Combining numeric/categorical | 114 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.13 | Execute the "woe" function | 114 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.14 | The xgboost_model function | 116 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.15 | Execute the model function | 117 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.16 | Plotting ROC curves and a confusion matrix | 118 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.17 | BFSI score conversion and distribution | 120 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.18 | Training the final model on all data | 122 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |
| 5.19 | Single-record inference example | 122 | [Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb](Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Fetch the data: `git lfs pull --include="chapter05/*"`. `train_df_sample.pkl` is 334 MB (100,000 rows x 919 columns), and chapter 6 reads the same file.
2. Install `requirements.txt` (on macOS also run `brew install libomp` for XGBoost).
3. Open `Chapter_05_Part1_Build_CSS_from_the_scratch.ipynb` from inside this folder and run all cells. It takes about 30 seconds on a laptop, and the mean fold AUC is about 0.947.
4. The Airflow DAG is optional. Install Airflow in a separate virtual environment:

   ```bash
   pip install "apache-airflow==3.1.7" apache-airflow-providers-postgres \
     --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.1.7/constraints-3.12.txt
   ```

   Then copy `airflow_dag_credit_pipeline.py` and `sql/` into your DAGs folder and create a Postgres connection named `bfsidb`.

## Differences from the printed book

- Listings 5.1 and 5.2 (pp. 95-97) are in `sql/credit_data_mart.sql` and `airflow_dag_credit_pipeline.py`. The printed DAG imports `PostgresOperator`, which current Postgres provider releases no longer include, so the file uses `SQLExecuteQueryOperator(conn_id=...)` from the common SQL provider. The DAG also references three SQL scripts that the book doesn't print (`create_monthly_usage.sql`, `create_bureau_lookup.sql`, `create_demographics.sql`); supply your own.
- The book refers to `ch5/train_df_sample.pkl` (p. 100). In this repository the file is `chapter05/train_df_sample.pkl`.
- The notebook adds `random.seed(2023)` before `random.sample` in listing 5.6 (p. 104). Runs are reproducible, but numbers differ slightly from the book's figures.
- In listing 5.14 (p. 116), `predictions` averages each qualifying fold model's predictions on the full dataset, so they are not out-of-fold estimates. Use the per-fold validation AUCs as the honest performance estimate.
- Listings 5.17 and 5.19 compute `offset - factor * log(p / (1 - p))`, so a higher score means lower risk: 650 points corresponds to good:bad odds of 20:1, and every 20 points doubles the odds.
- Two notebooks that used to live here, `Chapter_05_Part2_CSS_modeling_with_optbinning.ipynb` and `Chapter_05_Part3_Monitoring_with_Evidently.ipynb`, hold chapter 6 code. They are now in [`../chapter06/legacy/`](../chapter06/legacy/).

## Further reading

### Regulatory update: US model-risk guidance replaced (April 2026)

Appendix E maps SR 11-7 and OCC Bulletin 2011-12 to chapters 5 and 6. On April 17, 2026, the Federal Reserve, the OCC and the FDIC replaced them with revised interagency guidance on model risk management: [SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) ([guidance text](https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf)) and [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html). The OCC bulletin also rescinds OCC Bulletin 1997-24, *Credit Scoring Models: Examination Guidance*.

Two points matter for this book's systems:

- The new guidance covers traditional statistical and quantitative models and non-generative, non-agentic AI models, such as the scorecards in chapters 4-6. The agencies expect it to be most relevant to banks with more than $30 billion in total assets.
- Generative AI and agentic AI models are explicitly outside its scope (footnote 3 of the guidance). For the LLM systems in chapters 11-14, your own risk-management and governance practices have to fill that gap.

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Apache Airflow documentation](https://airflow.apache.org/docs/): reference for the DAG in listing 5.2.
- [Chen & Guestrin, "XGBoost: A scalable tree boosting system," KDD 2016](https://arxiv.org/abs/1603.02754): the gradient-boosting library behind listing 5.14.
- [Grinsztajn, Oyallon & Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (2022)](https://arxiv.org/abs/2207.08815): why tree ensembles still beat deep learning on most tabular problems.
- [American Express, "American Express - Default Prediction" (Kaggle, 2022)](https://www.kaggle.com/competitions/amex-default-prediction): the competition data behind `train_df_sample.pkl`.
- [Home Credit Group, "Home Credit Default Risk" (Kaggle, 2018)](https://www.kaggle.com/competitions/home-credit-default-risk): another public credit-risk dataset, spread over several related tables.
- Hall, Curtis & Pandey, *Machine Learning for High-Risk Applications* (O'Reilly, 2023): risk management for machine learning in high-stakes settings such as lending: governance, explainability and bias testing.

### Turning probabilities into points: `lendrisk.LogisticScorecard`

Listing 5.17 maps PD to points so that **20 more points double the good:bad odds**
and **650 points ↔ 20:1 odds**. [`lendrisk`](https://github.com/datakim/lendrisk)'s `LogisticScorecard` uses the same
convention (WoE bins → logistic regression → points) and exposes per-bin point contributions, which
is what adverse-action reason codes need. Its default anchor is different (600 points ↔ 50:1), so
to reproduce the book's scale set it explicitly:

```python
from lendrisk import LogisticScorecard
card = LogisticScorecard(pdo=20, base_score=650, base_odds=20)  # same scale as listing 5.17
```

### Beyond the book's code: merchant cash advances (MCA) and revenue-based finance

Section 4.1.3 introduces merchant cash advances, but the hands-on chapters score consumer-style credit
with a bureau-like feature set. Modeling small-business **merchant cash advances** and **revenue-based
financing** works differently: the provider buys a
share of future receivables, collects a fixed percentage (the *holdback*) of each day's sales until a
fixed amount (*principal × factor rate*) is repaid, and charges no interest. A factor rate of 1.12
is a repayment multiple, **not** a 12% annual rate — the effective annual cost depends on how fast
sales repay it. Underwriting therefore hinges on the merchant's *cash flow* rather than on a bureau
score, and the risk question becomes "if sales fall, when do we get paid, and how much cash is left?"

`lendrisk` was built for exactly that question:

- `cashflow_features` / `merchant_features` — revenue level, growth, volatility (coefficient of
  variation), coverage and operating margin at an underwriting cutoff, computed only from history
  before the cutoff (no look-ahead).
- `RevenueAdvance` + `RevenueShock` + `compare_scenarios` — simulate daily holdback payments, payoff
  day, unpaid balance and the merchant's minimum cash under sales shocks; optional payment floors and
  repayment milestones.
- `TermLoan`, `xirr`, `xnpv` — compare against an installment loan on a dated-cash-flow basis.

Start with the [revenue-financing tutorial](https://github.com/datakim/lendrisk/blob/main/docs/tutorials/revenue-financing.md)
or the notebook [01_revenue_financing.ipynb](https://github.com/datakim/lendrisk/blob/main/notebooks/01_revenue_financing.ipynb)
([open in Colab](https://colab.research.google.com/github/datakim/lendrisk/blob/main/notebooks/01_revenue_financing.ipynb)).

Primary sources on how real products work, and on how regulators treat them:

- Stripe, "How Capital for platforms works" (revenue withholding, fixed fee, periodic minimums).
  https://docs.stripe.com/capital/how-capital-for-platforms-works
- Shopify, "Shopify Capital – United States" (revenue-linked repayment, minimum-payment checkpoints).
  https://help.shopify.com/en/manual/finance/shopify-capital/united-states
- New York DFS, 23 NYCRR Part 600 — disclosure rules under the Commercial Finance Disclosure Law
  (N.Y. Financial Services Law §§ 801–811), including a format for *sales-based financing*.
  https://www.dfs.ny.gov/industry_guidance/regulations/final_financial_services/rf_finservices_23nycrr600_text
- U.S. FTC, *FTC v. RCG Advances* — MCA provider and owner banned from the industry for deceptive
  terms and abusive collection (Jan 2022).
  https://www.ftc.gov/news-events/press-releases/2022/01/merchant-cash-advance-providers-banned-industry-ordered-redress
- U.S. FTC, *FTC v. Yellowstone Capital* — $9.8 million settlement over unauthorized withdrawals and
  undisclosed fees (Apr 2021).
  https://www.ftc.gov/news-events/news/press-releases/2021/04/cash-advance-firm-pay-98m-settle-ftc-complaint-it-overcharged-small-businesses
- Federal Reserve Banks, *Small Business Credit Survey* — annual data on applications for loans,
  lines of credit and merchant cash advances. https://www.fedsmallbusiness.org/reports/survey

### Foundation models for tabular credit data

The book uses gradient-boosted trees, and Grinsztajn et al. (cited above) explain why trees still
win on most tabular problems. Two lines of work are worth tracking anyway:

- **TabPFN** — Hollmann et al., "Accurate predictions on small data with a tabular foundation
  model," *Nature* 637:319–326 (2025). https://doi.org/10.1038/s41586-024-08328-6 —
  a transformer pretrained on millions of synthetic datasets; strongest on small tables
  (up to ~10,000 rows), which is the regime of new products and thin-file segments.
  Earlier version: [arXiv:2207.01848](https://arxiv.org/abs/2207.01848).
- **Deep tabular baselines** — Gorishniy et al., "Revisiting deep learning models for tabular data"
  (FT-Transformer), NeurIPS 2021, [arXiv:2106.11959](https://arxiv.org/abs/2106.11959); and Gorishniy et al.,
  "TabM," ICLR 2025, [arXiv:2410.24210](https://arxiv.org/abs/2410.24210). Use them as honest challengers to XGBoost,
  not as defaults: validate on out-of-time data and check that you can still produce reason codes.

---

[All chapters](../README.md) · [Chapter 4](../chapter04/README.md) · [Chapter 6](../chapter06/README.md)
