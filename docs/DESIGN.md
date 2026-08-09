# Design: Safety Quality Regressions

**Project:** `safety-quality-regressions`  
**Parent system design:** `05-model-monitoring-observability.md / 06`

## 1. What this POC demonstrates

Slice-aware behavioral monitoring that pages on block-rate spikes vs baseline.

## 2. Architecture (POC)

```text
POST /observe {slice, block_rate} → compare baseline → alerts
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Slice baselines | Global averages hide localized harm. | Per-slice `baseline` map. |
| Page vs ticket threshold | Alert fatigue kills response. | `page` when ≥2× baseline. |
| Behavioral signal focus | GPU green ≠ model healthy. | Block-rate observation. |

## 4. Key endpoints

`GET /health`, `POST /observe`, `GET /alerts`

## 5. Tradeoffs / POC limits

No LLM-as-judge sampling pipeline in this stub.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

Narrated with **ElevenLabs Debpro voice** and Debpro still image (via [GitaProject](/Users/deb/Development/GenAI/GitaProject)):

- Video: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Script: [`video/narration.txt`](./video/narration.txt)

