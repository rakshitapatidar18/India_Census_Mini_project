
# cd "C:\Users\raksh\OneDrive\CampusX\india-data-mini-project"
# streamlit run app.py




import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title("India's Data Visualization📊")

selected_state = st.sidebar.selectbox("Select a state",list_of_states)
primary  = st.sidebar.selectbox("Select Primary parameter",sorted(df.columns[5:]))

secondary  = st.sidebar.selectbox("Select Secondary parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text('Size represent primary parametr')
    st.text('Color represent secondary parametr')
    if selected_state == "Overall India":
        # plotting for India
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",
                            size=primary,color=secondary,map_style="carto-positron",
                            color_continuous_scale="YlGnBu",
                            size_max=30,
                            center={"lat": 20.5937, "lon": 78.9629}, # Centered perfectly on India
                            opacity=1.0,
                            width=1500,
                            height=700,
                            hover_name='District',
                            zoom=3.5)

        st.plotly_chart(fig,use_container_width=True)

    else:
        # plotting for State
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude",
                            size=primary,color=secondary,map_style="carto-positron",
                            color_continuous_scale="YlGnBu",
                            size_max=30,
                            center={"lat": 20.5937, "lon": 78.9629}, # Centered perfectly on India
                            opacity=1.0,
                            width=1500,
                            height=700,
                            hover_name='District',
                            zoom=6)
        
        st.plotly_chart(fig,use_container_width=True)
        