#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def ayudaPrincipal():
	print (" ---------------------------------------------------------------------")
	print ("                                                                                     ")
	print (" \tALGORITMOS CRIPTOGRAFICOS                                                     ")
	print ("										      ")
	print ("| sintaxis: python3 principal.py <algoritmo>					      ")
	print ("										      ")
	print (" <algoritmo>:									      ")
	print ("\t-sc    Algoritmo de sustitución monoalfabética Julio Cesar		      ")
	print ("\      -k    Criptoanalisis de Kasiski		                            ")

	print (" --------------------------------------------------------------------")



def ayudaCesar():
	print (" -------------------------------------------------------------------------------------")
	print ("|                                                                                     |")
	print ("| \tALGORITMO JULIO CÉSAR		                                              |")
	print ("|										      |")
	print ("| sintaxis: python3 principal.py -sc <modo> <archivoEntrada> <clave>                  |")
	print ("|										      |")
	print ("| <modo>:									      |")
	print ("|\t-c    para cifrar el archivo			             		      |")
	print ("|\t-d    para decifrar el archivo                  			      |")
	print ("| 										      |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt|")
	print ("|										      |")
	print ("| <clave>: es un número que corresponde al desplazamiento del alfabeto                |")
	print ("|										      |")
	print ("|                                        	 	                              |")
	print ("|\tsintaxis: python3 principal.py -sc <modo> <archivoEntrada> <clave>        |")
	print ("|										      |")
	print ("| Forma:    					 				      |")
	print ("|										      |")	
	print ("|\tcifrar:    python3 principal.py -sc -c textos_prueba/quijote.txt 4                             |")
	print ("|\tdescifrar: python3 principal.py -sc -d textos_prueba/quijote.txt.cif 4                      |")
	print ("|\                                                                               |")
	print ("|\                                                                               |")
	print (" -------------------------------------------------------------------------------------")

def ayudaKasiski():
	print (" -------------------------------------------------------------------------------------")
	print ("|                                                                                     |")
	print ("| \tALGORITMO CRIPTOANALISIS KASISKI		                                              |")
	print ("|										      |")
	print ("| sintaxis: python3 principal.py -k <archivoEntrada> <clave>                  |")
	print ("|										      |")
	print ("| <modo>:									      |")
	print ("|\t El archivo debe estar cifrado en viggener		             		      |")
	print ("|\t-k <archivoEntrada> para decifrar el archivo                  			      |")
	print ("| 										      |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada  descifrar ej: texto_cifrado.txt|")
	print ("|										      |")
	print ("   ")
	print ("|										      |")
	print ("|                                        	 	                              |")
	print ("|\tsintaxis: python3 principal.py -k <archivoEntrada>        |")
	
	print (" -------------------------------------------------------------------------------------")
