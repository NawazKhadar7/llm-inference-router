# quota-seven

Exercise quota rounding with seven prompts.

The quota admits three prompts and limits four.

Family: quota. Size: 7. Deterministic seed: 910509.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 7 |
| accepted | equals 3 |
| blocked | equals 0 |
| limited | equals 4 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
