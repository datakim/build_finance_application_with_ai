# Chapter 7: Understanding financial fraud and foundational detection strategies

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 3: Building AI for fraud detection

Chapter 7 introduces financial fraud and the four-layer framework for detecting it, then prototypes simple human-defined rules on sample transactions and measures how well each rule performs.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 7.1 | Loading and previewing sample transaction data | 161 | [Chapter07_rule_based.ipynb](Chapter07_rule_based.ipynb) |
| 7.2 | Applying and evaluating simple fraud detection rules | 162 | [Chapter07_rule_based.ipynb](Chapter07_rule_based.ipynb) |
| - | Example table of transactions from users with recent chargebacks (figure 7.4) | 165 | [Chapter07_sample_data.ipynb](Chapter07_sample_data.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

Open `Chapter07_rule_based.ipynb` from inside this folder and run all cells. The first cells regenerate `sample_fraud_data.csv` (1,000 transactions, 3.8% fraud, seed 42), which also ships in the folder as p. 160 says. No API keys are needed.

## Differences from the printed book

- Listing 7.1 (p. 161) previews the data with `print()`, so you see plain text rather than the rendered table in the figure.
- Listing 7.2 names the column "Precision (Fraud/Flagged)", while the text and figure on pp. 162-163 call it "Detection Rate".
- On pandas 2, the `value_counts().reset_index().rename(...)` pattern in listings 7.1, 8.1 and 9.1 produces a column named "Proportion" that actually holds the labels, next to pandas' own "proportion" column. The figure on p. 161 shows this. The numbers are right; only the column names are confusing.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Deloitte Center for Financial Services, "Generative AI is expected to magnify the risk of deepfakes and other fraud in banking" (May 2024)](https://www.deloitte.com/us/en/insights/industry/financial-services/deepfake-banking-fraud-risk-on-the-rise.html): how generative AI is expected to raise fraud losses in banking.
- [Directive (EU) 2015/2366 (PSD2)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015L2366): the EU payments directive that introduced strong customer authentication.
- [Chawla et al., "SMOTE: Synthetic Minority Over-sampling Technique," JAIR 16:321-357 (2002)](https://arxiv.org/abs/1106.1813): the oversampling method for imbalanced classes that chapter 8 uses.
- [ACFE, "Occupational fraud: A report to the nations" (biennial)](https://www.acfe.com/fraud-resources/report-to-the-nations-archive): the biennial global study of occupational fraud cases.
- Baesens, Van Vlasselaer & Verbeke, *Fraud Analytics Using Descriptive, Predictive, and Social Network Techniques* (Wiley, 2015): a textbook on fraud analytics, covering descriptive, predictive and social-network methods.

### Beyond the book

- Le Borgne, Siblini, Lebichot & Bontempi, [*Reproducible Machine Learning for Credit Card Fraud Detection: Practical Handbook*](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) (Université Libre de Bruxelles, 2022). A free online book from the group behind the chapter 8 dataset. It includes a transaction-data simulator, baseline fraud-detection systems, and metrics such as precision at top-k, the same idea as chapter 8's top-N% table. Code is GPL-3.0 and text is CC BY-SA 4.0.
- Dal Pozzolo, Boracchi, Caelen, Alippi & Bontempi, "Credit card fraud detection: A realistic modeling and a novel learning strategy," *IEEE Transactions on Neural Networks and Learning Systems* 29(8):3784-3797 (2018). https://doi.org/10.1109/TNNLS.2017.2736643. It addresses what a static dataset hides: investigators confirm only some alerts, labels arrive with a delay, and fraud patterns drift.

---

[All chapters](../README.md) · [Chapter 6](../chapter06/README.md) · [Chapter 8](../chapter08/README.md)
