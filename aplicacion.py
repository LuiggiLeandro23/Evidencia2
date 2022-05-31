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
     
def eliminar():
     print("--Eliminar archivo")
     archivo = input("Archivo: ")
     gestion_archivos.eliminar_archivo(archivo)

def agregar():
     print("--Agregar Datos a un Archivo--")
     archivo = input("Archivo: ")
  
     contenido = input("Contenido: ")
     gestion_archivos.agregar_contenido_archivo(archivo, contenido)
     
def listar():
     print("--Mostrar contenido de un archivo--")
     archivo = input("Archivo") 
     
          
def salir():
     print("Gracias por su visita....") 
     
def error():
     print("Opcion incorrecta")