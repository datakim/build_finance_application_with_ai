# Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems

Companion code for [*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems*](https://www.manning.com/books/financial-ai-in-practice) by Taehun Kim (Manning). You can also read the book on
[liveBook](https://livebook.manning.com/book/financial-ai-in-practice/welcome).

Each `chapterNN` folder holds that chapter's notebooks, the data they read, and a README that tells you:

- which notebook holds each printed listing, with page numbers;
- how to run it: data, API keys and run time;
- where the code differs from the printed book, and why;
- what to read next: the chapter's references with a note on why each is worth your time, plus newer work the book
  doesn't cover in code, such as time-series and anomaly-detection transformers, foundation models, and merchant cash
  advances.

## Chapters

| Part | Chapter | Folder | What the code does |
|---|---|---|---|
| Part 1: Foundations of financial AI | 1. Introduction to AI in finance | [chapter01](chapter01/) | Reading guide (no code) |
|  | 2. From model to money: A strategist's guide to real-world financial AI | [chapter02](chapter02/) | Alpha Digest prompts: summarization and moderation with the OpenAI API |
|  | 3. Working with Generative AI in finance | [chapter03](chapter03/) | Model evaluation, RAG, LoRA fine-tuning, function calling vs. MCP |
| Part 2: Building AI for credit risk | 4. Risk and compliance: Credit risk fundamentals | [chapter04](chapter04/) | Vintage analysis, survival analysis, WoE and IV |
|  | 5. End-to-end credit scoring for financial applications: A real-world AI approach | [chapter05](chapter05/) | End-to-end credit scorecard: SQL + Airflow data mart, WoE/IV selection, XGBoost, score scaling |
|  | 6. Enhancing BFSI scoring workflows: Advanced binning, monitoring, and explainability | [chapter06](chapter06/) | OptBinning scorecard, PSI monitoring, Evidently drift report |
| Part 3: Building AI for fraud detection | 7. Understanding financial fraud and foundational detection strategies | [chapter07](chapter07/) | Rule-based fraud detection on sample transactions |
|  | 8. Building AI fraud detectors: From supervised scoring to anomaly identification | [chapter08](chapter08/) | SMOTE + LightGBM fraud model with top-N% analysis; autoencoder anomaly detection |
|  | 9. Unveiling hidden connections: Graph-based analytics for advanced fraud detection | [chapter09](chapter09/) | Transaction graph, Louvain fraud rings, a simple GNN |
| Part 4: Building AI for investment strategies | 10. Building the quantitative engine: Market direction prediction with machine learning | [chapter10](chapter10/) | ETF direction prediction with embargoed time-series cross-validation |
|  | 11. Building the qualitative engine with news analysis and LLMs | [chapter11](chapter11/) | News ingestion from four sources, ChromaDB, an LLM analyst with RAG |
|  | 12. Augmenting investment decisions: LLM-guided portfolio allocation | [chapter12](chapter12/) | LLM-guided monthly ETF allocation with macro data, backtested |
| Part 5: Building AI for customer and operational excellence | 13. Enhancing customer experience: Building a personalization engine | [chapter13](chapter13/) | Financial-DNA user vectors, segmentation, semantic content matching |
|  | 14. Driving operational efficiency: Building autonomous retention agents | [chapter14](chapter14/) | Tool-using retention agent, Slack alerts, draft-approve queue, experiment and ROI |

Appendixes A-F are in the book. Appendix A's setup is summarized below.

## Getting started

```bash
# 1. Install Git LFS once (appendix A.5), then clone
git lfs install
git clone https://github.com/datakim/build_finance_application_with_ai.git
cd build_finance_application_with_ai

# 2. Create a Python 3.12 virtual environment (appendix A.2)
python3.12 -m venv finai_env         # Windows: py -3.12 -m venv finai_env
source finai_env/bin/activate        # Windows: finai_env\Scripts\activate

# 3. Install the libraries from listing A.1, plus Jupyter
pip install -r requirements.txt
pip install jupyterlab

# 4. Add your API keys (appendix A.4); needed for chapters 2, 3 and 11-14
cp .env.example .env                 # Windows: copy .env.example .env; then edit .env

# 5. Run each notebook from inside its chapter folder
cd chapter05
jupyter lab
```

`requirements.txt` is listing A.1. If a pinned version won't install on your platform, use the fully resolved lock
file for your system, as appendix A.3 suggests:
[`macos-arm64`](requirements-lock/macos-arm64.txt) (Apple Silicon),
[`linux-x86_64`](requirements-lock/linux-x86_64.txt) or
[`windows-x86_64`](requirements-lock/windows-x86_64.txt). For example:

```bash
pip install -r requirements-lock/macos-arm64.txt
```

### Platform notes

- **macOS:** XGBoost and LightGBM need the OpenMP runtime. If either fails with "library could not be loaded", run
  `brew install libomp`.
- **Intel Macs:** torch 2.12.1, tensorflow 2.21.0 and onnxruntime 1.27.0 publish macOS wheels for Apple Silicon only.
  Remove those lines, along with `torch-geometric`, `sentence-transformers` and `peft`, from `requirements.txt`. You
  lose listing 3.3, the chapter 8 autoencoder, the chapter 9 GNN and the import check in listing A.3; everything
  else runs.
- **Linux:** `pip install torch` from PyPI pulls the CUDA build, several GB of NVIDIA libraries. For a CPU-only
  install, run `pip install torch==2.12.1 --index-url https://download.pytorch.org/whl/cpu` before
  `pip install -r requirements.txt`.
- **TA-Lib (chapter 10):** install the C library first (`brew install ta-lib` on macOS, or your distribution's
  TA-Lib development package on Linux), then `pip install TA-Lib`.
- **Apache Airflow (chapters 5 and 13):** optional, and best kept in a separate virtual environment. See the
  chapter 5 README for the install command with Airflow's constraints file.
- **GPU:** only listing 3.3 (fine-tuning an 8B model) needs one.

### Download only the data you need

A full clone downloads about 390 MB of Git LFS data. To fetch one chapter's data at a time:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/datakim/build_finance_application_with_ai.git
cd build_finance_application_with_ai
git lfs pull --include="chapter05/*"   # chapters 5 and 6
```

On Windows PowerShell, run `$env:GIT_LFS_SKIP_SMUDGE=1` before `git clone`. Notebooks and the small CSV files are
plain Git files, so they always download, even without Git LFS.

| Folder | Git LFS data | Size |
|---|---|---|
| chapter05 | `train_df_sample.pkl` (chapters 5 and 6) | 334 MB |
| chapter09 | `fraud_transactions.csv` | 2.4 MB |
| chapter13 | `alphastream_user_mart_20260115.csv`, `user_mart_with_cluster.csv`, `content_store.pkl` | 55 MB |
| chapter14 | `user_mart_with_cluster.csv` (same file as in chapter 13, downloaded once) | 31 MB |

`chapter08/creditcard.csv.zip` (69 MB) is a regular Git file, so it comes with every clone.

## API keys and services

| Variable in `.env` | Chapters | Notes |
|---|---|---|
| `OPENAI_API_KEY` | 2, 3, 11, 12, 13, 14 | Billed per call |
| `NEWS_API_KEY` | 11 | Free Developer plan: last month only, 24-hour delay, for development and testing |
| `FRED_API_KEY` | 12 | [Free key](https://fred.stlouisfed.org/docs/api/api_key.html) |
| `SLACK_WEBHOOK_URL` | 14 | Optional Slack incoming webhook; leave empty to skip the post |

Yahoo Finance (`yfinance`, chapters 10 and 12), the World Nuclear News and Google News RSS feeds, and the GDELT API
(chapter 11) need no key. Listing A.2 also shows `WNN_API_KEY` and `SLACK_BOT_TOKEN`, which the code doesn't use, and
leaves out `FRED_API_KEY`, which chapter 12 needs. [`.env.example`](.env.example) lists exactly what the notebooks read.

## Data in this repository

| File | Chapter | What it is |
|---|---|---|
| `chapter04/vintage_data.csv` | 4 | Synthetic vintage curves, generated by the notebook (seed 42) |
| `chapter05/train_df_sample.pkl` | 5, 6 | 100,000-row sample of the [American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction) competition data |
| `chapter07/sample_fraud_data.csv` | 7 | Synthetic transactions, generated by the notebook (seed 42) |
| `chapter08/creditcard.csv.zip` | 8 | [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), ULB Machine Learning Group; ODbL 1.0 / DbCL 1.0 (see the chapter 8 README) |
| `chapter09/fraud_transactions.csv` | 9 | E-commerce transactions with fraud labels: 14,813 rows, 263 fraudulent |
| `chapter13/*.csv`, `content_store.pkl` | 13, 14 | Mock data for the fictional AlphaStream platform, plus metadata for 105 ETFs |

## When the code differs from the printed book

The notebooks follow the printed listings, including the corrections made during production. A notebook differs
only where it has to: a setup cell that loads your API keys, a helper that unzips data, or a fix for a printed line
that doesn't run. Such cells say so, and each chapter README lists every difference with its page number. These
printed listings need a fix to run:

| Page | Listing | Problem | Details |
|---|---|---|---|
| 97 | 5.2 | Imports `PostgresOperator`, which current Airflow Postgres providers no longer include | [chapter05](chapter05/README.md) |
| 141 | 6.9 | `save_html` fails on the categorical index | [chapter06](chapter06/README.md) |
| 236 | 9.6 | `print` at column 0 under `else:` | [chapter09](chapter09/README.md) |
| 284 | 10.10 | `balanced_accuracy_score` isn't imported | [chapter10](chapter10/README.md) |
| 331 | 12.11 | `plt` isn't imported | [chapter12](chapter12/README.md) |
| 346 | 13.1 | Last line indented 6 spaces | [chapter13](chapter13/README.md) |
| 360 | 13.8 | User and content vectors have different lengths | [chapter13](chapter13/README.md) |

One result also changes: the Evidently drift report in figures 6.9 and 6.10 shows 11 of 20 columns drifting because
of a `float16` artifact. With correctly typed data, no column drifts. The [chapter 6 README](chapter06/README.md)
explains why.

## Regulatory update

On April 17, 2026, the Federal Reserve, OCC and FDIC replaced SR 11-7 and OCC Bulletin 2011-12, which appendix E
maps to chapters 5 and 6, with revised interagency model-risk guidance
([SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)). Generative and agentic AI models
are outside its scope. Details are in the [chapter 1 README](chapter01/README.md).

## Related project: lendrisk

[lendrisk](https://github.com/datakim/lendrisk) is an open-source credit-risk and cash-flow lending toolkit by the author (Apache 2.0,
alpha, Python 3.10+). It goes with part 2 of the book:

- monotonic optimal binning, WoE and logistic scorecards with reason-code-ready point tables (chapters 4-6);
- **merchant cash advances and revenue-based financing**, which section 4.1.3 introduces but the hands-on chapters
  don't build: cash-flow features for underwriting, daily holdback simulation under sales shocks, and comparison
  with term loans on a dated-cash-flow basis. See the [chapter 5 README](chapter05/README.md#further-reading).

## Questions and corrections

Open an issue in this repository, or use the liveBook discussion forum for the book.
