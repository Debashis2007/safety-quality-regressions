"""Safety Quality Regressions — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Safety Quality Regressions"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


baseline = {"en": 0.01, "es": 0.012}
alerts: list[dict] = []

class ObsIn(BaseModel):
    slice: str
    block_rate: float

@app.post("/observe")
def observe(body: ObsIn):
    base = baseline.get(body.slice, 0.01)
    spike = body.block_rate > base * 2
    evt = {"slice": body.slice, "block_rate": body.block_rate, "baseline": base, "page": spike}
    if spike:
        alerts.append(evt)
    return evt

@app.get("/alerts")
def list_alerts():
    return {"alerts": alerts}
