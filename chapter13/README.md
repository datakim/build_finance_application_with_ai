# Chapter 13: Enhancing customer experience: Building a personalization engine

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 5: Building AI for customer and operational excellence

Chapter 13 builds a personalization engine for AlphaStream: it turns each user's holdings and searches into a semantic vector, fuses it with behavioral signals into a "financial DNA" vector, clusters users into segments, and matches users to content by cosine similarity.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 13.1 | A conceptual Airflow DAG for the user mart pipeline | 345 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.2 | Loading the user mart and ETF metadata | 347 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.3 | Creating the semantic vectors | 351 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.4 | Normalizing behavioral scalars | 352 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.5 | Fusing semantics and behavior | 353 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.6 | Uncovering tribes via clustering | 354 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.7 | Visualizing the clusters with t-SNE | 356 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |
| 13.8 | The semantic matching engine | 360 | [Chapter13_personalization.ipynb](Chapter13_personalization.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Fetch the data: `git lfs pull --include="chapter13/*"`.
2. Put `OPENAI_API_KEY` in `.env`. A full run makes roughly 240 embedding calls with `text-embedding-3-small` and needs about 2.5 GB of memory.
3. Run the notebook from inside this folder. Skip the listing 13.1 cell unless you have Airflow with the Spark provider; the DAG is conceptual. Without an API key, only the setup cell, listing 13.2 and the figure 13.3 cell run.

## Data

**Data in this folder:** `alphastream_user_mart_20260115.csv` is the mock user mart for the fictional AlphaStream platform, a teaching abstraction as p. 346 explains. `etf_metadata_mart_20260115.csv` describes the 105 ETFs (category, risk level, volatility, drawdown, volume, tags and a templated description). `user_mart_with_cluster.csv` adds the book's cluster assignment, and chapter 14 uses the same file.

## Differences from the printed book

- The last line of listing 13.1 (p. 346) is indented 6 spaces instead of 4, which is an `IndentationError`. The notebook fixes the indentation.
- Listing 13.6 (p. 354) uses `dna_matrix`, which no listing builds. A cell marked "Not in the book" builds it for all 100,000 users.
- Re-clustering can number the clusters differently from the book (p. 355). The book's assignment is saved in `user_mart_with_cluster.csv`, and an added cell rebuilds the figure 13.3 table from it without API calls.
- Listing 13.8 (p. 360) compares 1,541-dimensional user vectors (1,536 embedding values plus five behavioral features) with 1,536-dimensional content vectors, which raises a dimension error. The notebook compares the user's 1,536-dimensional semantic part, as the listing's own comment suggests.
- The four items in `content_store.pkl` carry stand-in vectors, not real embeddings, so the scores in listing 13.8 won't match the book's example. An optional cell at the end re-embeds them (four API calls) and reruns the recommendations.
- The `financial_dna` column in `user_mart_with_cluster.csv` is a truncated text rendering that contains "...", so it can't be parsed back into vectors. Rebuild the vectors with the notebook.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [van der Maaten & Hinton, "Visualizing data using t-SNE," JMLR 9(86):2579-2605 (2008)](https://jmlr.org/papers/v9/vandermaaten08a.html): the visualization in listing 13.7.
- [Pedregosa et al., "Scikit-learn: Machine learning in Python," JMLR 12:2825-2830 (2011)](https://jmlr.org/papers/v12/pedregosa11a.html): the library behind clustering in listing 13.6 and cosine similarity in listing 13.8.
- [Covington, Adams & Sargin, "Deep neural networks for YouTube recommendations," RecSys 2016](https://doi.org/10.1145/2959100.2959190): two-stage recommendation at scale: candidate generation, then ranking.
- [Martin Zinkevich, "Rules of machine learning."](https://developers.google.com/machine-learning/guides/rules-of-ml): Google's practical rules for shipping machine-learning products.

### The model behind `sentence-transformers`

- Reimers & Gurevych, "Sentence-BERT: Sentence embeddings using Siamese BERT-networks," EMNLP 2019.
  [arXiv:1908.10084](https://arxiv.org/abs/1908.10084) — the method behind the `sentence-transformers` library pinned in
  appendix A, useful if you replace OpenAI embeddings with a local model.

---

[All chapters](../README.md) · [Chapter 12](../chapter12/README.md) · [Chapter 14](../chapter14/README.md)
