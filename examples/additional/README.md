# Additional scenarios for llm-inference-router

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case short-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| short-single | short | 1 | Route one short prompt. |
| long-single | long | 1 | Route one long prompt. |
| mixed-three | mixed | 3 | Route three prompts with alternating lengths. |
| blocked-single | blocked | 1 | Block one guardrail-matching prompt. |
| blocked-seven | blocked | 7 | Block seven guardrail-matching prompts. |
| quota-single | quota | 1 | Exercise the minimum one-request quota. |
| quota-two | quota | 2 | Route two prompts with a one-request quota. |
| quota-three | quota | 3 | Exercise quota rounding with three prompts. |
| quota-seven | quota | 7 | Exercise quota rounding with seven prompts. |
| fallback-five | fallback | 5 | Route five prompts while the economy provider fails. |

Scope: Local mock providers, quotas, and guardrail patterns.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
