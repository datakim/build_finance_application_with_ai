# Chapter 9: Unveiling hidden connections: Graph-based analytics for advanced fraud detection

*Financial AI in Practice: A Playbook for Credit, Fraud, and Investment Systems* · Part 3: Building AI for fraud detection

Chapter 9 turns transactions into a graph of users, IP addresses, devices, phone numbers and cards, finds fraud rings with Louvain community detection, and trains a simple graph neural network (GNN) on transaction connections.

## Listings

| Listing | Title | Page | Where in this folder |
|---|---|---|---|
| 9.1 | Loading and initial overview of the transaction data | 227 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.2 | Building the graph from transaction data with parallel edge preparation | 228 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.3 | Applying Louvain community detection | 230 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.4 | Preparing for detailed community analysis | 231 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.5 | Parallel analysis of communities and displaying top results | 232 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.6 | Visualizing a selected community subgraph with different node markers | 235 | [Chapter09_FDS_graph.ipynb](Chapter09_FDS_graph.ipynb) |
| 9.1 | Loading and initial overview of the transaction data | 227 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |
| 9.7 | Defining the GNN model | 241 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |
| 9.8 | Function to create graph data (create_fast_graph) | 242 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |
| 9.9 | Defining the orchestration function (1/3): Data prep and model setup | 243 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |
| 9.10 | Defining the orchestration function (2/3): Model training logic | 244 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |
| 9.11 | Defining the orchestration function (3/3): Results analysis, return, and execution | 245 | [Chapter09_FDS_graph_GNN.ipynb](Chapter09_FDS_graph_GNN.ipynb) |

Page numbers refer to the print edition. Cells that aren't in the book are marked as such in each notebook.

## How to run

1. Fetch the data: `git lfs pull --include="chapter09/*"`.
2. **Graph analytics:** run `Chapter09_FDS_graph.ipynb` from inside this folder. It takes a few seconds. Community detection comes from `python-louvain`, imported as `community`; don't install the unrelated PyPI package named `community`.
3. **GNN:** `Chapter09_FDS_graph_GNN.ipynb` needs PyTorch (CPU is fine) and about 3 GB of free memory for the dense adjacency matrix. PyTorch Geometric isn't used.

## Differences from the printed book

- With the pinned versions, the graph notebook reproduces pp. 229-234: 14,906 nodes, 30,567 edges and 2,913 communities, the largest being community 161 with 128 nodes.
- Listing 9.6 (p. 236) prints `print("Graph, partition, ...")` at column 0 under `else:`, which is an `IndentationError`. The notebook indents it.
- Figure 9.5 (p. 237) was made with earlier draft code. Listing 9.6 produces the title "(Nodes by Shape/Color)" and capitalized legend labels.
- In listing 9.8, the hour-of-day feature is always 0 because `transaction_time` in this dataset holds dates only.
- The imports cell isn't printed in the book (p. 226 points to this folder for it). It also imports `display`, which listings 9.1 and 9.5 call.

## Further reading

### References cited in this chapter

From appendix F, with a note on why each is worth your time.

- [Hagberg, Schult & Swart, "Exploring network structure, dynamics, and function using NetworkX," SciPy 2008](https://networkx.org/): the graph library used in listings 9.2-9.6.
- [Blondel et al., "Fast unfolding of communities in large networks" (Louvain), J. Stat. Mech. P10008 (2008)](https://arxiv.org/abs/0803.0476): the community-detection algorithm in listing 9.3.
- [Kipf & Welling, "Semi-supervised classification with graph convolutional networks" (2016)](https://arxiv.org/abs/1609.02907): graph convolutional networks. Listing 9.7 uses the same idea of mixing in neighbors' features, in a simplified form.
- [Hamilton, Ying & Leskovec, "Inductive representation learning on large graphs" (GraphSAGE), NeurIPS 2017](https://arxiv.org/abs/1706.02216): inductive node embeddings that scale to large, growing graphs.
- [Cheng et al., "Graph neural networks for financial fraud detection: A review" (2024)](https://arxiv.org/abs/2411.05815): a review of graph neural networks for financial fraud detection.
- [Fey & Lenssen, "Fast graph representation learning with PyTorch Geometric" (2019)](https://arxiv.org/abs/1903.02428): the standard library for building graph neural networks in PyTorch.
- [William L. Hamilton, *Graph Representation Learning* (2020)](https://www.cs.mcgill.ca/~wlh/grl_book/): a free book on graph representation learning.
- [Traag, Waltman & van Eck, "From Louvain to Leiden," Scientific Reports 9:5233 (2019)](https://arxiv.org/abs/1810.08473): fixes Louvain's tendency to produce badly connected communities.

### Beyond static graphs

- **Temporal graphs** — Rossi et al., "Temporal graph networks for deep learning on dynamic graphs"
  (2020). [arXiv:2006.10637](https://arxiv.org/abs/2006.10637) — transactions are timestamped edges; the chapter's
  static snapshot discards their order, which is often where mule and ring behaviour shows.
- **Graph transformers** — Ying et al., "Do transformers really perform bad for graph
  representation?" (Graphormer), NeurIPS 2021. [arXiv:2106.05234](https://arxiv.org/abs/2106.05234).

Public datasets for practising financial graph models:

- Weber et al., "Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks
  for financial forensics," KDD 2019 Workshop on Anomaly Detection in Finance.
  [arXiv:1908.02591](https://arxiv.org/abs/1908.02591) — introduces the Elliptic dataset (200K+ labelled Bitcoin
  transactions). Worth knowing: in the paper's own results, a random forest beat the GCN.
- Altman et al., "Realistic synthetic financial transactions for anti-money laundering models"
  (2023). [arXiv:2306.16424](https://arxiv.org/abs/2306.16424) — IBM's synthetic AML transactions with ground-truth
  laundering labels, which real data rarely has.

---

[All chapters](../README.md) · [Chapter 8](../chapter08/README.md) · [Chapter 10](../chapter10/README.md)
