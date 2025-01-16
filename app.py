# Proyecto app_web alojada en streamlit para gestionar las vacaciones de una pyme

# importamos las librerias necesarias
import pandas as pd
import streamlit as st

# Importamos los datos de las vacaciones de cada empleado
vacaciones_df = pd.read_csv('vacaciones.csv')

def ver_vacaciones(nombre, apellido1, apellido2):
    # Filtramos el dataframe por los apellidos del empleado
    empleado_df = vacaciones_df[(vacaciones_df['Apellido1'] == apellido1) & (vacaciones_df['Apellido2'] == apellido2)]
    
    # Verificamos si se encontró el empleado
    if not empleado_df.empty:
        # Obtenemos los días de vacaciones
        dias_vacaciones = empleado_df['Vacaciones'].values[0]
        return dias_vacaciones
    else:
        return "Empleado no encontrado."

# Ejemplo de uso
dias_vacaciones = ver_vacaciones('Juan', 'Pérez', 'García')
print(dias_vacaciones)  # Esto imprimirá 30 si el empleado existe en el dataframe
