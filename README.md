# Exercice projet

## Prérequis

* Python 3.7+
* Git
* Docker, Docker-Compose

### Créer les fichiers obligatoires pour un projet GitHub

* `.gitignore`
* `LICENSE` (voir https://choosealicense.com/)
* `README.md`

## Installation

### Créer un environment virtuel Python (venv)

- Créer un environnement virtuel
    ```bash
    # Linux
    python -m venv .venv

    # Windows
    py -m venv .venv
    ```
- Activer l'environnement virtuel
    ```bash
    # Linux
    .venv/bin/activate

    # Windows (batch/cmd)
    .venv/Scripts/activate.bat

    # Windows (powershell)
    .venv/Scripts/Activate.ps1
    ```

### Installer les dépendances

```bash
pip install -r requirements.txt
```
