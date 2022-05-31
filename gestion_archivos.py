# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:00:13 2022

@author: 18130
"""

import os
def crear_archivo(nombre,contenido):
     archivo=open(nombre,"wt")
     archivo.writable(contenido)
     archivo.close()
