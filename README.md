# Análisis de Datos con Python - Libro Profesional

Bienvenido al repositorio oficial del libro **"Análisis de Datos con Python"**. Este repositorio contiene todos los materiales necesarios para seguir el curso: datasets, notebooks de Jupyter con el código de los capítulos y soluciones a los ejercicios prácticos.

![Portada del Libro (Placeholder)](static/images/portada_placeholder.png)

## 📂 Estructura del Repositorio

- **`data/`**: El almacén de datos.
  - `raw/`: Datasets originales "sucios" tal cual se descargan de la fuente (para practicar limpieza).
  - `processed/`: Datasets limpios y listos para análisis (para comprobar tus resultados).
- **`notebooks/`**: Cuadernos de Jupyter organizados por Unidad Temática (UT).
- **`static/`**: Recursos visuales y scripts auxiliares.
- **`docs/`**: Documentación adicional (Diccionario de datos, guías de instalación).

## 🚀 Cómo Empezar

### Opción A: Google Colab (Recomendada para principiantes)
Puedes ejecutar los notebooks directamente en la nube sin instalar nada. Busca el botón "Open in Colab" al inicio de cada notebook.

### Opción B: Entorno Local (Recomendada para profesionales)
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/analisis-datos-python-libro.git
   cd analisis-datos-python-libro
   ```
2. Crea un entorno virtual e instala las dependencias exactas:
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Datasets Incluidos

| Dataset | Descripción | Uso en UTs |
| :--- | :--- | :--- |
| **Titanic** | Pasajeros del famoso naufragio (Clasificación) | UT1, UT3, UT8 |
| **House Prices** | Precios de viviendas en Ames, Iowa (Regresión) | UT5, UT6, UT7, UT8, UT9, UT10 |
| **Air Quality UCI** | Calidad del aire con series temporales | UT2, UT4 |

*Consulta `docs/Diccionario_Datos.md` para el detalle de las variables de House Prices.*

## ⚖️ Licencia

El código de este repositorio se distribuye bajo licencia **MIT**. Los textos y explicaciones pertenecen al libro y están protegidos por derechos de autor.
