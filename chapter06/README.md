# Chapter 6: Enhancing BFSI scoring workflows: Advanced binning, monitoring, and explainability

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 2: Building AI for credit risk

Chapter 6 strengthens the chapter 5 workflow: constrained optimal binning and a scorecard with OptBinning, stability monitoring with the population stability index (PSI), and a data-drift report with Evidently.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 6.1 | Creating the BinningProcess and specifying selection criteria | 129 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.2 | Inspecting a single binned variable | 130 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.3 | Creating and fitting the scorecard | 132 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.4 | Viewing the summary scorecard table | 132 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.5 | Viewing the detailed scorecard table | 133 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.6 | Evaluating the scorecard’s rank-ordering | 134 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.7 | Plotting the final score distribution (event vs. nonevent) | 135 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.8 | Monitoring distribution stability | 136 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |
| 6.9 | Creating and saving the Evidently drift report | 141 | [Chapter06_explainability_and_monitoring.ipynb](Chapter06_explainability_and_monitoring.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Fetch the chapter 5 data: `git lfs pull --include="chapter05/*"`. This notebook reads `../chapter05/train_df_sample.pkl` rather than keeping a second 334 MB copy here, unlike the one-folder-per-chapter layout described in appendix A.
2. Install `requirements.txt`. Evidently must be 0.4.x (`evidently==0.4.40`), which needs NumPy below 2.1.
3. Open the notebook from inside this folder and run all cells. It takes about 30 seconds, then open the generated `combined_drift_report.html` in a browser.

## Differences from the printed book

- The setup cells at the top aren't in the book. They rebuild the chapter 5 inputs with the same seed, because no chapter 6 listing creates `X`, `y`, `feature_list` or `cat_features`, or imports `plt` (pp. 129 and 135).
- `print(system_report)` on p. 138 prints an extra `None`, because the method prints the report itself and returns nothing.
- Listing 6.9 (p. 141) fails as printed with the pinned versions: `save_html` raises `TypeError: Categorical is not ordered for operation min`, because the data's index is the categorical `customer_ID`. The notebook resets the index in the cell before the listing.
- **Your drift report will cover 111 columns and flag none of them, unlike figures 6.9 and 6.10 ("11 out of 20", pp. 142-144).** The printed report came from an earlier version of this pipeline, kept in [`legacy/`](legacy/), in which most feature columns were still stored as `float16`; only the randomly chosen imputed columns had become `float64`. For a `float16` column, pandas returns a standard deviation of 0, so Evidently's normalized Wasserstein test divides by its 0.001 floor instead and inflates the score by orders of magnitude. Every flagged column was one of those `float16` columns. Cast the same data to `float64` and none of the 20 columns drift. That agrees with the near-zero PSI from listing 6.8, and it is what you should expect from a random train/test split of one population. The way section 6.2.2 reads a drift report still applies.
- In Evidently 0.4.x, 0.5 is the dataset-level threshold: the share of drifted columns. Each numeric column is flagged when its normalized Wasserstein distance reaches 0.1, the default per-column threshold.
- [`legacy/`](legacy/) holds the author's original notebooks for this chapter (moved from the chapter 5 folder) and the `combined_drift_report.html` behind the printed drift figures. They differ from the printed listings in places; use the notebook in this folder to follow the book.

## Further reading

### Regulatory update: US model-risk guidance replaced (April 2026)

Appendix E maps SR 11-7 and OCC Bulletin 2011-12 to chapters 5 and 6. On April 17, 2026, the Federal Reserve, the OCC and the FDIC replaced them with revised interagency guidance on model risk management: [SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) ([guidance text](https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf)) and [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html). The OCC bulletin also rescinds OCC Bulletin 1997-24, *Credit Scoring Models: Examination Guidance*.

Two points matter for this book's systems:

- The new guidance covers traditional statistical and quantitative models and non-generative, non-agentic AI models, such as the scorecards in chapters 4-6. The agencies expect it to be most relevant to banks with more than $30 billion in total assets.
- Generative AI and agentic AI models are explicitly outside its scope (footnote 3 of the guidance). For the LLM systems in chapters 11-14, your own risk-management and governance practices have to fill that gap.

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Navas-Palencia, "Optimal binning: Mathematical programming formulation" (2020)](https://arxiv.org/abs/2001.08025) and the [OptBinning documentation](http://gnpalencia.org/optbinning/): the optimization formulation behind `BinningProcess` in listings 6.1-6.3, plus the library's documentation.
- [Evidently AI (this book uses the 0.4.x API)](https://github.com/evidentlyai/evidently): the drift-monitoring library used in listing 6.9.
- [Ribeiro, Singh & Guestrin, "'Why should I trust you?'" (LIME), KDD 2016](https://arxiv.org/abs/1602.04938): local surrogate explanations.
- [Lundberg & Lee, "A unified approach to interpreting model predictions" (SHAP), NeurIPS 2017](https://arxiv.org/abs/1705.07874): Shapley-value explanations.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final): the US federal catalog of security and privacy controls, useful for access control and audit logging around models.
- [Christoph Molnar, *Interpretable Machine Learning*, 3rd ed. (2025)](https://christophm.github.io/interpretable-ml-book/): a free book on interpretability methods, including LIME and SHAP, and their limits.
- [Barocas, Hardt & Narayanan, *Fairness and Machine Learning* (MIT Press, 2023)](https://fairmlbook.org/): a free book on fairness definitions and the trade-offs between them.

### Drift detection beyond PSI

- Rabanser, Günnemann & Lipton, "Failing loudly: An empirical study of methods for detecting
  dataset shift," NeurIPS 2019. [arXiv:1810.11953](https://arxiv.org/abs/1810.11953) — across the shifts studied, a
  two-sample test on representations from a pretrained classifier worked best; useful when PSI on
  single features says "stable" but the joint distribution has moved.
- [`lendrisk`](https://github.com/datakim/lendrisk) — `population_stability_index` and monotonic `OptimalBinning`
  (see the chapter 4 README) if you want a small, dependency-light alternative to the OptBinning
  workflow in section 6.1.

---

[All chapters](../README.md) · [Chapter 5](../chapter05/README.md) · [Chapter 7](../chapter07/README.md)
