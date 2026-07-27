import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp
import libreria_clases_proyecto1 as srv

st.sidebar.image('DMC.png')

app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  # --- Título ---
  st.title ('Proyecto N°1 de la Especialización de Python Ed. 60')
  # --- Sub título ---
  st.subheader("_Streamlit_ is :red[cool] :sunglasses:")
  # --- Cuerpo ---
  st.markdown(
    '''
    Estudiante: Erick Eduardo Cárdenas Velarde.
    
    Modulo 1: Pyhton Fundamentals.
    
    Información General: Ingeniero Informático con experiencia en automatización de procesos, actualmente trabajando en el Backoffice de un Banco.
    
    Año: 2026.
    
    Descripción: Proyecto enfocado en el desarrollo de una Aplicación con Streamlit.
    '''
    )
  # --- Creo dos columnas ---
  col_izq, col_der = st.columns([2, 1])
  # --- Asigno columna derecha ---
  with col_der:
    # --- Logo ---
    st.image('Python_logo.png',width=400)
    # --- Comentario ---
    st.write("Elaborado por: Erick Cárdenas")
  
elif app_mode == 'Ejercicio 1':
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 1 - Flujo de Caja")
  # --- Descripción del ejercicio ---
  st.markdown("""
  ## Flujo de caja con listas
  Registra y administra tus movimientos financieros de forma sencilla. Ingresa el concepto, el tipo (ingreso o gasto) y el monto para visualizar al instante tu historial, totales y el estado actual de tu flujo de caja.
  """)
  # --- Linea divisora ---
  st.divider()
  # --- Inicialización del estado (Session State) ---
  if "historial" not in st.session_state:
    st.session_state.historial = []
  # --- Interfaz de entrada de datos ---
  col1, col2, col3 = st.columns([2, 1, 1])
  with col1:
    concepto = st.text_input("Concepto", placeholder="Ej: Pago de servicio de agua")
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
  # --- Linea divisora ---
  st.divider()
  # --- Cálculos y Resultados ---
  if st.session_state.historial:
    # Convertir a DataFrame para facilitar cálculos
    df = pd.DataFrame(st.session_state.historial)
    # Calcular totales
    total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
    total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
    saldo_final = total_ingresos - total_gastos
    # Mostrar tabla de movimientos registrados
    st.subheader("Lista de movimientos registrados")
    st.dataframe(df, use_container_width=True, hide_index=True)
    # Mostrar métricas
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
    c2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
    c3.metric("Saldo Final", f"S/{saldo_final:,.2f}")
    # Resumen del flujo de la caja
    if saldo_final >= 0:
      st.success(f"### El flujo de caja está **A FAVOR** 📈")
    else:
      st.error(f"### El flujo de caja está **EN CONTRA** 📉")
    # Botón de reinicio
    if st.button("Limpiar todo"):
      st.session_state.historial = []
      st.rerun()
  else:
    st.info("Aún no hay movimientos registrados.")
elif app_mode == 'Ejercicio 2':
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 2 - Formulario")
  # --- Descripción del ejercicio ---
  st.markdown("""
  ## Formulario
  Módulo de registro de ventas para accesorios y dispositivos I/O, desarrollado con arreglos de NumPy para un procesamiento de datos eficiente.
  """)
  # --- Linea divisora ---
  st.divider()
  # --- Inicialización del estado (Session State) ---
  if "registros" not in st.session_state:
    st.session_state.registros = []
    # --- Inicialización del estado (Session State) ---
  st.subheader("Registro con NumPy, arrays y DataFrame")
  producto =  st.text_input('Producto', placeholder="Ej: Ingrese producto")
  categoria = st.selectbox('Categoría',['Laptop','Teclado','Mouse','Disco externo'])
  precio_unitario = st.number_input('Precio Unitario', min_value=0.0, step=1.0)
  cantidad = st.number_input("Cantidad", min_value=0, step=1)
  total = cantidad*precio_unitario
  # Botón para agregar
  if st.button('agregar registro'):
    if producto.strip()=="":
      st.error('ingresar un producto')
    elif precio_unitario <0:
      st.error ('el precio debe ser mayor a cero')
    elif cantidad <0:
      st.error ('la cantidad debe ser mayor a cero')
    else: 
      registro = {
        'producto': producto,
        'categoria' : categoria,
        'precio unitario' : precio_unitario,
        'cantidad' : cantidad,
        'total': total
      }
      st.session_state.registros.append(registro)
      st.success("Agregado")
    if st.session_state.registros:
      df = pd.DataFrame(st.session_state.registros)
      st.dataframe(df,use_container_width=True, hide_index=True)
      # Botón para reiniciar
    if st.button("Limpiar todo"):
      st.session_state.registros = []
      st.rerun()
    else:
      st.info("Aún no hay registros.")
