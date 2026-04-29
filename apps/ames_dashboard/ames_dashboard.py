import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE = ("https://raw.githubusercontent.com/jgarcia314/"
        "analisis-datos-python-fp/main/data/raw/")

@st.cache_data
def cargar_datos():
    return pd.read_csv(BASE + "house_prices_ml.csv")

@st.cache_resource
def entrenar_modelo(_df):
    FEATURES = ['log_GrLivArea', 'OverallQual', 'YearBuilt',
                'TotalBsmtSF', 'GarageArea', 'BarrioPremium']
    X = _df[FEATURES].fillna(0)
    y = _df['SalePrice']
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor(n_estimators=100, max_depth=15,
                               n_jobs=-1, random_state=42)
    rf.fit(X_tr, y_tr)
    return rf, X_te, y_te, FEATURES

# ── Configuración ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ames Housing", layout="wide")
st.title("Ames Housing — Del EDA al modelo")
st.caption("Datos de UT5 · Hallazgos de UT6 · Modelo de UT8")

df = cargar_datos()
tab_eda, tab_modelo, tab_predictor = st.tabs(
    ["Exploración (UT6)", "Modelo (UT8)", "Predictor interactivo"])

# ── Pestaña 1: EDA ─────────────────────────────────────────────────────────────
with tab_eda:
    st.subheader("Hallazgos del EDA")

    with st.sidebar:
        st.header("Filtros")
        barrios = st.multiselect(
            "Barrios", sorted(df['Neighborhood'].unique()),
            default=sorted(df['Neighborhood'].unique()))
        rango_precio = st.slider(
            "Rango de precio ($)", int(df['SalePrice'].min()),
            int(df['SalePrice'].max()),
            (int(df['SalePrice'].quantile(0.05)),
             int(df['SalePrice'].quantile(0.95))))
        calidad_min = st.slider("Calidad mínima (OverallQual)", 1, 10, 1)

    filtro = (df['Neighborhood'].isin(barrios) &
              df['SalePrice'].between(*rango_precio) &
              (df['OverallQual'] >= calidad_min))
    df_f = df[filtro]

    col1, col2, col3 = st.columns(3)
    col1.metric("Viviendas", f"{len(df_f):,}")
    col2.metric("Precio mediano", f"${df_f['SalePrice'].median():,.0f}")
    col3.metric("Calidad media", f"{df_f['OverallQual'].mean():.1f} / 10")

    fig_scatter = px.scatter(
        df_f, x='GrLivArea', y='SalePrice', color='OverallQual',
        color_continuous_scale='RdYlGn',
        labels={'GrLivArea': 'Área habitable (sq ft)',
                'SalePrice': 'Precio de venta ($)',
                'OverallQual': 'Calidad'},
        title='Área vs Precio — coloreado por Calidad general',
        opacity=0.7)
    st.plotly_chart(fig_scatter, use_container_width=True)

    mediana_barrio = (df_f.groupby('Neighborhood')['SalePrice']
                        .median().sort_values(ascending=False).head(10)
                        .reset_index())
    fig_box = px.bar(mediana_barrio, x='Neighborhood', y='SalePrice',
                     title='Top 10 barrios por precio mediano',
                     labels={'SalePrice': 'Precio mediano ($)',
                             'Neighborhood': 'Barrio'})
    st.plotly_chart(fig_box, use_container_width=True)

# ── Pestaña 2: Modelo ──────────────────────────────────────────────────────────
with tab_modelo:
    st.subheader("Random Forest — resultados de UT8")

    rf, X_te, y_te, FEATURES = entrenar_modelo(df)
    y_pred = rf.predict(X_te)

    mae  = mean_absolute_error(y_te, y_pred)
    rmse = mean_squared_error(y_te, y_pred) ** 0.5
    r2   = r2_score(y_te, y_pred)

    col1, col2, col3 = st.columns(3)
    col1.metric("MAE", f"${mae:,.0f}")
    col2.metric("RMSE", f"${rmse:,.0f}")
    col3.metric("R²", f"{r2:.3f}")

    fig_pred = px.scatter(
        x=y_te, y=y_pred, opacity=0.5,
        labels={'x': 'Precio real ($)', 'y': 'Precio predicho ($)'},
        title='Precio real vs precio predicho')
    fig_pred.add_shape(type='line',
        x0=y_te.min(), y0=y_te.min(), x1=y_te.max(), y1=y_te.max(),
        line=dict(color='red', dash='dash'))
    st.plotly_chart(fig_pred, use_container_width=True)

    importancias = (pd.Series(rf.feature_importances_, index=FEATURES)
                      .sort_values().tail(8).reset_index())
    importancias.columns = ['Variable', 'Importancia']
    fig_imp = px.bar(importancias, x='Importancia', y='Variable',
                     orientation='h',
                     title='Top 8 variables — confirma hallazgos de UT6')
    st.plotly_chart(fig_imp, use_container_width=True)
    st.caption("OverallQual lidera la importancia — exactamente lo que la "
               "correlación r = 0,791 de UT6 anticipaba.")

# ── Pestaña 3: Predictor interactivo ──────────────────────────────────────────
with tab_predictor:
    st.subheader("Estima el precio de una vivienda")
    st.caption("El modelo aplica las mismas transformaciones log que aprendiste en UT6.")

    col_a, col_b = st.columns(2)
    with col_a:
        area    = st.slider("Área habitable (sq ft)", 500, 4000, 1500)
        calidad = st.slider("Calidad general (1-10)", 1, 10, 5)
        anno    = st.slider("Año de construcción", 1872, 2010, 1990)
        garaje  = st.slider("Área de garaje (sq ft)", 0, 1400, 400)
    with col_b:
        sotano  = st.slider("Área de sótano (sq ft)", 0, 3000, 800)
        barrio_p = st.selectbox("¿Barrio premium?",
                                ["No (barrio estándar)", "Sí (NridgHt, NoRidge, StoneBr)"])

    barrio_premium = 1 if barrio_p.startswith("Sí") else 0

    entrada = pd.DataFrame([{
        'log_GrLivArea': np.log(area),
        'OverallQual':   calidad,
        'YearBuilt':     anno,
        'TotalBsmtSF':   sotano,
        'GarageArea':    garaje,
        'BarrioPremium': barrio_premium,
    }])

    if st.button("Calcular precio estimado", type="primary"):
        precio = rf.predict(entrada)[0]
        st.success(f"Precio estimado: **${precio:,.0f}**")
        st.caption(f"Basado en {len(df):,} viviendas de Ames, Iowa "
                   f"(dataset limpiado en UT5, analizado en UT6, modelado en UT8).")
