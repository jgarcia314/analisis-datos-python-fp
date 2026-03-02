# Guía de Entornos de Trabajo

Esta guía explica todas las opciones disponibles para ejecutar los notebooks del libro
**"Análisis de Datos con Python"**. Elige la que mejor se adapte a tu situación.

---

## Comparativa rápida

| Opción | Instalación | Cuenta necesaria | Recomendada para |
| :--- | :---: | :---: | :--- |
| [Google Colab](#opción-a-google-colab) | Ninguna | Google | Empezar rápido |
| [Binder](#opción-b-binder) | Ninguna | Ninguna | Sin cuenta Google |
| [VS Code + Dev Containers](#opción-c-vs-code--dev-containers) | Docker + VS Code | Ninguna | Alumnos con VS Code |
| [Docker local](#opción-d-docker-local) | Docker | Ninguna | Entorno idéntico al libro |
| [conda local](#opción-e-conda-local) | Anaconda/Miniconda | Ninguna | Windows, uso habitual |
| [pip + venv](#opción-f-pip--venv) | Python 3.10+ | Ninguna | Linux/macOS, uso habitual |

---

## Opción A: Google Colab

**Sin instalación. Requiere cuenta Google.**

Haz clic en el badge de cada notebook en el [README](README.md) o accede directamente
a [colab.research.google.com](https://colab.research.google.com) y abre el notebook
desde GitHub (`jgarcia314/analisis-datos-python-fp`).

> **Nota:** Colab instala las dependencias en cada sesión. La primera celda de cada
> notebook incluye el comando `pip install` necesario.

---

## Opción B: Binder

**Sin instalación. Sin cuenta. Solo navegador.**

Haz clic en el badge del README:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jgarcia314/analisis-datos-python-fp/main)

Binder construye el entorno automáticamente a partir del repositorio. La primera vez
puede tardar 1-2 minutos; las siguientes es inmediato (usa caché).

> **Limitación:** las sesiones se cierran tras 10 minutos de inactividad. Descarga
> el notebook si quieres guardar tu trabajo.

---

## Opción C: VS Code + Dev Containers

**Requiere:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) y
[VS Code](https://code.visualstudio.com/) con la extensión
[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jgarcia314/analisis-datos-python-fp.git
   ```
2. Abre la carpeta en VS Code:
   ```bash
   code analisis-datos-python-fp
   ```
3. VS Code detectará el fichero `.devcontainer/devcontainer.json` y mostrará
   una notificación: **"Reopen in Container"** — haz clic.
4. La primera vez construye la imagen (~2-3 min). Las siguientes es instantáneo.
5. Abre cualquier fichero `.ipynb` desde el explorador y ejecuta las celdas
   directamente en VS Code.

---

## Opción D: Docker local

**Requiere:** [Docker Desktop](https://www.docker.com/products/docker-desktop/)
(Windows/macOS) o Docker Engine (Linux).

```bash
# 1. Clona el repositorio
git clone https://github.com/jgarcia314/analisis-datos-python-fp.git
cd analisis-datos-python-fp

# 2. Construye la imagen (solo la primera vez, ~2-3 min)
docker build -t pyad .

# 3. Arranca JupyterLab
docker run --rm -p 8888:8888 -v $(pwd):/home/jovyan/work pyad
```

4. Abre en el navegador la URL que aparece en el terminal (incluye el token de seguridad):
   ```
   http://127.0.0.1:8888/lab?token=...
   ```

Para parar el servidor: `Ctrl+C` en el terminal.

---

## Opción E: conda local

**Recomendada en Windows.** Requiere
[Miniconda](https://docs.conda.io/en/latest/miniconda.html) o Anaconda.

```bash
# 1. Clona el repositorio
git clone https://github.com/jgarcia314/analisis-datos-python-fp.git
cd analisis-datos-python-fp

# 2. Crea el entorno e instala dependencias
conda env create -f environment.yml

# 3. Activa el entorno
conda activate pyad

# 4. Abre JupyterLab
jupyter lab
```

Para sesiones posteriores, solo necesitas los pasos 3 y 4.

---

## Opción F: pip + venv

**Linux/macOS.** Requiere Python 3.10 o superior.

```bash
# 1. Clona el repositorio
git clone https://github.com/jgarcia314/analisis-datos-python-fp.git
cd analisis-datos-python-fp

# 2. Crea un entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Abre JupyterLab
jupyter lab
```

Para sesiones posteriores, solo necesitas activar el entorno (`source .venv/bin/activate`)
y ejecutar `jupyter lab`.

---

## Verificación del entorno

En cualquier opción, ejecuta el notebook `00_check_entorno.ipynb` para confirmar
que todas las librerías están instaladas correctamente.

---

## ¿Problemas?

Abre un [issue en GitHub](https://github.com/jgarcia314/analisis-datos-python-fp/issues)
describiendo el sistema operativo, la opción elegida y el mensaje de error.
