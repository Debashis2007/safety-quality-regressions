# Use Case: Safety / Quality Regressions

**Author fingerprint:** `DBHATT-Debashis2007-SystemDesignPOC-2026` — Debashis Bhattacharjee ([@Debashis2007](https://github.com/Debashis2007))

**YouTube walkthrough:** [Safety Quality Regressions — System Design #Shorts](https://youtu.be/08CIgZkzlAs)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [05 — Model Monitoring & Behavior Observability](./05-model-monitoring-observability.md)  
**Also references:** [06 — Safety pipeline](./06-safety-moderation-pipeline.md)

## Users & problem

Trust and product teams need early detection when refusal quality, toxicity, or task success degrades—even if GPUs look healthy.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Detect | Minutes for severe; hours for gradual drift |
| Slices | Language, topic, product surface |
| Sampling | Overweight rare/high-risk |
| Action | Page + optional traffic freeze |

## Design (from parent)

```
Serving telemetry + stratified samples
  → online judges / classifiers
  → anomaly on category rates + quality proxies
  → incident ticket + link to sampled traces
```

Reuse behavioral layer and privacy controls from **05**; align categories with **06** reason codes.

## Specializations

| Concern | Regression choice |
|---------|-------------------|
| Judges | Calibrate LLM-as-judge vs humans weekly |
| Thresholds | Absolute high-severity miss ≫ average shift |
| Privacy | Restricted raw text access |
| Tie-in | Same signals as canary gates |

## Failure modes

- Alert fatigue → few page-worthy severities; ticket the rest.
- Judge drift → version judges; shadow compare.
- Missing slice → mandatory slice configs in monitoring templates.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Safety Quality Regressions — System Design #Shorts](https://youtu.be/08CIgZkzlAs)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd safety-quality-regressions
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/observe -H 'Content-Type: application/json' -d '{"slice":"en","block_rate":0.02}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

