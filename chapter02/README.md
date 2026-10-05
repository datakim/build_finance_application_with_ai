# Chapter 2: From model to money: A strategist's guide to real-world financial AI

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 1: Foundations of financial AI

Chapter 2 is about tying a financial AI project to business value, using AlphaStream's *Alpha Digest* as the running example. The two listings are short conceptual snippets that call the OpenAI API.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 2.1 | Conceptual snippet for Alpha Digest summarization | 23 | [Chapter02_alpha_digest.ipynb](Chapter02_alpha_digest.ipynb) |
| 2.2 | Conceptual snippet for an internal moderation tool | 25 | [Chapter02_alpha_digest.ipynb](Chapter02_alpha_digest.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Put `OPENAI_API_KEY` in the repository's `.env` file (copy `.env.example`).
2. Open `Chapter02_alpha_digest.ipynb` from inside this folder and run the setup cell, then listings 2.1 and 2.2. Each listing makes one billed `gpt-4o-mini` call.

## Differences from the printed book

- The first code cell isn't in the book. It loads your key from `.env`, as described in appendix A.4.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [IBM Newsroom, "IBM study: CEOs double down on AI while navigating enterprise hurdles" (May 6, 2025)](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles): IBM's 2025 survey of CEOs on AI investment and the obstacles to getting returns at enterprise scale.
- [Zest AI, resources on AI-automated underwriting](https://www.zest.ai/): a vendor of machine-learning underwriting for lenders, useful as a concrete version of the automated-underwriting business case.
- [New York State DFS, "Report on Apple Card investigation" (March 2021)](https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation): the regulator's investigation into alleged gender bias in Apple Card credit limits. It found no unlawful discrimination but criticized how little customers were told.
- [Agrawal, Gans & Goldfarb, *Prediction Machines*, updated ed. (HBR Press, 2022)](https://www.predictionmachines.ai/): the economics of AI: when prediction gets cheaper, more decisions become worth automating.
- [McKinsey & Company, "The state of AI" (annual survey)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai): an annual survey of where companies adopt AI and where they report value from it.

### Beyond the book

- Sculley et al., ["Hidden technical debt in machine learning systems"](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), NeurIPS 2015: the maintenance costs of ML systems that a business case tends to leave out, from data dependencies to feedback loops. Read it before you promise an ROI number.

---

[All chapters](../README.md) · [Chapter 1](../chapter01/README.md) · [Chapter 3](../chapter03/README.md)
