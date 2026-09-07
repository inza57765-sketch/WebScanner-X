# 🛡️ WebScanner-X

**WebScanner-X** est un outil CLI développé en Python permettant
d'effectuer des analyses simples de serveurs Web et des résolutions DNS.

> 🚧 Version actuelle : **1.5.0 — Projet en développement**

---

## ✨ Fonctionnalités

WebScanner-X permet actuellement de :

- 🔍 Analyser une URL Web
- 🌐 Afficher certaines informations HTTP
- 🧠 Résoudre un nom de domaine en adresse IP
- 📖 Afficher l'aide directement dans le terminal
- 📄 Afficher le README depuis le terminal
- 🌳 Afficher l'arborescence du projet
- ℹ️ Afficher la version du programme

---

# 📦 Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/inza57765-sketch/WebScanner-X.git
```

Puis entrer dans le projet :

```bash
cd WebScanner-X
```

---

## 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

Les principales dépendances utilisées par WebScanner-X sont :

- `requests`
- `beautifulsoup4`
- `colorama`

---

## 3. Installer WebScanner-X

### Installation classique

```bash
pip install .
```

### Installation en mode éditable

Pour le développement, il est recommandé d'utiliser :

```bash
pip install -e .
```

Le mode éditable permet de modifier le code source sans devoir
réinstaller WebScanner-X après chaque modification.

---

# ⚡ Utilisation

Une fois installé, WebScanner-X peut être lancé directement avec :

```bash
WebScan
```

Il est également possible de lancer le paquet avec Python :

```bash
python -m WebScanner
```

---

# 🧾 Options CLI

## `--help`

Affiche l'aide de WebScanner-X.

```bash
WebScan --help
```

---

## `--version`

Affiche la version actuelle du programme.

```bash
WebScan --version
```

Exemple :

```text
WebScanner-X : v1.5.0
```

---

## `--scan`

Analyse une URL Web.

```bash
WebScan --scan https://python.org
```

L'analyse affiche notamment certaines informations de la réponse HTTP :

- URL
- Status HTTP
- Server
- Content-Type
- Cache-Control
- X-Powered-By
- X-Frame-Options
- X-XSS-Protection
- Content-Security-Policy

Exemple :

```text
https://python.org

Status                  : 200
Server                  : nginx
Content-Type            : text/html; charset=utf-8
```

---

## `--dns`

Résout un nom de domaine en adresse IP.

```bash
WebScan --dns google.com
```

Exemple :

```text
domaine : google.com
IP      : xxx.xxx.xxx.xxx
```

---

## `--readme`

Affiche le README du projet directement dans le terminal.

```bash
WebScan --readme
```

Cette commande peut être utilisée depuis n'importe quel répertoire
après l'installation du paquet.

---

## `--tree`

Affiche l'arborescence du projet.

```bash
WebScan --tree
```

---

# 🐍 Exécution avec Python

WebScanner-X est organisé comme un paquet Python.

Il peut donc être exécuté avec :

```bash
python -m WebScanner
```

Par exemple :

```bash
python -m WebScanner --version
```

ou :

```bash
python -m WebScanner --scan https://python.org
```

Après installation, la commande recommandée pour utiliser l'outil est :

```bash
WebScan
```

---

# 🏗️ Architecture

WebScanner-X utilise une architecture en paquet Python.

Le lancement principal du paquet est effectué par :

```text
__main__.py
```

La gestion des commandes CLI est réalisée par :

```text
commands.py
```

Les imports relatifs permettent aux différents modules du projet
de communiquer correctement entre eux.

---

# 📁 Structure du projet

La structure actuelle du projet est organisée ainsi :

```text
WebScanner-X/
├── README.md
├── __init__.py
├── __main__.py
├── aide.py
├── cmdreadme.py
├── commands.py
├── configs/
│   ├── WebScanner-X.json
│   └── settings.json
├── core/
│   ├── __init__.py
│   ├── Terminal_Visualisation.py
│   ├── banner.py
│   ├── code.py
│   ├── couleurs.py
│   ├── dns_lookup.py
│   ├── headers.py
│   ├── logger.py
│   ├── modules/
│   │   ├── __init__.py
│   │   └── dns_lookup.py
│   └── settings_calc.py
├── docs/
├── help.txt
├── install.sh
├── packages.txt
├── project_lister.py
├── pyproject.toml
├── requirements.txt
├── test/
├── utils/
│   ├── bibs-links/
│   └── dev-links/
└── version.py
```

> ℹ️ La structure du projet peut évoluer au cours du développement.

---

# ⚙️ Configuration

Le fichiers de configuration se trouvent dans :

```text
configs/
```

Notamment :

```text
configs/settings.json
```

---

# 🔧 Développement

Pour récupérer le projet :

```bash
git clone https://github.com/inza57765-sketch/WebScanner-X.git
cd WebScanner-X
```

Installer le projet en mode éditable :

```bash
pip install -e .
```

Les modifications effectuées dans le code source seront alors
directement utilisées par la commande :

```bash
WebScan
```

---

# 🔐 Utilisation responsable

WebScanner-X doit être utilisé uniquement sur des systèmes,
serveurs et sites Web pour lesquels vous disposez d'une autorisation.

Le projet a notamment pour objectif l'apprentissage du développement
Python, du fonctionnement HTTP, du DNS et de la création d'outils CLI.

---

# 📊 État du projet

**WebScanner-X v1.5.0**

🚧 **Développement en cours**

Fonctionnalités actuellement disponibles :

```text
[✓] CLI Python
[✓] Installation avec pip
[✓] Installation éditable
[✓] Commande WebScan
[✓] --help
[✓] --version
[✓] --scan
[✓] --dns
[✓] --readme
[✓] --tree
[✓] Architecture en paquet Python
```

De nouvelles fonctionnalités pourront être ajoutées dans les
prochaines versions.

---

# 👨‍💻 Développeur

**Cyber-Tchak**

GitHub :

https://github.com/inza57765-sketch/WebScanner-X

---

# 📜 Licence

Ce projet est distribué sous licence **MIT**.

---

<p align="center">

🛡️ <strong>WebScanner-X</strong><br>
<em>Explore • Analyze • Learn</em>

</p>
