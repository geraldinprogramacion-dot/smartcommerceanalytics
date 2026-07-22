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

archivo_cargado = st.file_uploader ("cargar archivo de ventas(CSV)",type="csv")




