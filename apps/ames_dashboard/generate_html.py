"""
Genera ames_dashboard.html — versión estática del dashboard Ames Housing.
Uso: python3 generate_html.py
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ── Datos ──────────────────────────────────────────────────────────────────────
BASE = ("https://raw.githubusercontent.com/jgarcia314/"
        "analisis-datos-python-fp/main/data/raw/")
df = pd.read_csv(BASE + "house_prices_ml.csv")

# ── Modelo ─────────────────────────────────────────────────────────────────────
FEATURES = ['log_GrLivArea', 'OverallQual', 'YearBuilt',
            'log1p_TotalBsmtSF', 'GarageArea', 'BarrioPremium']
X = df[FEATURES].fillna(0)
y = df['SalePrice']
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=100, max_depth=15, n_jobs=-1, random_state=42)
rf.fit(X_tr, y_tr)
y_pred = rf.predict(X_te)

mae  = mean_absolute_error(y_te, y_pred)
rmse = mean_squared_error(y_te, y_pred) ** 0.5
r2   = r2_score(y_te, y_pred)

# ── Gráfico 1: Área vs Precio (EDA) ───────────────────────────────────────────
fig1 = px.scatter(
    df, x='GrLivArea', y='SalePrice', color='OverallQual',
    color_continuous_scale='RdYlGn',
    labels={'GrLivArea': 'Área habitable (sq ft)',
            'SalePrice': 'Precio de venta ($)',
            'OverallQual': 'Calidad'},
    title='Área habitable vs Precio de venta — coloreado por Calidad general',
    opacity=0.7,
    hover_data=['Neighborhood', 'YearBuilt'])

# ── Gráfico 2: Top 10 barrios por precio mediano ───────────────────────────────
mediana_barrio = (df.groupby('Neighborhood')['SalePrice']
                    .median().sort_values(ascending=False).head(10)
                    .reset_index())
fig2 = px.bar(
    mediana_barrio, x='Neighborhood', y='SalePrice',
    title='Top 10 barrios por precio mediano',
    labels={'SalePrice': 'Precio mediano ($)', 'Neighborhood': 'Barrio'},
    color='SalePrice', color_continuous_scale='Blues')

# ── Gráfico 3: Real vs Predicho ────────────────────────────────────────────────
fig3 = px.scatter(
    x=y_te, y=y_pred, opacity=0.5,
    labels={'x': 'Precio real ($)', 'y': 'Precio predicho ($)'},
    title=f'Precio real vs precio predicho — R² = {r2:.3f} | MAE = ${mae:,.0f} | RMSE = ${rmse:,.0f}')
fig3.add_shape(type='line',
    x0=y_te.min(), y0=y_te.min(), x1=y_te.max(), y1=y_te.max(),
    line=dict(color='red', dash='dash', width=2))

# ── Gráfico 4: Feature Importance ─────────────────────────────────────────────
importancias = (pd.Series(rf.feature_importances_, index=FEATURES)
                  .sort_values().reset_index())
importancias.columns = ['Variable', 'Importancia']
fig4 = px.bar(
    importancias, x='Importancia', y='Variable', orientation='h',
    title='Importancia de variables — Random Forest',
    labels={'Importancia': 'Importancia relativa', 'Variable': ''},
    color='Importancia', color_continuous_scale='Teal')
fig4.add_annotation(
    x=importancias['Importancia'].max() * 0.6,
    y=0.3,
    text=f"OverallQual lidera — confirma r = 0,791 del EDA (UT6)",
    showarrow=False,
    font=dict(size=11, color='gray'))

# ── HTML ───────────────────────────────────────────────────────────────────────
TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ames Housing — Del EDA al modelo</title>
  <style>
    body  {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
             max-width: 1200px; margin: 0 auto; padding: 20px; background: #f8f9fa; }}
    h1    {{ color: #1a1a2e; border-bottom: 3px solid #4CAF50; padding-bottom: 8px; }}
    h2    {{ color: #16213e; margin-top: 40px; }}
    .subtitle {{ color: #666; margin-top: -10px; margin-bottom: 30px; }}
    .metrics  {{ display: flex; gap: 20px; margin: 20px 0; }}
    .metric   {{ background: white; border-radius: 8px; padding: 16px 24px;
                 box-shadow: 0 2px 8px rgba(0,0,0,.08); flex: 1; text-align: center; }}
    .metric .label {{ font-size: 13px; color: #888; margin-bottom: 4px; }}
    .metric .value {{ font-size: 24px; font-weight: 700; color: #1a1a2e; }}
    .note     {{ background: #e8f5e9; border-left: 4px solid #4CAF50;
                 padding: 12px 16px; border-radius: 4px; margin: 20px 0;
                 font-size: 14px; color: #2e7d32; }}
    .chart    {{ background: white; border-radius: 8px; padding: 10px;
                 box-shadow: 0 2px 8px rgba(0,0,0,.08); margin-bottom: 24px; }}
    footer    {{ text-align: center; color: #aaa; font-size: 12px;
                 margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; }}
  </style>
</head>
<body>

<h1>Ames Housing — Del EDA al modelo</h1>
<p class="subtitle">Datos de UT5 &middot; Hallazgos de UT6 &middot; Modelo de UT8 &middot; Dashboard de UT9</p>

<div class="note">
  Versi&oacute;n interactiva completa (con predictor) en
  <a href="https://ames-housing-dashboard.streamlit.app" target="_blank">
    ames-housing-dashboard.streamlit.app</a>
</div>

<h2>Exploraci&oacute;n (UT6)</h2>
<div class="chart">{fig1}</div>
<div class="chart">{fig2}</div>

<h2>Modelo Random Forest (UT8)</h2>
<div class="metrics">
  <div class="metric"><div class="label">MAE</div><div class="value">${mae:,.0f}</div></div>
  <div class="metric"><div class="label">RMSE</div><div class="value">${rmse:,.0f}</div></div>
  <div class="metric"><div class="label">R&sup2;</div><div class="value">{r2:.3f}</div></div>
</div>
<div class="chart">{fig3}</div>
<div class="chart">{fig4}</div>

<footer>
  Libro &ldquo;An&aacute;lisis de Datos con Python&rdquo; &mdash;
  <a href="https://github.com/jgarcia314/analisis-datos-python-fp" target="_blank">
    github.com/jgarcia314/analisis-datos-python-fp</a>
</footer>

</body>
</html>"""

html = TEMPLATE.format(
    fig1=fig1.to_html(full_html=False, include_plotlyjs='cdn'),
    fig2=fig2.to_html(full_html=False, include_plotlyjs=False),
    fig3=fig3.to_html(full_html=False, include_plotlyjs=False),
    fig4=fig4.to_html(full_html=False, include_plotlyjs=False),
    mae=mae, rmse=rmse, r2=r2,
)

out = 'apps/ames_dashboard/ames_dashboard.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"OK — {out} ({len(html)//1024} KB)")
