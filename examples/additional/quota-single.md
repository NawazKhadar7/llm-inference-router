# quota-single

Exercise the minimum one-request quota.

The minimum quota permits the single request.

Family: quota. Size: 1. Deterministic seed: 910506.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-single
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
