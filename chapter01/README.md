# Chapter 1: Introduction to AI in finance

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 1: Foundations of financial AI

Chapter 1 has no code listings. It explains where AI creates value across banking, financial services and insurance (BFSI), introduces the four building blocks used throughout the book (data asset, modeling, strategy and monitoring, and application layers), and lists the tools you need.

## How to run

Set up your environment with appendix A before the hands-on chapters. The [top-level README](../README.md) has the short version.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [OpenAI, "Morgan Stanley uses AI evals to shape the future of financial services."](https://openai.com/index/morgan-stanley/): how Morgan Stanley used evaluations to test GPT-4-based tools before rolling them out to its financial advisors.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj): the EU data-protection regulation. Article 22 restricts decisions based solely on automated processing, such as an automated credit refusal.
- [Federal Reserve, "Comprehensive Capital Analysis and Review (CCAR)."](https://www.federalreserve.gov/supervisionreg/ccar.htm): the Federal Reserve's capital-planning and stress-testing review for large banks, a big reason model documentation and validation are so formal in banking.
- [NIST, "AI Risk Management Framework."](https://www.nist.gov/itl/ai-risk-management-framework): a voluntary framework for managing AI risk, organized around four functions: Govern, Map, Measure and Manage.
- [FINRA, "Artificial intelligence (AI) key topic page."](https://www.finra.org/rules-guidance/key-topics/artificial-intelligence): FINRA's collection of guidance, notices and reports on how broker-dealers use AI.

### Regulatory update: US model-risk guidance replaced (April 2026)

Appendix E maps SR 11-7 and OCC Bulletin 2011-12 to chapters 5 and 6. On April 17, 2026, the Federal Reserve, the OCC and the FDIC replaced them with revised interagency guidance on model risk management: [SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) ([guidance text](https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf)) and [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html). The OCC bulletin also rescinds OCC Bulletin 1997-24, *Credit Scoring Models: Examination Guidance*.

Two points matter for this book's systems:

- The new guidance covers traditional statistical and quantitative models and non-generative, non-agentic AI models, such as the scorecards in chapters 4-6. The agencies expect it to be most relevant to banks with more than $30 billion in total assets.
- Generative AI and agentic AI models are explicitly outside its scope (footnote 3 of the guidance). For the LLM systems in chapters 11-14, your own risk-management and governance practices have to fill that gap.

### More on regulation

- [EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj): Annex III, point 5(b) lists AI systems that evaluate the creditworthiness of individuals or set their credit score as high-risk, and excludes systems used to detect financial fraud. Appendix E covers the timeline.

---

[All chapters](../README.md) · [Chapter 2](../chapter02/README.md)
