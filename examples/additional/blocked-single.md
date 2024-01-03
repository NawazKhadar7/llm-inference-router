# blocked-single

Block one guardrail-matching prompt.

The blocked request incurs zero provider cost.

Family: blocked. Size: 1. Deterministic seed: 910504.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case blocked-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| accepted | equals 0 |
| blocked | equals 1 |
| limited | equals 0 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | equals 0 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
