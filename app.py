import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

st.sidebar.image('DMC.png')
app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.write("Bienvenido a la " & app_mode)
elif app_mode == 'Ejercicio 1':
  st.write("Bienvenido a la " & app_mode)
elif app_mode == 'Ejercicio 2':
  st.write("Bienvenido a la " & app_mode)
elif app_mode == 'Ejercicio 3':
  st.write("Bienvenido a la " & app_mode)
elif app_mode == 'Ejercicio 4':
  st.write("Bienvenido a la " & app_mode)
