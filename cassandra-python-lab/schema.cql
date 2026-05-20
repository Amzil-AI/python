-- Modèle query-first : capteurs IoT / logs applicatifs (cours Python & Cassandra)
CREATE KEYSPACE IF NOT EXISTS iaware_course
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

USE iaware_course;

CREATE TABLE IF NOT EXISTS events_by_device (
  device_id text,
  event_date date,
  event_time timestamp,
  metric text,
  value double,
  payload text,
  PRIMARY KEY ((device_id, event_date), event_time)
) WITH CLUSTERING ORDER BY (event_time DESC);
