import json
import streamlit as st
import shapely

Tariff_zone = shapely.geometry.Polygon([(0,0),(0,3),(3,3),(3,0)])
Polygon = shapely.geometry.Polygon([(2,2),(2,5),(5,5),(5,2)])

result = (Tariff_zone.difference(Polygon))

st.write(result)
