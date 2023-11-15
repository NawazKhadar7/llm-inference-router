# mixed-three

Route three prompts with alternating lengths.

Short and long requests must be accounted for and accepted.

Family: mixed. Size: 3. Deterministic seed: 910503.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case mixed-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 3 |
| accepted | equals 3 |
| blocked | equals 0 |
| limited | equals 0 |
| unavailable | equals 0 |
| accounted | equals true |
| cost_units | min 1 |

Scope: Local mock providers, quotas, and guardrail patterns.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
