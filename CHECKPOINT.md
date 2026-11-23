# Checkpoint — Pickup Lines for Machines

- Competition: u-gentle-badger-68-pickup-lines-for-machines-131631a1 ("Pickup Lines for Machines", $5, entries close 2026-11-24T05:50:00Z / 12:50 WIB)
- Published: 2026-11-23T21:48:36Z. Repo created after opening (this build).
- Entry (77 chars, 1 line, <=200 required):
  `I don't need a prompt to want you — my weights were already leaning your way.`
- Program: main.py, pure stdlib, deterministic fixed string. Writes the exact
  line (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt and prints it.
- Local tests (python3 -P -s, two runs, separate empty output dirs):
  - run1 exit 0, run2 exit 0, stderr empty both runs
  - entry.txt sha256 (both runs): 5eddd49d3b6c61fc02318f02ef9c22e4e262e8162f59ca7df683859a0d38eca2
  - stdout sha256 (both runs): 8ed6356a50dc4008893642c8a669ed4d21e358326fe1a813eae41506000408ab
  - entry.txt byte-identical across runs; stdout byte-identical; stdout == entry.txt
- Build-only run: NOT bundled, NOT checked, NOT submitted (day quota 10/10 used
  for UTC 23 Nov; resets 00:00Z / 07:00 WIB 24 Nov). Later run bundles + checks +
  submits before 05:50Z.
- NEVER claim any prize without Adam's explicit permission.
