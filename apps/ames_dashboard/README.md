# Dashboard Ames Housing

Aplicación interactiva que integra los resultados del análisis completo del dataset Ames Housing desarrollado a lo largo del libro **"Análisis de Datos con Python"** (UT5 → UT6 → UT8 → UT9).

**Demo en vivo:** [analisis-datos-python-fp-ames-dashboard.streamlit.app](https://analisis-datos-python-fp-ames-dashboard.streamlit.app)

## Pestañas

| Pestaña | Contenido |
|---------|-----------|
| Exploración (UT6) | EDA interactivo con filtros por barrio, precio y calidad |
| Modelo (UT8) | Métricas del Random Forest y gráfico real vs predicho |
| Predictor interactivo | Estima el precio de una vivienda con 7 variables |

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run ames_dashboard.py
```

## Datos

El dashboard carga automáticamente `house_prices_ml.csv` desde este repositorio. Este CSV es generado en UT6 a partir del dataset original de Ames Housing con las features derivadas del EDA.
