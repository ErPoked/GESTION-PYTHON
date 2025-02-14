#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  manipulacion_docXML_JCR.py
#  
#  Copyright 2025 usuario <usuario@2asir15>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# CONTENIDO DEL ARCHIVO
"""
<?xml version="1.0"?>
<customers>
   <customer id="55000">
      <name>Charter Group</name>
      <address>
         <street>100 Main</street>
         <city>Framingham</city>
         <state>MA</state>
         <zip>01701</zip>
      </address>
      <address>
         <street>720 Prospect</street>
         <city>Framingham</city>
         <state>MA</state>
         <zip>01701</zip>
      </address>
      <address>
         <street>120 Ridge</street>
         <state>MA</state>
         <zip>01760</zip>
      </address>
   </customer>
</customers>
"""
import xml.etree.ElementTree as ET
import sys
import os

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Mostrar todos los clientes")
    print("2. Mostrar direcciones de un cliente específico")
    print("3. Buscar cliente por ID")
    print("4. Salir")

def cargar_xml(archivo_xml):
    if not os.path.exists(archivo_xml):
        print(f"Error: El archivo {archivo_xml} no existe.")
        sys.exit(1)
    
    try:
        docXML = ET.parse(archivo_xml)
        return docXML.getroot()
    except ET.ParseError as e:
        print(f"Error al parsear el archivo XML: {e}")
        sys.exit(1)

def mostrar_clientes(NodoRaiz):
    for customer in NodoRaiz.findall('customer'):
        print(f"Cliente ID: {customer.get('id')}, Nombre: {customer.find('name').text}")

def mostrar_direcciones_cliente(NodoRaiz, cliente_id):
    for customer in NodoRaiz.findall('customer'):
        if customer.get('id') == cliente_id:
            for address in customer.findall('address'):
                calle = address.find('street').text if address.find('street') is not None else "No disponible"
                ciudad = address.find('city').text if address.find('city') is not None else "No disponible"
                estado = address.find('state').text if address.find('state') is not None else "No disponible"
                codigo_postal = address.find('zip').text if address.find('zip') is not None else "No disponible"
                print(f"  Dirección: {calle}, {ciudad}, {estado} {codigo_postal}")
            return
    print("Cliente no encontrado.")

def buscar_cliente_por_id(NodoRaiz, cliente_id):
    for customer in NodoRaiz.findall('customer'):
        if customer.get('id') == cliente_id:
            print(f"Cliente ID: {customer.get('id')}, Nombre: {customer.find('name').text}")
            return
    print("Cliente no encontrado.")

def main(args):
    archivo_xml = "JCR_ejemplo.xml"
    NodoRaiz = cargar_xml(archivo_xml)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_clientes(NodoRaiz)
        
        elif opcion == "2":
            cliente_id = input("Ingrese el ID del cliente: ")
            mostrar_direcciones_cliente(NodoRaiz, cliente_id)
        
        elif opcion == "3":
            cliente_id = input("Ingrese el ID del cliente: ")
            buscar_cliente_por_id(NodoRaiz, cliente_id)
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    sys.exit(main(sys.argv))