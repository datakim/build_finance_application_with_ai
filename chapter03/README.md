# Chapter 3: Working with Generative AI in finance

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 1: Foundations of financial AI

Chapter 3 follows the AlphaStream team building the Alpha Digest with generative AI: choosing and evaluating a model, grounding it with retrieval-augmented generation (RAG), fine-tuning it with LoRA, and moving from hand-written function calling to the Model Context Protocol (MCP).

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 3.1 | A simple, practical litmus test for model evaluation | 39 | [Chapter03_GenAI_in_finance.ipynb](Chapter03_GenAI_in_finance.ipynb) |
| 3.2 | Conceptual snippet for a RAG-powered response | 42 | [Chapter03_GenAI_in_finance.ipynb](Chapter03_GenAI_in_finance.ipynb) |
| 3.3 | Conceptual snippet for fine-tuning with PEFT (LoRA) | 46 | [Chapter03_GenAI_in_finance.ipynb](Chapter03_GenAI_in_finance.ipynb) |
| 3.4 | The "Old Way": Building an agent with manual function calling | 49 | [Chapter03_GenAI_in_finance.ipynb](Chapter03_GenAI_in_finance.ipynb) |
| 3.5 | The "new way": a conceptual agent interacting via MCP | 50 | [Chapter03_GenAI_in_finance.ipynb](Chapter03_GenAI_in_finance.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

- **Listings 3.1 and 3.2** need `OPENAI_API_KEY` in `.env`.
- **Listing 3.3** fine-tunes `meta-llama/Meta-Llama-3-8B`. You need approved access to that gated model on Hugging Face (`hf auth login`), a CUDA GPU with roughly 24 GB of memory or more (the model alone is about 16 GB in float16), and your own `alpha_stream_digests.jsonl`. The book notes there is no public dataset for it; the notebook describes the expected format. The listing stops before `trainer.train()`.
- **Listings 3.4 and 3.5** are pseudocode. Read them; don't run them.

## Differences from the printed book

- Listing 3.4 (p. 49) uses `...` placeholders inside dictionaries, so running it raises a `SyntaxError`. The cell is kept as printed and tagged `raises-exception`.
- Listing 3.5 (pp. 50-51) imports `mcp_client`, a fictional package, as the book points out on p. 51.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [CFA Institute, "A practical guide for LLMs in the financial industry."](https://rpc.cfainstitute.org/research/the-automation-ahead-content-series/practical-guide-for-llms-in-the-financial-industry): an investment-industry introduction to how LLMs work and where they fit in financial workflows.
- [Lewis et al., "Retrieval-Augmented Generation for knowledge-intensive NLP tasks" (2020)](https://arxiv.org/abs/2005.11401): the paper that introduced retrieval-augmented generation, the pattern behind listing 3.2.
- [Hu et al., "LoRA: Low-rank adaptation of large language models" (2021)](https://arxiv.org/abs/2106.09685): low-rank adapters, the parameter-efficient fine-tuning method in listing 3.3.
- [Dettmers et al., "QLoRA: Efficient finetuning of quantized LLMs" (2023)](https://arxiv.org/abs/2305.14314): LoRA on a 4-bit quantized base model, which makes fine-tuning large models feasible on a single GPU.
- [Llama Team, AI @ Meta, "The Llama 3 herd of models" (2024)](https://arxiv.org/abs/2407.21783): the technical report for the Llama 3 models, including the 8B base model that listing 3.3 fine-tunes.
- [Anthropic, "Introducing the Model Context Protocol" (Nov 25, 2024)](https://www.anthropic.com/news/model-context-protocol): Anthropic's introduction of the Model Context Protocol, which listing 3.5 sketches.
- [Chip Huyen, *AI Engineering* (O'Reilly, 2025)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/): building applications on foundation models: evaluation, prompting, RAG, agents and fine-tuning.
- [Sebastian Raschka, *Build a Large Language Model (From Scratch)* (Manning, 2024)](https://www.manning.com/books/build-a-large-language-model-from-scratch): implements a GPT-style model step by step, if you want to see what happens behind the API.

### Beyond the book

- Islam et al., "FinanceBench: A new benchmark for financial question answering" (2023). [arXiv:2311.11944](https://arxiv.org/abs/2311.11944). Questions about public companies, answered from their filings. In the authors' tests, GPT-4-Turbo with a retrieval system answered incorrectly or refused to answer 81% of the sample questions. It is a sobering baseline for the litmus test in listing 3.1 and the RAG pattern in listing 3.2.
- [Model Context Protocol documentation](https://modelcontextprotocol.io/): the current specification and SDKs, if you want to turn the conceptual MCP client in listing 3.5 into working code.

---

[All chapters](../README.md) · [Chapter 2](../chapter02/README.md) · [Chapter 4](../chapter04/README.md)
