# Distributed LLM Inference Router & Guardrail Engine

An asynchronous local routing gateway with context-aware provider selection, single-flight caching and admission quotas.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Asyncio provider abstraction, approximate token budgeting, cheapest eligible routing, tenant quotas, in-memory TTL/LRU cache, synthetic provider fallback and a local workload HTTP API.

## Limits and optional runtimes

Providers are deterministic mocks; no external LLM, Redis or ONNX model is bundled. Pattern matching is a demonstration and cannot reliably detect jailbreaks. Character-based token estimates differ from real tokenizers. Distributed shared quotas, streaming completions, cache size in bytes and credential management remain extension work.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
