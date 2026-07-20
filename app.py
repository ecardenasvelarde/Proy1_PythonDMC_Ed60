import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

st.sidebar.image('DMC.png')
app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])
