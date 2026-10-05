# Chapter 10: Building the quantitative engine: Market direction prediction with machine learning

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 4: Building AI for investment strategies

Chapter 10 builds the quantitative engine: it downloads ETF prices, engineers technical and cross-asset features, labels three-class market direction, and trains a random forest with embargoed time-series cross-validation so that overlapping windows don't leak the future into the past.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 10.1 | Downloading ETF data with yfinance | 266 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.2 | Essential data quality validation | 267 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.3 | Creating realistic target labels | 271 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.4 | Basic technical features for all ETF assets | 273 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.5 | Advanced cross-asset relationship features | 274 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.6 | Understanding our multiclass prediction problem | 279 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.7 | Basic time-series splitting | 280 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.8 | Creating embargoed time-series splits | 281 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.9 | Final model training with conservative parameters | 282 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |
| 10.10 | Trading-focused evaluation | 284 | [Chapter10_quant_engine.ipynb](Chapter10_quant_engine.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Install the TA-Lib C library first (`brew install ta-lib` on macOS, or your distribution's TA-Lib development package on Linux), then `pip install TA-Lib`.
2. Run the notebook from inside this folder. Prices come from Yahoo Finance through `yfinance`, so you need internet access but no API key.

## Differences from the printed book

- The download window ends on the day you run the notebook, so your numbers will differ from the book's.
- Listing 10.10 (p. 284) calls `balanced_accuracy_score` but imports only `classification_report`, which raises `NameError`. The notebook imports both.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Guo et al., "Quant 4.0" (2023)](https://arxiv.org/abs/2301.04020): a view of where quant investing is heading: automated, explainable and knowledge-driven.
- [Federated Hermes, "A history of quant" (June 2025)](https://www.hermes-investment.com/us/en/professional/insights/macro/a-history-of-quant/): a short history of quantitative investing.
- [Gorton & Rouwenhorst, "Facts and fantasies about commodity futures," FAJ 62(2):47-68 (2006)](https://www.nber.org/papers/w10595): the long-run return properties of commodity futures.
- [Asness, Moskowitz & Pedersen, "Value and momentum everywhere," J. Finance 68(3):929-985 (2013)](https://doi.org/10.1111/jofi.12021): value and momentum premia across asset classes.
- Marcos Lopez de Prado, *Advances in Financial Machine Learning* (Wiley, 2018) - source of purged/embargoed CV: the source of purged and embargoed cross-validation.
- [Kayit & Ismail, "Advancing stock price prediction through the development of hybrid ensembles," J. Big Data 12 (2025)](https://doi.org/10.1186/s40537-025-01185-8): hybrid ensembles for stock-price prediction.
- [Marcos Lopez de Prado, *Machine Learning for Asset Managers* (CUP, 2020)](https://doi.org/10.1017/9781108883658): a shorter companion to the previous book, on denoising, clustering and feature importance.
- [Hudson & Thames, mlfinlab](https://github.com/hudson-and-thames/mlfinlab): Python implementations of many techniques from Lopez de Prado's books.

### Transformers and foundation models for time series (not covered in the book)

The chapter's engine is a random forest on engineered features. Here is the map of what
transformer and foundation-model approaches offer — and what the evidence says for markets.

**Architectures** (trained on your own data):

- Zhou et al., "Informer," AAAI 2021. [arXiv:2012.07436](https://arxiv.org/abs/2012.07436)
- Wu et al., "Autoformer," NeurIPS 2021. [arXiv:2106.13008](https://arxiv.org/abs/2106.13008)
- Nie et al., "A time series is worth 64 words: Long-term forecasting with transformers" (PatchTST),
  ICLR 2023. [arXiv:2211.14730](https://arxiv.org/abs/2211.14730)
- Wu et al., "TimesNet," ICLR 2023. [arXiv:2210.02186](https://arxiv.org/abs/2210.02186)
- Liu et al., "iTransformer," ICLR 2024. [arXiv:2310.06625](https://arxiv.org/abs/2310.06625)

**Read alongside them** — Zeng et al., "Are transformers effective for time series forecasting?"
AAAI 2023 (37(9):11121–11128). [arXiv:2205.13504](https://arxiv.org/abs/2205.13504) — a one-layer linear model beat
many transformer forecasters on standard benchmarks.

**Pretrained foundation models** (zero-shot or fine-tuned):

- Das et al., "A decoder-only foundation model for time-series forecasting" (TimesFM), ICML 2024.
  [arXiv:2310.10688](https://arxiv.org/abs/2310.10688)
- Ansari et al., "Chronos: Learning the language of time series," TMLR 2024.
  [arXiv:2403.07815](https://arxiv.org/abs/2403.07815)
- Woo et al., "Unified training of universal time series forecasting transformers" (Moirai),
  ICML 2024 (PMLR 235). [arXiv:2402.02592](https://arxiv.org/abs/2402.02592)
- Goswami et al., "MOMENT," ICML 2024. [arXiv:2402.03885](https://arxiv.org/abs/2402.03885)
- Rasul et al., "Lag-Llama" (2023). [arXiv:2310.08278](https://arxiv.org/abs/2310.08278)
- Garza & Mergenthaler-Canseco, "TimeGPT-1" (2023). [arXiv:2310.03589](https://arxiv.org/abs/2310.03589)
- Benchmark: Aksu et al., "GIFT-Eval" (2024). [arXiv:2410.10393](https://arxiv.org/abs/2410.10393)

**LLMs repurposed for time series** — Jin et al., "Time-LLM," ICLR 2024.
[arXiv:2310.01728](https://arxiv.org/abs/2310.01728); and the counterpoint, Tan et al., "Are language models actually
useful for time series forecasting?" NeurIPS 2024 (spotlight). [arXiv:2406.16964](https://arxiv.org/abs/2406.16964) —
removing the LLM component from three popular methods did not hurt accuracy, and often helped.

**What the evidence says for financial returns:**

- Rahimikia, Ni & Wang, "Re(Visiting) time series foundation models in finance" (2025).
  [arXiv:2511.18578](https://arxiv.org/abs/2511.18578) — on daily excess returns across global markets, off-the-shelf
  models performed poorly zero-shot and fine-tuned; models pretrained from scratch on financial data
  did much better.
- Noguer i Alonso & Franklin, "Pretrained time-series foundation models for financial return
  forecasting" (2026). [arXiv:2606.27100](https://arxiv.org/abs/2606.27100) — foundation models won most rankings on
  five U.S. stocks, but gains over a random walk were small and statistically significant in only
  2 of 10 tasks.

Two practical cautions if you try them on this chapter's ETF data:

1. **Leakage through pretraining.** Check whether your assets and test period could be inside the
   model's pretraining corpus. Chronos's authors report that its advantage over other methods is
   much larger on datasets that were part of its training corpus than on new ones — in a backtest,
   that kind of gap is what look-ahead bias looks like.
2. **Keep the embargo.** Zero-shot does not remove the overlap problem of section 10.5: rolling
   context windows still overlap your labels, so evaluate with the same embargoed splits.

---

[All chapters](../README.md) · [Chapter 9](../chapter09/README.md) · [Chapter 11](../chapter11/README.md)