elif app_mode == 'Ejercicio 3':
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 3 - Cálculo de Disponibilidad") 
  # --- Inicialización del estado (Session State) ---
  if 'historico_resultados' not in st.session_state:
    st.session_state.historico_resultados = []
  # --- Titulo ---
  st.subheader("Uso de funciones desde una librería externa")
  # Selector de función (aunque solo usemos una, el ejercicio lo pide)
  opcion = st.selectbox("Seleccione la función a utilizar", ["Calcular Cuota Prestamo Frances"])
  # Widgets para ingresar parámetros
  st.subheader("Parámetros de entrada")
  col1, col2, col3 = st.columns(3)
  with col1:
    t_monto = st.number_input("Monto", min_value=1.0, value=1000.0, step=1000.0)
  with col2:
    t_tasa = st.number_input("Tasa (%)", min_value=0.0, value=0.0, step=0.1)
  with col3:
    t_plazo = st.number_input("Plazo (meses)", min_value=0.0, value=0.0, step=0.1)
  # Botón para ejecutar y mostrar resultado
  if st.button("Ejecutar Función"):
    try:
      # Ejecución de la función desde la librería externa
      # Recordar que devuelve un diccionario: {"disponibilidad_pct": valor}
      resultado_dict = lfp.calcular_cuota_prestamo_frances(t_monto, t_tasa, t_plazo)
      # Extraer el valor del diccionario
      valor_cuota = resultado_dict["cuota_mensual"]
      
      # 5. Mostrar resultado en pantalla
      st.success(f"La cuota calculada es: {valor_cuota}")
      st.metric("Resultado", f"{valor_cuota}")
      
      # 6. Guardar en el histórico para el DataFrame
      registro = {
        "Monto": t_monto,
        "Tasa (%)": t_tasa,
        "Plazo (m)": t_plazo,
        "Cuota": valor_cuota
      }
      st.session_state.historico_resultados.append(registro)
    
    except ValueError as e:
      st.error(f"Error en los parámetros: {e}")
  
  # --- Mostrar tabla histórica ---
  st.divider()
  st.subheader("Tabla histórica de resultados")
  
  if st.session_state.historico_resultados:
      df_historico = pd.DataFrame(st.session_state.historico_resultados)
      st.dataframe(df_historico, use_container_width=True, hide_index=True)
  else:
      st.info("Aún no hay registros en el histórico.")
elif app_mode == 'Ejercicio 4':
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 4 - CRUD")
  # --- Inicialización del estado (Session State) ---
  if 'proyectos' not in st.session_state:
    st.session_state.proyectos = []
  # --- Título ---
  st.subheader("Gestión de Proyectos de Inversion (CRUD)")
  # Usamos Tabs para organizar el CRUD
  tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])
  # ---------------------------------------------------------
  # C - CREATE (Crear)
  # ---------------------------------------------------------
  with tab_crear:
    st.subheader("Registrar Nuevo Proyecto de Inversion")
    with st.form("form_registro"):
      t_nombre = st.text_input("Nombre del Proyecto")
      t_inversion = st.number_input("Monto de Inversion Inicial Total ", min_value=1.0, value=1000.0)
      t_flujos = st.number_input("Flujos", min_value=1.0, value=1.0)
      t_tasa = st.number_input("Tasa dscto (%)", min_value=0.0, value=1.0)
      btn_crear = st.form_submit_button("Guardar Servidor")
      if btn_crear:
        try:
          # Instanciamos la clase de la librería
          nuevo_srv = srv.ProyectoInversion(t_nombre, t_inversion, [t_flujos,t_flujos], t_tasa)
          # Guardamos el resumen (diccionario) en la lista
          st.session_state.proyectos.append(nuevo_srv.resumen())
          st.success(f"Proyecto de Inversion {t_nombre} registrado!")
        except ValueError as e:
          st.error(f"Error: {e}")
  # ---------------------------------------------------------
  # R - READ (Leer)
  # ---------------------------------------------------------
  with tab_leer:
    st.subheader("Listado de Proyectos de Inversion")
    if st.session_state.proyectos:
      df = pd.DataFrame(st.session_state.proyectos)
      st.dataframe(df, use_container_width=True)
    else:
      st.info("No hay Proyectos de Inversion registrados.")
  # ---------------------------------------------------------
  # U - UPDATE (Actualizar)
  # ---------------------------------------------------------
  with tab_actualizar:
    st.subheader("Modificar Datos")
    if st.session_state.proyectos:
      nombres_srv = [s['proyecto'] for s in st.session_state.proyectos]
      elegido = st.selectbox("Selecciona el proyecto para editar", nombres_srv)
      
      # Formulario de edición
      nuevo_t_inversion = st.number_input("Nuevo Monto de Inversion Inicial Total", min_value=1.0)
      nuevo_t_flujos = st.number_input("Nuevo Flujos", min_value=1.0)
      nuevo_t_tasa = st.number_input("Nueva Tasa dscto", min_value=0.0)
      
      if st.button("Actualizar"):
        for s in st.session_state.proyectos:
          if s['proyecto'] == elegido:
            # Recalculamos usando la clase de nuevo para validar
            try:
              # Buscamos datos originales para no perder el nombre y totales
              # (En un CRUD real guardaríamos el objeto completo)
              upd = srv.ProyectoInversion(elegido, nuevo_t_inversion, [nuevo_t_flujos,nuevo_t_flujos], nuevo_t_tasa) 
              s['vpn'] = round(upd.calcular_vpn(), 2)
              s['roi_pct'] = round(upd.calcular_roi(), 2)
              s['payback_anios'] = round(upd.calcular_payback_simple(), 2)
              s['decision'] = "Viable" if s['vpn'] > 0 else "No viable"
              st.success("Actualizado")
              st.rerun()
            except ValueError as e:
              st.error(e)
      else:
        st.write("Nada que actualizar.")
  # ---------------------------------------------------------
  # D - DELETE (Eliminar)
  # ---------------------------------------------------------
  with tab_eliminar:
    st.subheader("Eliminar Registros")
    if st.session_state.proyectos:
      nombres_eliminar = [s['proyecto'] for s in st.session_state.proyectos]
      a_borrar = st.selectbox("Selecciona servidor a borrar", nombres_eliminar)
      
      if st.button("Eliminar permanentemente", type="primary"):
        st.session_state.proyectos = [s for s in st.session_state.servidores if s['proyecto'] != a_borrar]
        st.warning(f"Proyecto de Inversion {a_borrar} eliminado.")
        st.rerun()
