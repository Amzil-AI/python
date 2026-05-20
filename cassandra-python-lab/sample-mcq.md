# QCM — échantillons (cours Python & Cassandra)

## QCM-A — POO (Séquence 1)

1. En Python, `__init__` sert principalement à :
   - a) Détruire l'objet  
   - **b) Initialiser l'instance**  
   - c) Déclarer une variable globale  

2. La composition est préférable à l'héritage lorsque :
   - a) On veut réutiliser toute l'API parente  
   - **b) On veut un couplage faible entre comportements**  
   - c) On utilise uniquement des dataclasses  

## QCM-E — Frameworks (Séquence 2)

1. FastAPI est particulièrement adapté pour :
   - **a) APIs REST async avec documentation OpenAPI**  
   - b) Sites CMS avec admin intégré  
   - c) Scripts batch uniquement  

2. En MVC, la couche « Vue » correspond surtout à :
   - a) La base de données  
   - **b) Présentation (HTML/templates ou JSON)**  
   - c) Les règles métier uniquement  

## QCM-G — Cassandra (Séquence 3)

1. La partition key dans Cassandra sert à :
   - **a) Distribuer les données sur le cluster**  
   - b) Chiffrer les colonnes  
   - c) Remplacer une clé primaire SQL auto-incrémentée  

2. Une requête `WHERE` efficace doit en général :
   - a) Filtrer sur n'importe quelle colonne non indexée  
   - **b) Inclure la partition key (et clustering si besoin)**  
   - c) Utiliser `JOIN` entre plusieurs tables  
