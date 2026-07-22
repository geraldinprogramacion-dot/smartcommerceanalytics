#Componente matimatico aislado que va a realizar los calculos de la estimacion del inventario futuro.(STOCK)
import pandas as pd
import numpy as  np      #Es más veloz haciendo operaciones matimaticas"

#vamos a crear la clase principal dl motor de prediccion
class MotorPrediccion:
    """ Componente Analitico para estimar la demanda futura del inventario"""
    def __init__(self, incremento_simulado=0.15):
        self.incremento = incremento_simulado

    def predecir_demanda(Self,df_historico: pd.DataFrame)-> pd.DataFrame:
        """ 
        Toma los datos historicos y estima el STOCK que se necesita para el proximo mes.
        Logica del componente aislada de la interfez de Usuario 
        """
        if df_historico.empty:
            #empty traduce Vasia(buleanossssss)
            return pd.DataFrame()
        #Agrupamos por producto para ver el promedio de ventas mensuales.
        ventas_promedio = df_historico.groupby('producto')['cantidad'].mean().reset_index()    # mean , si el promedio no lo calcula vuelve al inicio(groupby)Agrupar por (producto) se lo va agregar a cantidad

        #Aplicamos la formula matematicas de stock sugerido(Demanda+Margen de seguridad)
        ventas_promedio['stock_sugerido'] = np.ceil (ventas_promedio['cantidad']*(1 + Self.incremento)).astype(int)
        ventas_promedio.rename(columns={'cantidad':'promedio_historico'},inplace=True)  #quiero que remplace la columna cantidad
        return ventas_promedio
    