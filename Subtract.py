import json
import streamlit as st
import shapely

Zone1 = st.text_area ("input coordinates that will be substracted from", "")
try:
  Zone1_json = json.loads(Zone1)
  Zone_to_substract_from = shapely.geometry.Polygon(Zone1_json['geometry']['coordinates'][0])
except Exception as Error:
  st.write("1st zone")
  st.write(Error)
  Zone1_json = "null"
  Zone_to_substract_from = "null"
Zone2 = st.text_area ("input coordinates that will be substracted", "")
try:
  Zone2_json = json.loads(Zone2)
  Zone_to_substract = shapely.geometry.Polygon(Zone2_json['geometry']['coordinates'][0])
except Exception as Error:
  st.write("2nd zone")
  st.write(Error)
  Zone2_json = "null"
  Zone_to_substract = "null"
try:
  result = (Zone_to_substract_from.difference(Zone_to_substract))
  st.write(shapely.to_geojson(result, indent=2))
except:
  st.write("enter valid geojsons")
