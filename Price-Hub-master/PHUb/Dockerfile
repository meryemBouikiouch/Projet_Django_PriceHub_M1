# Utilisez une image légère basée sur Alpine
FROM alpine:latest


# Installez SQLite3
RUN apk add --no-cache sqlite


# Copiez votre fichier de base de données SQLite3 dans le conteneur
COPY db.sqlite3 /app/


# Définissez le répertoire de travail dans le conteneur
WORKDIR /app


# Commande par défaut pour démarrer SQLite3
CMD ["sqlite3", "db.sqlite3"]