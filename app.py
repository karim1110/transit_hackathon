import pandas as pd

plotdf=pd.read_csv('data/plotdf.csv')


plotdf.head()


import streamlit as st
import plotly.express as px
import pandas as pd

# Title
st.title("Density Mapbox Visualization of Delays")

# Dummy data for illustration

# Create the plot
fig = px.density_mapbox(
    plotdf, 
    lat='lat_bin', 
    lon='lon_bin', 
    z='Delay', 
    radius=10,
    center=dict(lat=41, lon=-87),
    zoom=0,
    mapbox_style="open-street-map",
    width=900,
    height=600
)

# Display the plot in Streamlit
st.plotly_chart(fig)


