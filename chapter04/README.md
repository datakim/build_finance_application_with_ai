# Chapter 4: Risk and compliance: Credit risk fundamentals

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 2: Building AI for credit risk

Chapter 4 covers credit-risk fundamentals: vintage analysis of cumulative default rates, survival analysis with the Kaplan-Meier estimator, and weight of evidence (WoE) and information value (IV).

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 4.1 | Vintage analysis | 68 | [Chapter_04_Vintage_analysis.ipynb](Chapter_04_Vintage_analysis.ipynb) |
| 4.2 | Survival analysis example | 70 | [Chapter_04_Vintage_analysis.ipynb](Chapter_04_Vintage_analysis.ipynb) |
| 4.3 | Understand WoE and IV with data | 85 | [Chapter_04_WoE_and_IV.ipynb](Chapter_04_WoE_and_IV.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

Run `Chapter_04_Vintage_analysis.ipynb` from inside this folder. Its first code cell writes `vintage_data.csv` if the file is missing. `Chapter_04_WoE_and_IV.ipynb` builds its own data. Only pandas, NumPy, matplotlib and lifelines are used, and no API keys are needed.

## Differences from the printed book

- `vintage_data.csv` is synthetic: 21 monthly vintages (2022-04 to 2023-12) with Month1-Month16 cumulative default rates, generated with seed 42 and cut off at an April 2024 data date. The curves have the same shape as the book's figure but not the same values.
- Listing 4.2's output differs from figure 4.3 (p. 71). With seed 42 the survival curve steps down at months 3, 4, 5, 6 and 10, while the figure steps at months 8, 9 and 10. Both end at 0.88.
- Listing 4.3 prints IV = 0.7582, as on p. 86.
- In the IV rule of thumb on p. 85, the last row should read "> 0.5 → Suspiciously strong".

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [IFRS Foundation, "IFRS 9 Financial Instruments."](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/): the accounting standard that requires expected-credit-loss provisioning.
- [Federal Reserve, SR 20-12, "Interagency policy statement on allowances for credit losses" (2020)](https://www.federalreserve.gov/supervisionreg/srletters/SR2012.htm): the US interagency policy statement on allowances for credit losses under CECL.
- [CFPB, "Regulation B (Equal Credit Opportunity Act)."](https://www.consumerfinance.gov/rules-policy/regulations/1002/): the regulation that implements the Equal Credit Opportunity Act, including adverse-action notices that state specific reasons.
- [Davidson-Pilon, "lifelines: survival analysis in Python," JOSS 4(40):1317 (2019)](https://joss.theoj.org/papers/10.21105/joss.01317): the survival-analysis library used in listing 4.2.
- [Kaplan & Meier, "Nonparametric estimation from incomplete observations," JASA 53(282):457-481 (1958)](https://doi.org/10.1080/01621459.1958.10501452): the original paper behind the Kaplan-Meier survival curve in listing 4.2.
- [Great Expectations (data validation)](https://greatexpectations.io/): an open-source framework for writing data-quality tests.
- Naeem Siddiqi, *Intelligent Credit Scoring*, 2nd ed. (Wiley, 2017): the standard practitioner's guide to developing and implementing scorecards.
- [Thomas, Crook & Edelman, *Credit Scoring and Its Applications*, 2nd ed. (SIAM, 2017)](https://epubs.siam.org/doi/book/10.1137/1.9781611974560): the statistical foundations of credit scoring.

### A runnable companion for binning and WoE: `lendrisk`

[`lendrisk`](https://github.com/datakim/lendrisk) is an open-source toolkit by the author of this book (Apache 2.0, alpha, Python 3.10+).
Its `OptimalBinning` builds constrained, monotonic bins with WoE — the supervised
**coarse classing** step described in section 4.4.2 — without requiring OptBinning at import time.
It also ships `population_stability_index`, `credit_metrics` (AUC, KS, Brier, log loss) and `expected_loss`.

```bash
python -m pip install "git+https://github.com/datakim/lendrisk.git@v0.1.0a2"
```

- Tutorial: [Binning and scorecards](https://github.com/datakim/lendrisk/blob/main/docs/tutorials/scorecards.md) ·
  notebook: [02_native_scorecard.ipynb](https://github.com/datakim/lendrisk/blob/main/notebooks/02_native_scorecard.ipynb)
  ([open in Colab](https://colab.research.google.com/github/datakim/lendrisk/blob/main/notebooks/02_native_scorecard.ipynb))
- Other scorecard libraries worth comparing (listed in lendrisk's design notes):
  [scorecardpy](https://github.com/ShichenXie/scorecardpy),
  [skorecard](https://github.com/ing-bank/skorecard) (ING), and
  [OptBinning](https://github.com/guillermo-navas-palencia/optbinning).

---

[All chapters](../README.md) · [Chapter 3](../chapter03/README.md) · [Chapter 5](../chapter05/README.md)
