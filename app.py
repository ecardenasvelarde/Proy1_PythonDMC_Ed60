import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

st.sidebar.image('DMC.png')
app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python Ed. 60')
  
  st.subheader("_Streamlit_ is :red[cool] :sunglasses:")
  
  st.write("Elaborado por: Erick Cárdenas")
  
  st.markdown(
    '''
    Estudiante: Erick Eduardo Cárdenas Velarde.
    
    Modulo 1: Pyhton Fundamentals.
    
    Información General: Ingeniero Informático con experiencia en automatización de procesos, actualmente trabajando en el Backoffice de un Banco.
    
    Año: 2026.
    
    Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit.
    '''
    )
  st.image('Python_logo.png')
elif app_mode == 'Ejercicio 1':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 2':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 3':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 4':
  st.write("Bienvenido a la " + app_mode)
