# Cassandra + Python — Lab pédagogique (IAWARE)

Matériel TP pour le cours **Python avancé & Cassandra** — séquence 3.

## Contenu

| Fichier | Rôle |
|---------|------|
| `docker-compose.yml` | Cluster Cassandra local (3 nœuds) |
| `schema.cql` | Keyspace, table, modèle query-first |
| `queries.cql` | INSERT / SELECT / batch CQL |
| `connect.py` | Connexion Python (`cassandra-driver`) |
| `api_fastapi.py` | API REST (CRUD) + démo Ajax/Fetch |
| `static/demo.html` | Page Fetch → API → Cassandra |
| `sample-mcq.md` | Exemples de QCM (3 séquences) |
| `requirements.txt` | Dépendances lab |

## Démarrage rapide

```bash
docker compose up -d
# Attendre ~60s que le cluster soit prêt
docker compose exec cassandra-node1 cqlsh -f /lab/schema.cql
docker compose exec cassandra-node1 cqlsh -f /lab/queries.cql
pip install -r requirements.txt
python connect.py
uvicorn api_fastapi:app --reload
# Ouvrir http://127.0.0.1:8000/demo  ·  Docs : http://127.0.0.1:8000/docs
```

## Objectifs pédagogiques

- Comprendre le modèle **orienté colonnes** (partition key / clustering key)
- Écrire des requêtes **CQL**
- Lancer un **cluster** local et y connecter une app **Python**
- Relier Cassandra à un projet web (REST ou CRUD) en option

© IAWARE · Dhiya Lecheheb · 2026
