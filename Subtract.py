import json
import streamlit as st
import shapely

option = st.selectbox("Substract or add?",("Substract","Add")
Zone1 = st.text_area ("input coordinates that will be substracted from", "")
try:
  Zone1_json = json.loads(Zone1)
  Zone_to_substract_from = shapely.geometry.Polygon(Zone1_json['geometry']['coordinates'][0])
except:
  Zone1_json = "null"
  Zone_to_substract_from = "null"
Zone2 = st.text_area ("input coordinates that will be substracted", "")
try:
  Zone2_json = json.loads(Zone2)
  Zone_to_substract = shapely.geometry.Polygon(Zone2_json['geometry']['coordinates'][0])
except:
  Zone2_json = "null"
  Zone_to_substract = "null"
try:
  if option == "substract":
    result = (Zone_to_substract_from.difference(Zone_to_substract))
  else:
    result = (Zone_to_substract_from.union(Zone_to_substract))                    
  st.code(shapely.to_geojson(result, indent=2), language='json')
except:
  st.write("enter valid geojsons")
