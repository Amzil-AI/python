USE iaware_course;

-- Insertion unitaire
INSERT INTO events_by_device (device_id, event_date, event_time, metric, value, payload)
VALUES ('sensor-paris-01', '2026-05-20', '2026-05-20T10:15:00Z', 'temperature', 22.4, '{"unit":"C"}');

-- Batch (même partition → efficace)
BEGIN BATCH
  INSERT INTO events_by_device (device_id, event_date, event_time, metric, value, payload)
  VALUES ('sensor-paris-01', '2026-05-20', '2026-05-20T10:16:00Z', 'humidity', 61.2, '{"unit":"%"}');
  INSERT INTO events_by_device (device_id, event_date, event_time, metric, value, payload)
  VALUES ('sensor-paris-01', '2026-05-20', '2026-05-20T10:17:00Z', 'pressure', 1013.5, '{"unit":"hPa"}');
APPLY BATCH;

-- Lecture par device + jour (requête primaire du modèle)
SELECT event_time, metric, value, payload
FROM events_by_device
WHERE device_id = 'sensor-paris-01' AND event_date = '2026-05-20'
LIMIT 10;
