# fallback-five

Route five prompts while the economy provider fails.

The next eligible mock provider accepts every request.

Family: fallback. Size: 5. Deterministic seed: 910510.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case fallback-five
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 5 |
| accepted | equals 5 |
| blocked | equals 0 |
| limited | equals 0 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
