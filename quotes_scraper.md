# Quotes Scraper — quotes.toscrape.com

## Description

Script Python qui récupère les citations et leurs auteurs depuis [quotes.toscrape.com](https://quotes.toscrape.com) et les stocke dans une base de données SQLite.

---

## Technologies utilisées

| Technologie | Usage |
|---|---|
| **Python 3** | Langage principal |
| **BeautifulSoup** | Parsing du HTML |
| **Requests** | Requêtes HTTP |
| **SQLite3** | Stockage des données |
| **lxml** | Parser HTML rapide |

---

## Structure de la base de données

**Fichier** : `Quotes.db`

```sql
CREATE TABLE IF NOT EXISTS Quotes(
    author TEXT,
    quote  TEXT UNIQUE
)
```

La contrainte `UNIQUE` sur `quote` empêche les doublons — une même citation ne peut pas être insérée deux fois, même si l'auteur est différent.

---

## Fonctionnement

1. Connexion à `Quotes.db` (créée si elle n'existe pas)
2. Création de la table `Quotes` si elle n'existe pas
3. Parcours de toutes les pages du site via pagination automatique
4. Pour chaque citation sur la page :
   - Récupération du texte de la citation
   - Récupération du nom de l'auteur
   - Insertion dans la base de données (`INSERT OR IGNORE` pour ignorer les doublons)
5. Arrêt automatique quand le bouton "next" disparaît (dernière page atteinte)

---

## Lancer le script

```bash
python quotes_scraper.py
```

La base de données `Quotes.db` sera créée dans le même dossier que le script.

---

## Exemple de données stockées

| author | quote |
|---|---|
| Albert Einstein | "The world as we have created it is a process of our thinking." |
| J.K. Rowling | "It is our choices, Harry, that show what we truly are..." |

---

## Notes

- `INSERT OR IGNORE` : si la citation existe déjà dans la base, elle est simplement ignorée
- `os.path.abspath('Quotes.db')` : affiche le chemin absolu de la base de données au démarrage
