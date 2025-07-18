import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de coches usados')  # título de la aplicación

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Evolucion precio promedio segun condición del coche')

    df_agrupado = car_data.groupby('condition').agg(
        {'price': 'mean'}).reset_index()
    fig_2 = px.bar(df_agrupado, x='condition', y='price',
                   title='Precio promedio por condición del coche')

    st.plotly_chart(fig_2, use_container_width=True)  # mostrar el gráfico

if st.checkbox('Mostrar datos'):  # casilla de verificación para mostrar datos
    st.write('Datos del conjunto de datos de coches usados')
    st.dataframe(car_data)  # mostrar el DataFrame

# agregamos graficos de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Gráfico de dispersión')
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Gráfico de dispersión: Precio vs Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)

if st.balloons():  # si se muestran globos
    # mensaje de felicitación
    st.write('Beinvenido!!!!.')
