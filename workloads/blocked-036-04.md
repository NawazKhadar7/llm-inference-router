# blocked-036-04

Block explicit instruction-override patterns before provider execution.

Input scale: 36; deterministic random seed: 197.
Run `python scripts/demo.py --case workloads/blocked-036-04.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
