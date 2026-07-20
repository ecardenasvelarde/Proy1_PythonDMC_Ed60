import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

st.sidebar.image('DMC.png')
app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.subheader("_Streamlit_ is :yellow[cool] :sunglasses:")
  st.image('Python_logo.png')
  st.write("Elaborado por: Erick Cardenas")
  st.markdown(
    '''
    Estudiante: Miguel Angel Limaquispe Huaman
    
    Modulo 1: Pyhton Fundamentals
    
    Información General: Ingeniero de Sistemas con experiencia en Bussines Intelligence en Sectores de Banca, Telecomunicaciones, Consumo Masivo y Farmaceútico.
    
    Año: 34 años
    
    Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit
    '''
    )
elif app_mode == 'Ejercicio 1':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 2':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 3':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 4':
  st.write("Bienvenido a la " + app_mode)
