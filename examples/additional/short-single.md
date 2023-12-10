# short-single

Route one short prompt.

The local mock provider must accept the request.

Family: short. Size: 1. Deterministic seed: 910501.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case short-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| accepted | equals 1 |
| blocked | equals 0 |
| limited | equals 0 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
