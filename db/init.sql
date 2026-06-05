-- Script d'initialisation pour la base de données de la COFRAP

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,          -- Mot de passe haché (bcrypt)
    mfa TEXT,                        -- Secret TOTP chiffré (Fernet)
    gendate BIGINT NOT NULL,         -- Unix timestamp de génération
    expired INT DEFAULT 0            -- 0 = Actif, 1 = Expiré
);
