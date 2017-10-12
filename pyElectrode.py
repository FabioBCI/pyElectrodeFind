 #!/usr/bin/python
 # -*- coding: utf-8 -*-

#Autor: Fabio BCI
#Date: 06/10/2017

#TODO: option for print a list of electrodes

import pandas as pd
import numpy as np
import os
import sys
from argparse import ArgumentParser

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
	print(electrodes)
	raw_input("[*]- Press intro to continue ...")
	if(mode==1):
		main_menu(electrodes,mode)
	else:
		message_exit()
		sys.exit(1)

def list_names_electrodes(electrodes,mode):

	print(electrodes_data["electrode"])
	raw_input("[*]- Press intro to continue ...")
	if(mode==1):
		main_menu(electrodes,mode)
	else:
		message_exit()
		sys.exit(1)

def find_electrode_name_menu(electrodes,mode):
	name_electrode=raw_input("Name of electrode:")
	if(mode==1):
		dades=(electrodes.loc[electrodes['electrode']==name_electrode])
		if(np.shape(dades)[0]==0):
			print("No found the name of electrode")
		else:
			print(dades)

		raw_input("[*]- Press intro to continue ...")
		main_menu(electrodes,mode)
	else:
		for i in electrodes_data:
			if(electrodes_data[i]["electrode"]==name_electrode):
				print(electrodes_data[i])
				pass
			else:
				pass
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

def main_shell(options):
	electrodes_data=pd.read_csv(options.electrodes,header=0)
	if(options.mode==0):
		#Mode command line
		if(options.l=='1'):
			list_electrodes(electrodes_data,options.mode)
		else:
			if(options.l=='2'):
				list_names_electrodes(electrodes_data,options.mode)
			else:
				pass
	else:
		#Mode menu		
		main_menu(electrodes_data,options.mode)
		


def main():
	argp=ArgumentParser(version='1.0',description='Program for work with electrode EEG positons.',epilog='Copyright 2017 Autor under license GPL v3.0')

	
	argp.add_argument('-file',help='file that contains the electrode data in .csv',dest='electrodes',required='True')
	argp.add_argument('-m',help='command line mode or menu mode, menu mode=0 commandline mode=1',dest='mode',action='store',required='True',type=int)
	argp.add_argument('-l',help='list all electrodes by name or by name and position')
	argp.add_argument('-f',help='find one electrode')
	opts = argp.parse_args()

	main_shell(opts)	


if __name__=='__main__':
	main()