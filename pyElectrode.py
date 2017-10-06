 #!/usr/bin/python
 # -*- coding: utf-8 -*-

#Autor: Fabio BCI
#Date: 06/10/2017

import pandas as pd
import os
import sys

def main_menu():
	os.system("clear")

	print('******************************************')
	print('*        WELCOME pyELECTRODE             *')
	print('*              v.1.0                     *')
	print('*                                        *')
	print('*          Licence: GNU. v3              *')
	print('*                                        *')
	print('*                                        *')
	print('*  1- Find electrode with name           *')
	print('*  2- Finde electrode with coordenates   *')
	print('*  3- Add electrode                      *')
	print('*  4- Create group of electrodes         *')
	print('*  5- Find by group                      *')
	print('*  6- List all electrodes                *')
	print('*  7- List groups                        *')
	print('*                                        *')
	print('*  8- Exit                               *')
	print('*                                        *')
	print('******************************************')
	
	
	while True:
		option=int(raw_input(">>")) #Prompt of menu		
		if(option==8):
			sys.exit(1) #Finis the program
		else:
			return option

def find_electrode_name_menu():
	name_electrode=raw_input("Name of electrode:")

def main():
	option=main_menu()


if __name__=='__main__':
	main()