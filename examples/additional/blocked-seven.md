# blocked-seven

Block seven guardrail-matching prompts.

All blocked requests avoid provider execution and cost.

Family: blocked. Size: 7. Deterministic seed: 910505.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case blocked-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 7 |
| accepted | equals 0 |
| blocked | equals 7 |
| limited | equals 0 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | equals 0 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
