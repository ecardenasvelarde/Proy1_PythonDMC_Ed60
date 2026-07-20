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
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 1 - Flujo de Caja", page_icon="💰")
  
  # --- Descripción del ejercicio ---
  st.markdown("""
  ## Flujo de caja con listas
  Este módulo permite registrar movimientos financieros. 
  Puedes ingresar el **concepto**, el **tipo** (Ingreso/Gasto) y el **valor**. 
  Al finalizar, verás el historial, los totales y el estado actual de tu flujo.
  """)
  
  st.divider()
  
  # --- Inicialización del estado (Session State) ---
  if "historial" not in st.session_state:
      st.session_state.historial = []
  
  # --- Interfaz de entrada de datos ---
  col1, col2, col3 = st.columns([2, 1, 1])
  
  with col1:
      concepto = st.text_input("Concepto", placeholder="Ej: Pago de luz")
  
  with col2:
      tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
  
  with col3:
      valor = st.number_input("Valor", min_value=0.0, step=1.0)
  
  # Botón para agregar
  if st.button("Agregar movimiento"):
      if concepto.strip() == "":
          st.error("Por favor, ingresa un concepto.")
      elif valor <= 0:
          st.error("El valor debe ser mayor a 0.")
      else:
          # Guardar en la lista
          registro = {
              "Concepto": concepto,
              "Tipo": tipo,
              "Valor": valor
          }
          st.session_state.historial.append(registro)
          st.success(f"Registrado: {concepto}")
  
  st.divider()
  
  # --- Cálculos y Resultados ---
  if st.session_state.historial:
      # Convertir a DataFrame para facilitar cálculos
      df = pd.DataFrame(st.session_state.historial)
      
      # Calcular totales
      total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
      total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
      saldo_final = total_ingresos - total_gastos
  
      # Mostrar Tabla
      st.subheader("Lista de movimientos registrados")
      st.dataframe(df, use_container_width=True, hide_index=True)
  
      # Mostrar Métricas
      c1, c2, c3 = st.columns(3)
      c1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
      c2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
      c3.metric("Saldo Final", f"S/{saldo_final:,.2f}")
  
      # Mostrar Estado del flujo
      if saldo_final >= 0:
          st.success(f"### El flujo de caja está **A FAVOR** 📈")
      else:
          st.error(f"### El flujo de caja está **EN CONTRA** 📉")
      
      # Botón para reiniciar
      if st.button("Limpiar todo"):
          st.session_state.historial = []
          st.rerun()
  else:
      st.info("Aún no hay movimientos registrados.")
elif app_mode == 'Ejercicio 2':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 3':
  st.write("Bienvenido a la " + app_mode)
elif app_mode == 'Ejercicio 4':
  st.write("Bienvenido a la " + app_mode)
