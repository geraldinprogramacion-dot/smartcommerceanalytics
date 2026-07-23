#Este componente se encarga exclusivamente de la ingesta,limpieza  y validación  de datos.
#Es el motor de datos
import pandas as pd
class IngestorDatos:
    """Componente independiente para la ingesta y  validacion de datos comerciales """
    def __init__(self):
        pass
    
    def cargar_datos(self, archivo) -> pd.DataFrame:
        """ Carga un archivo y valida  con la interfaz  requerida """

        #El bloque Try,se usa junto con except para manejar errores
        #  y execpciones de forma controlada , evitando que el codigo
        #se rompoa abruptamente al suceder un error, definido
        # acciones alternativas.
        try:  
            df = pd.read_csv(archivo, sep=None, engine='python', encoding='utf-8-sig')
            df.columns = df.columns.str.strip().str.lower()
            #  Usamos sep=None y el motor de python para que pandas detecte
            # automaticamente si el archivo usa comas(,)puntos y coma (;) o tabuladores( espacio)

            #validamos el contrato de la interfaz(columnas requeridas)
            columnas_requeridas= {'fecha','producto','cantidad','precio_unitario'}
            if not columnas_requeridas.issubset(df.columns): #si columnas requeridas no escribe lo anterior requerido.
                raise ValueError(f"El archivo no cumple con el contrato.columnas requeridas:{ columnas_requeridas}")#me permite mostrar un mensaje de error controlado.
            #limpieza conversión de tipos de datos
            df ['fecha']=pd.to_datetime(df['fecha']) #convertir a un tipo de dato datetime
            df ['total_venta']=df ['cantidad']*df ['precio_unitario'] 
            return df
        except Exception as e:
            raise IOError(f"Error al procesar el componente de datos{e}")
        
        
    
