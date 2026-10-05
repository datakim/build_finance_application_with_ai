# Chapter 8: Building AI fraud detectors: From supervised scoring to anomaly identification

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 3: Building AI for fraud detection

Chapter 8 builds two fraud detectors on the public credit-card fraud dataset: a supervised SMOTE + LightGBM pipeline tuned for recall and evaluated with a top-N% capture table, and an unsupervised autoencoder trained only on legitimate transactions that scores fraud by reconstruction error.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 8.1 | Loading and basic exploration of the credit card fraud dataset | 189 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.2 | Scaling numerical features and splitting data | 192 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.3 | Defining the SMOTE-LightGBM pipeline and hyperparameter distributions | 195 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.4 | Performing RandomizedSearchCV to train and tune the model | 196 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.5 | Comprehensive evaluation of the tuned model on the test set | 198 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.6 | Preparing data for top-N% analysis | 200 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.7 | Calculating and displaying precision and fraud capture rate at the top N% of segments | 200 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.8 | Visualizing precision and fraud capture rate at the top N% | 203 | [Chapter_08_FDS_supervised.ipynb](Chapter_08_FDS_supervised.ipynb) |
| 8.1 | Loading and basic exploration of the credit card fraud dataset | 189 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.2 | Scaling numerical features and splitting data | 192 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.9 | Preparing training and test sets for the autoencoder | 206 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.10 | Defining and compiling the autoencoder architecture | 207 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.11 | Training the autoencoder on legitimate transactions | 209 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.12 | Calculating reconstruction errors on the full test set | 211 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |
| 8.13 | Visualizing reconstruction errors with scatter plots | 212 | [Chapter_08_FDS_unsupervised.ipynb](Chapter_08_FDS_unsupervised.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. The data ships as `creditcard.csv.zip` because the CSV (about 150 MB) is over GitHub's 100 MB file limit. The first code cell of each notebook extracts `creditcard.csv` once.
2. **Supervised:** run `Chapter_08_FDS_supervised.ipynb` from inside this folder. It takes about a minute on a laptop. On macOS, install OpenMP first (`brew install libomp`) if LightGBM won't load.
3. **Unsupervised:** needs TensorFlow (`tensorflow==2.21.0`, already in `requirements.txt`). Training writes `best_autoencoder_model_ch8.keras` into this folder.

## Data

**Dataset:** [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), Machine Learning Group, Université Libre de Bruxelles (ULB), in collaboration with Worldline: 284,807 European card transactions from September 2013, 492 of them fraudulent. Kaggle lists it under the Open Database License (ODbL 1.0) for the database and the Database Contents License (DbCL 1.0) for its contents. If you use it, cite Dal Pozzolo et al., "Calibrating probability with undersampling for unbalanced classification," IEEE SSCI 2015.

## Differences from the printed book

- With the pinned versions, the supervised notebook reproduces the book's numbers exactly: cross-validated recall 0.8894 (p. 197); test recall 0.86, precision 0.22, AUC-ROC 0.9728 and AUC-PR 0.7247 (p. 199); and the top-N% table on p. 202.
- In listing 8.3 (p. 195), LightGBM ignores `subsample` unless `subsample_freq` (bagging frequency) is set above 0, so row subsampling has no effect. The code is kept as printed.
- The two "To save space... refer to GitHub" comments at the top of listing 8.1 are omitted, because this is the GitHub version.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Ke et al., "LightGBM: A highly efficient gradient boosting decision tree," NeurIPS 2017](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree): the boosting library in listings 8.3 and 8.4.
- [ULB Machine Learning Group, "Credit card fraud detection" (Kaggle dataset)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud): the dataset used throughout the chapter.
- [Dal Pozzolo et al., "Calibrating probability with undersampling for unbalanced classification," IEEE SSCI 2015](https://doi.org/10.1109/SSCI.2015.33): how undersampling distorts predicted probabilities and how to correct them. The dataset's authors ask you to cite this paper.
- [Lemaitre, Nogueira & Aridas, "Imbalanced-learn," JMLR 18(17):1-5 (2017)](https://jmlr.org/papers/v18/16-365.html): the library behind the SMOTE pipeline in listing 8.3.
- [Chalapathy & Chawla, "Deep learning for anomaly detection: A survey" (2019)](https://arxiv.org/abs/1901.03407): a survey of deep anomaly detection, including autoencoders.
- [Liu, Ting & Zhou, "Isolation forest," IEEE ICDM 2008](https://doi.org/10.1109/ICDM.2008.17): the classic unsupervised baseline to compare the autoencoder against.

### Transformers for anomaly detection (not covered in the book)

The chapter's autoencoder scores each transaction independently. Much fraud and operational-risk
signal is *sequential* — a card's transaction stream, a session's event log, a merchant's daily
volume. Time-series anomaly transformers model that context directly:

- **Anomaly Transformer** — Xu, Wu, Wang & Long, "Anomaly Transformer: Time series anomaly
  detection with association discrepancy," ICLR 2022. [arXiv:2110.02642](https://arxiv.org/abs/2110.02642) —
  anomalous points attend mostly to their neighbours; the gap between learned attention and a local
  prior becomes the anomaly score.
- **TranAD** — Tuli, Casale & Jennings, "TranAD: Deep transformer networks for anomaly detection in
  multivariate time series data," VLDB 2022. [arXiv:2201.07284](https://arxiv.org/abs/2201.07284) — transformer with
  adversarial training and meta-learning, built for fast training and low-latency inference
  (the authors report up to 99% shorter training time than baselines).
- **DCdetector** — Yang et al., "DCdetector: Dual attention contrastive representation learning for
  time series anomaly detection," KDD 2023. [arXiv:2306.10347](https://arxiv.org/abs/2306.10347).
- **A foundation-model route** — Goswami et al., "MOMENT: A family of open time-series foundation
  models," ICML 2024. [arXiv:2402.03885](https://arxiv.org/abs/2402.03885) — open pretrained models whose model card
  lists anomaly detection alongside forecasting, classification and imputation; useful when you have
  little labelled data.
- **Survey** — Wen et al., "Transformers in time series: A survey," IJCAI 2023.
  [arXiv:2202.07125](https://arxiv.org/abs/2202.07125) — includes a section on anomaly detection.

Read this before trusting leaderboard numbers:

- Wu & Keogh, "Current time series anomaly detection benchmarks are flawed and are creating the
  illusion of progress," IEEE TKDE (extended abstract at ICDE 2022).
  [arXiv:2009.13807](https://arxiv.org/abs/2009.13807) — most exemplars in the widely used Yahoo, Numenta and NASA
  benchmarks have at least one of four flaws, so much of the apparent recent progress may be illusory;
  the authors release the UCR anomaly archive as a sounder alternative.
  For fraud, evaluate on your own labelled history with time-ordered splits, and compare every deep
  model against the isolation-forest baseline cited above.

If your fraud data is tabular rather than sequential, the deep-tabular baselines in the chapter 5
README (FT-Transformer, TabM) are the relevant comparison for LightGBM.

---

[All chapters](../README.md) · [Chapter 7](../chapter07/README.md) · [Chapter 9](../chapter09/README.md)
