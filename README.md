# Distributed LLM Inference Router & Guardrail Engine

An asynchronous local routing gateway with context-aware provider selection, single-flight caching and admission quotas.

## 1. Overview

A gateway must decide which provider can serve a request while respecting context limits, tenant quotas and cost. This local reference makes those decisions inspectable through deterministic providers, so routing behavior can be tested without paid API calls.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Context-aware routing:** Selects the cheapest eligible provider using an approximate token budget.
- **Tenant admission:** Applies request quotas before provider execution.
- **Cache and request coalescing:** Uses tenant-scoped TTL/LRU caching and single-flight handling to reduce repeated work.
- **Fallback and guardrail checks:** Exercises provider failures and simple pattern checks with synthetic requests.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+, asyncio | Runnable local reference |
| Cache and API | In-memory TTL/LRU cache, standard-library HTTP/JSON | Runnable; no Redis or external LLM required |
| Providers | Deterministic provider implementations | Mocks; real provider integration remains extension work |

### How the components fit together

The workload API invokes the run harness, which submits requests to the asynchronous gateway. Guardrail and quota checks precede tenant-scoped cache lookup; a provider abstraction handles routing, execution and fallback.

| Component | Responsibility |
| --- | --- |
| [src/syslab/core.py](src/syslab/core.py) | Gateway orchestration, provider selection and tenant admission. |
| [src/syslab/cache.py](src/syslab/cache.py) | TTL/LRU cache and coalescing of concurrent equivalent requests. |
| [src/syslab/providers.py](src/syslab/providers.py) | Provider interfaces and deterministic local provider behavior. |
| [src/syslab/guardrail.py](src/syslab/guardrail.py) | Demonstration pattern checks. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Providers are deterministic mocks; no external LLM, Redis or ONNX model is bundled. Pattern matching is a demonstration and cannot reliably detect jailbreaks. Character-based token estimates differ from real tokenizers. Distributed shared quotas, streaming completions, cache size in bytes and credential management remain extension work.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `llm-inference-router` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **20 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "short",
  "id": "short-006-01",
  "seed": 101,
  "size": 6
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/short-006-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accepted": 6,
    "accounted": true,
    "blocked": 0,
    "cost_units": 36,
    "limited": 0,
    "requests": 6,
    "unavailable": 0
  }
}
```

Six short synthetic requests are accepted at a total cost of 36 illustrative units. These units are internal accounting values, not a provider price or real LLM token bill.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=short-006-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Context-aware routing | [src/syslab/core.py](src/syslab/core.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

This project connects AI infrastructure with asynchronous systems, admission control and resource allocation. It can support a systems-focused MS portfolio discussion about the tradeoff between cost, responsiveness and reliability.

**A question to investigate:** How do cache policy, tenant quotas and provider fallback affect measured latency and fairness under different request mixes?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
