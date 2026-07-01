# Harbor Log Report Benchmark Fix

This repository contains my fixes for the Harbor "Log Report" benchmark task.

The objective of the task is to analyze an Apache-style access log and generate a JSON summary containing:

- Total number of requests
- Number of unique client IP addresses
- Most frequently requested path

The benchmark originally contained several issues affecting task correctness, verifier reliability, and reproducibility. These have been addressed and validated.

---

# Repository Structure

```
.
├── environment
│   ├── Dockerfile
│   ├── access.log
│   └── solution_hint.py
├── solution
│   ├── solve.py
│   └── solve.sh
├── tests
│   ├── test_outputs.py
│   └── test.sh
├── instruction.md
└── task.toml
```

---

# Issues Identified

## 1. Task configuration

- Artifact configuration required correction to match Harbor's expected format.

---

## 2. Docker environment

- Base image was updated to a pinned digest to ensure deterministic builds.
- Runtime dependencies remain pinned for reproducibility.

---

## 3. Verifier

The original verifier only confirmed that `report.json` existed and was non-empty.

This allowed incorrect implementations to pass even if the reported values were wrong.

The verifier was updated to validate:

- required JSON keys
- total request count
- unique IP count
- most frequently requested path

---

## 4. Reward generation

The verifier originally wrote the reward to an incorrect location.

The test runner was updated to create `/logs/verifier/reward.txt`, allowing Harbor to collect rewards correctly.

---

## 5. Instructions

The task instructions were rewritten so that every success criterion maps directly to verifier checks.

This removes ambiguity and ensures consistency between the prompt and automated evaluation.

---

# Validation

The task was validated using Harbor's built-in calibration agents.

## Oracle

Expected result

- Reward: 1

Observed result

- Mean: 1.000
- Reward: 1.0

---

## NOP Agent

Expected result

- Reward: 0

Observed result

- Mean: 0.000
- Reward: 0.0

This confirms that:

- correct solutions pass
- incorrect or missing solutions fail

---

# Reproducing the Results

Run:

```bash
harbor run -p . --agent oracle
```

Expected:

```
Reward: 1
Mean: 1.000
```

Run:

```bash
harbor run -p . --agent nop
```

Expected:

```
Reward: 0
Mean: 0.000
```

---

# Summary

The final benchmark now provides:

- deterministic environment configuration
- aligned task instructions
- robust verifier logic
- correct Harbor reward generation
- successful oracle calibration
- successful nop calibration

The task is reproducible and behaves as expected under Harbor evaluation.
