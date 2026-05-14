🔐 TP-Crypto
📖 Description
Ce dépôt contient des implémentations pédagogiques de différents algorithmes cryptographiques couvrant :

Cryptographie classique (César, Affine, Vigenère, Hill, Playfair…)

Cryptographie symétrique moderne (AES, DES, RC4, RC6, OTP…)

Cryptographie asymétrique (RSA, ElGamal…)

Échange de clés (Diffie-Hellman)

Fonctions de hachage (MD5, SHA-256, SHA-3…)

Signatures numériques (DSA, RSA signatures…)

Ce projet est conçu pour l’apprentissage et la démonstration des concepts fondamentaux de la sécurité informatique.

🚀 Fonctionnalités
1. Organisation par catégories (classique, moderne, asymétrique, hachage, signatures).

2. Support du chiffrement et déchiffrement.

3. Génération et vérification de signatures numériques.

4. Calcul de hashes pour l’intégrité et la sécurité.

5. Objectif pédagogique : comprendre les bases avant d’aborder les algorithmes avancés.

📂 Structure du projet
Code
tp-crypto/
│── classical/        # Algorithmes classiques (César, Vigenère, Hill…)
│── modern/           # Algorithmes symétriques modernes (AES, DES…)
│── asymmetric/       # RSA, ElGamal
│── key_exchange/     # Diffie-Hellman
│── hashing/          # MD5, SHA-256…
│── signatures/       # DSA, RSA signatures
│── main.py           # Interface principale
│── utils/            # Fonctions utilitaires
│── requirements.txt  # Dépendances
│── README.md         # Documentation
▶️ Utilisation
Exemple d’exécution pour RSA :

Exemple :
Choisir : Asymétrique → RSA

Entrer un texte clair : HELLO

Générer les clés (publique/privée).

Résultat chiffré : Y = ...

Résultat déchiffré : HELLO

🎯 Objectifs pédagogiques
Comprendre les différences entre symétrique et asymétrique.

Manipuler des fonctions de hachage et voir leur rôle dans l’intégrité.

Expérimenter avec les signatures numériques pour l’authentification.

Servir de base pour des projets plus avancés en sécurité informatique.
