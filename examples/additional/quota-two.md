# quota-two

Route two prompts with a one-request quota.

Exactly one prompt is accepted and one is limited.

Family: quota. Size: 2. Deterministic seed: 910507.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-two
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 2 |
| accepted | equals 1 |
| blocked | equals 0 |
| limited | equals 1 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
