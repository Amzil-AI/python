"""REST API FastAPI → Cassandra (pont séquences 2 & 3)."""
from datetime import date, datetime, timezone
from typing import Any
from uuid import uuid4

from cassandra.cluster import Cluster
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(
    title="IAWARE Cassandra Events API",
    description="Lab REST — Python avancé & Cassandra",
    version="1.0.0",
)

_cluster: Cluster | None = None
_session = None


def get_session():
    global _cluster, _session
    if _session is None:
        _cluster = Cluster(["127.0.0.1"], port=9042)
        _session = _cluster.connect("iaware_course")
    return _session


class EventIn(BaseModel):
    device_id: str = Field(..., examples=["sensor-paris-01"])
    event_date: date = Field(..., examples=["2026-05-20"])
    metric: str
    value: float
    payload: str = "{}"


class EventOut(BaseModel):
    event_time: datetime
    metric: str
    value: float
    payload: str | None = None


@app.on_event("shutdown")
def shutdown() -> None:
    global _cluster, _session
    if _cluster:
        _cluster.shutdown()
    _cluster = None
    _session = None


@app.get("/health")
def health() -> dict[str, str]:
    get_session().execute("SELECT now() FROM system.local")
    return {"status": "ok", "database": "cassandra", "keyspace": "iaware_course"}


@app.get("/events/{device_id}/{event_date}", response_model=list[EventOut])
def list_events(device_id: str, event_date: date, limit: int = 20) -> list[EventOut]:
    rows = get_session().execute(
        """
        SELECT event_time, metric, value, payload
        FROM events_by_device
        WHERE device_id = %s AND event_date = %s
        LIMIT %s
        """,
        (device_id, event_date, limit),
    )
    return [
        EventOut(
            event_time=r.event_time,
            metric=r.metric,
            value=r.value,
            payload=r.payload,
        )
        for r in rows
    ]


@app.post("/events", status_code=201)
def create_event(body: EventIn) -> dict[str, Any]:
    event_time = datetime.now(timezone.utc)
    get_session().execute(
        """
        INSERT INTO events_by_device
          (device_id, event_date, event_time, metric, value, payload)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            body.device_id,
            body.event_date,
            event_time,
            body.metric,
            body.value,
            body.payload,
        ),
    )
    return {"id": str(uuid4()), "event_time": event_time.isoformat(), **body.model_dump()}


@app.get("/demo")
def demo_page() -> FileResponse:
    return FileResponse("static/demo.html")


app.mount("/static", StaticFiles(directory="static"), name="static")
