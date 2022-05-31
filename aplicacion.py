# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:06:49 2022

@author: 18130
"""

import gestion_archivos

def menu():
    print("*****MENU PRINCIPAL*****")
    print("1. Crear Archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido del archivo")
    print("5.Salir")
    
def crear():
     print("--Crear Archivo--")
     archivo = input("Archivo: ")
     contenido = input("Contenido: ")
     gestion_archivos.crear_archivos(archivo, contenido)