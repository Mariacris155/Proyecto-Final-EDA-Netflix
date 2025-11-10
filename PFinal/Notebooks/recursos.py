import pandas as pd
from typing import List

def inspeccionar_duplicados(df: pd.DataFrame, columna_clave: str) -> pd.DataFrame:
    """
    Identifica y devuelve todos los registros que tienen valores duplicados en la columna clave,
    incluyendo la primera aparición, para inspección. (Usa keep=False).

    Args:
        df: DataFrame de pandas a inspeccionar.
        columna_clave: Nombre de la columna clave (ej: 'movie_id').

    Returns:
        DataFrame con solo los registros duplicados, ordenados por la clave.
    """
    duplicados_mask = df.duplicated(subset=[columna_clave], keep=False)
    df_duplicados = df[duplicados_mask].sort_values(by=columna_clave).copy()
    return df_duplicados

def eliminar_duplicados_por_clave(df: pd.DataFrame, columna_clave: str) -> pd.DataFrame:
    """
    Elimina los duplicados de un DataFrame, manteniendo la primera ocurrencia (keep='first').

    Args:
        df: DataFrame de pandas a limpiar.
        columna_clave: Nombre de la columna clave para la eliminación.

    Returns:
        El DataFrame limpio (eliminando los duplicados).
    """
    df_limpio = df.drop_duplicates(subset=[columna_clave], keep='first').copy()
    return df_limpio

def limpiar_nulos_esenciales(df: pd.DataFrame, columnas_esenciales: List[str]) -> pd.DataFrame:
    """
    Elimina filas donde las columnas clave (esenciales) tienen valores nulos.
    
    Args:
        df: DataFrame de pandas a limpiar.
        columnas_esenciales: Lista de columnas cuyas filas nulas deben eliminarse.

    Returns:
        El DataFrame sin filas con nulos en las columnas esenciales.
    """
    df_limpio = df.dropna(subset=columnas_esenciales).copy()
    return df_limpio