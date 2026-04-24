import pytest
import os
from processor.analyzer import analyze_new_lines

def test_funcion_es_llamable():
    assert callable(analyze_new_lines)

def test_manejo_archivo_no_existente():
    """
    Verifica que el motor capture el error de archivo no encontrado
    y devuelva el formato de error esperado.
    """
    resultado = analyze_new_lines("C:/ruta/falsa.log")
    
    # Verificamos que sea una lista
    assert isinstance(resultado, list)
    # Verificamos que el primer elemento indique un error
    # (Tu código devuelve una lista con una tupla que empieza con 'error')
    assert resultado[0][0] == 'error'
    assert "No such file or directory" in resultado[0][1]

def test_procesamiento_archivo_vacio(tmp_path):
    d = tmp_path / "subdir"
    d.mkdir()
    archivo_vacio = d / "vacio.log"
    archivo_vacio.write_text("")
    
    # Probamos que el motor sea resiliente
    try:
        analyze_new_lines(str(archivo_vacio))
        paso = True
    except:
        paso = False
    assert paso