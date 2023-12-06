# quota-three

Exercise quota rounding with three prompts.

Floor division admits one prompt and limits two.

Family: quota. Size: 3. Deterministic seed: 910508.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 3 |
| accepted | equals 1 |
| blocked | equals 0 |
| limited | equals 2 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
