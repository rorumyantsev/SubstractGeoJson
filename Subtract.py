import json
import streamlit as st
import shapely

Zone1 = st.text_area ("input coordinates that will be substracted from", z1)
Zone1_json = json.loads(Zone1)
Zone_to_substract_from = shapely.geometry.Polygon(Zone1_json['geometry']['coordinates'][0])

Zone2 = st.text_area ("input coordinates that will be substracted", z2)
Zone2_json = json.loads(Zone2)
Zone_to_substract = shapely.geometry.Polygon(Zone2_json['geometry']['coordinates'][0])

result = (Zone_to_substract_from.difference(Zone_to_substract))

st.write(shapely.to_geojson(result, indent=2))
