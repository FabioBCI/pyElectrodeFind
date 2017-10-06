 #!/usr/bin/python
 # -*- coding: utf-8 -*-

#Autor: Fabio BCI
#Date: 06/10/2017

#TODO: option for print a list of electrodes

import pandas as pd
import os
import sys
import argparse

def main_menu(electrodes,mode):
	os.system("clear")

	print('******************************************')
	print('*        WELCOME pyELECTRODE             *')
	print('*              v.1.0                     *')
	print('*                                        *')
	print('*          License: GNU. v3              *')
	print('*                                        *')
	print('*                                        *')
	print('*  1- Find electrode with name           *')
	print('*  2- Find electrode with coordenates    *')
	print('*  3- Add electrode                      *')
	print('*  4- List all electrodes                *')
	print('*  5- List name electrodes               *')
	print('*                                        *')
	print('*  6- Exit                               *')
	print('*                                        *')
	print('******************************************')
	
	while True:
		option=int(raw_input(">>")) #Prompt of menu		
		if(option==6):
			message_exit()
			sys.exit(1)
		else:
			switcher={
				1: find_electrode_name_menu,
				2: find_electrode_coordenate,
				3: add_electrode,
				4: list_electrodes,
				5: list_names_electrodes,
				6: lambda: "five"
			}
			func=switcher.get(option,lambda:"nothing")
			return func(electrodes,mode)

def list_electrodes(electrodes,mode):
	electrodes_data=pd.read_csv(electrodes,header=0)
	print(electrodes_data)
	raw_input("[*]- Press intro to continue ...")
	if(mode=="menu"):
		main_menu(electrodes,mode)
	else:
		message_exit()
		sys.exit(1)

def list_names_electrodes(electrodes,mode):
	electrodes_data=pd.read_csv(electrodes,header=0)
	print(electrodes_data["electrode"])
	raw_input("[*]- Press intro to continue ...")
	if(mode=="menu"):
		main_menu(electrodes,mode)
	else:
		message_exit()
		sys.exit(1)

def find_electrode_name_menu(electrodes,mode):
	name_electrode=raw_input("Name of electrode:")
	if(mode=="menu"):
		main_menu(electrodes,mode)
	else:
		message_exit()
		sys.exit(1)

def find_electrode_coordenate():
	pass

def add_electrode():
	pass

def message_exit():	
	print("")
	print("Use Free Software if you want to be free")
	print("")
	print("Thanks !!!")
	print("")

def main_shell():
	file_csv=sys.argv[1]	

	if(len(sys.argv) >= 3):
		parametro=sys.argv[2]
		mode="command"
		switcher={
			"-l": list_electrodes(file_csv,mode),
			"-fn": find_electrode_name_menu(),
		}
		switcher.get(parametro,"nothing")
	else:
		mode="menu"
		main_menu(file_csv,mode)
		


def main():
	main_shell()	


if __name__=='__main__':
	main()