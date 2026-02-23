# Guía de Instalación del Entorno

Para seguir este libro, recomendamos dos opciones principales.

## Opción 1: Google Colab (La más fácil)

No necesitas instalar nada en tu ordenador.
1. Ve a [colab.research.google.com](https://colab.research.google.com).
2. Inicia sesión con tu cuenta de Google.
3. Sube los notebooks (`.ipynb`) desde la pestaña "Subir".
4. ¡Listo!

## Opción 2: Instalación Local con Anaconda (Recomendada)

1. Descarga e instala **Anaconda Distribution** desde [anaconda.com](https://www.anaconda.com/download).
2. Abre la terminal (Anaconda Prompt en Windows).
3. Crea un entorno virtual para el libro:
   ```bash
   conda create -n pyad_libro python=3.10
   conda activate pyad_libro
   ```
4. Instala las librerías necesarias:
   ```bash
   pip install -r requirements.txt
   ```
5. Lanza Jupyter Lab:
   ```bash
   jupyter lab
   ```
