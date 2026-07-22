#Este modulo permite ensamblar el resto de componentes en la UI(interfaz de usuario)
import streamlit as st
import pandas as pd
# apartir de aqui voy a importar los componentes reutilizable como si fuera librerias locales.
from componente_datos import IngestorDatos 
from componente_prediccion import MotorPrediccion


#Configuramos la pagina inicial de mi ensamblador de componentes.(app web)
st.set_page_config(page_title="Consola de Componentes comerciales",layout="wide")
st.title("📦 ENSAMBLADOR DE COMPONENTES:INTELIGENCIA DE NEGOCIO")

#instanciamos los componentes de forma local.
ingestor = IngestorDatos() 
predictor = MotorPrediccion(incremento_simulado=0.20)

#Vamos a inicializar el estado de la sesion(session State)
if 'datos_negocio' not in st.session_state:
    st.session_state.datos_negocio = pd.DataFrame()

#Renderizado visual

archivo_cargado = st.file_uploader ("cargar archivo de ventas(CSV)",type="csv")  #vamos a pedirle al usuario que nos suba un archivo.

if archivo_cargado:
    try:
        #usamos el componente de datos para cargar el archivo el estado de la memoria(session state)
        st.session_state.datos_negocio = ingestor.cargar_datos(archivo_cargado)
        st.success("Componente de datos: Imgesta y validación ecitosas")
    except Exception as e :
        st.error(f"Fallo de interfaz de datos: {e} ")

# si hay datos en la session, los componentes visuales e intereactivos se van a activar.
if not st.session_state.datos_negocio.empty:
    col_tabla,col_prediccion= st.columns(2)

    with col_tabla:
        st.subheader("📋 Registro de ventas")
        st.dataframe(st.session_state.datos_negocio,width="stretch")

    with col_prediccion:
        st.subheader("🔮 Predicción de Stock Requerido")
        # Pasamos los datos limpios de un componente al otro de forma directa.
        df_predicciones=predictor.predecir_demanda(st.session_state.datos_negocio)
        st.dataframe(df_predicciones,width="stretch")
        