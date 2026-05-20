"""Connexion Python → Cassandra (TP séquence 3)."""
from datetime import date, datetime, timezone

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


def main() -> None:
    cluster = Cluster(["127.0.0.1"], port=9042)
    session = cluster.connect("iaware_course")

    insert = SimpleStatement(
        """
        INSERT INTO events_by_device
          (device_id, event_date, event_time, metric, value, payload)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
    )
    session.execute(
        insert,
        (
            "sensor-paris-01",
            date(2026, 5, 20),
            datetime.now(timezone.utc),
            "temperature",
            23.1,
            '{"source":"connect.py"}',
        ),
    )

    rows = session.execute(
        """
        SELECT event_time, metric, value
        FROM events_by_device
        WHERE device_id = %s AND event_date = %s
        LIMIT 5
        """,
        ("sensor-paris-01", date(2026, 5, 20)),
    )
    print("Dernières mesures :")
    for row in rows:
        print(f"  {row.event_time} | {row.metric} = {row.value}")

    cluster.shutdown()


if __name__ == "__main__":
    main()
