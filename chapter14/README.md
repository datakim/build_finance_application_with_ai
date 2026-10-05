# Chapter 14: Driving operational efficiency: Building autonomous retention agents

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 5: Building AI for customer and operational excellence

Chapter 14 builds an autonomous retention agent: it scores churn risk, gives an OpenAI tool-calling agent two tools (user context and segment insights), batches recommendations by segment, sends a Slack alert, holds actions in a draft-approve queue, and measures impact with an experiment and an ROI calculation.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 14.1 | Loading data and verifying structure | 371 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.2 | Generating churn scores and filtering high-risk users | 372 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.3 | RetentionTools class: initialization and cluster profiles | 373 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.4 | RetentionTools class: get_user_context method | 374 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.5 | RetentionTools class: get_cluster_insights method | 375 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.6 | Testing the RetentionTools | 376 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.7 | RetentionAgent class: Initialization and tool definitions | 378 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.8 | RetentionAgent: Tool execution | 379 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.9 | RetentionAgent: analyze_user method (system prompt) | 379 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.10 | RetentionAgent: analyze_user method (agent loop) | 380 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.11 | RetentionAgent: Response parsing | 381 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.12 | Single user analysis test | 381 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.13 | Batch analysis function | 382 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.14 | Cluster aggregation function | 383 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.15 | Slack notification function | 384 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.16 | Sending the Slack alert | 385 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.17 | The draft-approve approval queue | 386 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.18 | Experiment analysis function | 389 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.19 | Running the experiment analysis | 390 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |
| 14.20 | ROI calculation | 391 | [Chapter14_retention_agent.ipynb](Chapter14_retention_agent.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Fetch the data: `git lfs pull --include="chapter14/*"`.
2. Put `OPENAI_API_KEY` in `.env`. The agent cells make about 33 `gpt-4o-mini` calls. `SLACK_WEBHOOK_URL` is optional; if it's empty, the Slack post is skipped.
3. Run the notebook from inside this folder, top to bottom. Listings 14.1-14.11, 14.15 and 14.17-14.20 need no API key.

## Differences from the printed book

- Without any API calls, the notebook reproduces figures 14.3, 14.4, 14.5, 14.10 and 14.11: 6,796 high-risk users, the experiment (12.4% / 17.8% / 30.3%, p = 0.0009) and the ROI table.
- The book splits the `RetentionTools` and `RetentionAgent` classes across several listings and prints their `def` lines flush left (pp. 374-381). The notebook puts each class in one cell, with comments marking where each listing starts.
- The note on p. 376 asks you to create the OpenAI client yourself. A cell before listing 14.12 does this with `OpenAI()`, which reads `OPENAI_API_KEY` from your `.env` file.
- Figures 14.4, 14.5, 14.6 and 14.8 show output that the listings don't print. Cells marked "Not in the book" print it.
- Figure 14.7 (p. 383) shows "✓ action", while listing 14.13 prints "Done - action".
- In the approval queue of listing 14.17 (p. 386), `submit()` checks for the status `"parse_failed"`, which `_parse_response` never sets. `review()` reads a `"message"` key that the agent's JSON doesn't contain, so approved items end up with no final message. To make it work, set a failure status in `_parse_response` and build the message from `suggested_content`.
- Listing 14.16 reads the Slack webhook from `SLACK_WEBHOOK_URL` instead of a hard-coded URL.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [OpenAI, "Function calling" (docs)](https://platform.openai.com/docs/guides/function-calling): the tool-calling API the retention agent is built on.
- [Yao et al., "ReAct: Synergizing reasoning and acting in language models" (2022)](https://arxiv.org/abs/2210.03629): interleaving reasoning with tool use, the pattern behind the agent loop in listing 14.10.
- [Slack, "Sending messages using incoming webhooks."](https://api.slack.com/messaging/webhooks): the incoming-webhook API used in listings 14.15 and 14.16.
- [FINRA Regulatory Notice 24-09 (June 2024)](https://www.finra.org/rules-guidance/notices/24-09): FINRA's reminder that its existing rules apply when member firms use generative AI.
- [Anthropic, "Building effective agents" (Dec 19, 2024)](https://www.anthropic.com/research/building-effective-agents): when a simple workflow beats an agent, and patterns for each.
- [Micheal Lanham, *AI Agents in Action* (Manning, 2025)](https://www.manning.com/books/ai-agents-in-action): a book-length treatment of building agents.

### Testing an agent before customers meet it

- Yao et al., "τ-bench: A benchmark for tool-agent-user interaction in real-world domains" (2024).
  [arXiv:2406.12045](https://arxiv.org/abs/2406.12045) — evaluates tool-using agents against simulated users and written
  policies, and introduces pass^k to measure consistency over repeated trials (even strong
  function-calling agents succeeded on fewer than half the tasks). The same idea applies to the retention
  agent: script customer personas, replay them, and check that recommendations stay within policy.

---

[All chapters](../README.md) · [Chapter 13](../chapter13/README.md)
