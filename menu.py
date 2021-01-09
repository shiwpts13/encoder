from colorama import Fore
import sys
import os
import time

banner = """
  ___ _ __   ___ ___   __| | ___ _ __
 / _ \ '_ \ / __/ _ \ / _` |/ _ \ '__|
|  __/ | | | (_| (_) | (_| |  __/ |
 \___|_| |_|\___\___/ \__,_|\___|_|

 version:1.1
 coded by SHIWPTS13
 powered by Guardiran Security Team
 website: https://guardiran.org

		"""

while True:
	try:
		os.system('clear')
		time.sleep(0.1)
		print(Fore.LIGHTBLUE_EX+banner)
		print(Fore.GREEN+'[*]1: persian(فارسی)')
		time.sleep(0.2)
		print(Fore.GREEN+'[*]2: english')
		time.sleep(0.2)
		print(Fore.GREEN+'[*]3: arabic(عربی)')
		time.sleep(0.2)
		print(Fore.RED+'[*]4: exit')
		time.sleep(0.2)
		inp = int(input(Fore.CYAN+'wich one number: '))
		if inp == 1:
			from  modulespersian import compilep, decompilep
			while True:
				try:
					os.system('clear')
					time.sleep(0.1)
					print(Fore.LIGHTBLUE_EX+banner)
					print(Fore.RED+'[*]'+Fore.CYAN+'1: text to code (فارسی)')
					time.sleep(0.2)
					print(Fore.RED+'[*]'+Fore.CYAN+ '2: code to text(فارسی)')
					time.sleep(0.2)
					print(Fore.RED+'[*]3: exit')
					time.sleep(0.2)
					inp = int(input(Fore.GREEN+'wich one number: '))
        
					if inp == 1:
						compilep()
	    
					elif inp == 2:
						decompilep()
					elif inp == 3:
						break
						sys.exit()
        		
				except:
					print(Fore.RED+'sory')
					input('back to menu and try again')

		elif inp == 2:
			from  modulesenglish import compile, decompile
			while True:
				try:    
					os.system('clear')
					time.sleep(0.1)
					print(Fore.LIGHTBLUE_EX+banner)
					print(Fore.RED+'[*]'+Fore.CYAN+'1: text to code(english)')
					time.sleep(0.2)
					print(Fore.RED+'[*]'+Fore.CYAN+ '2: code to text(english)')
					time.sleep(0.2)
					print(Fore.RED+'[*]3: exit')
					inp = int(input(Fore.GREEN+'wich one number: '))
					if inp == 1: 
						compile()
	    
					elif inp == 2:
						decompile()
					elif inp == 3:
						break
						sys.exit()
				except:
					print(Fore.RED+'sory')
					input('back to menu and try again')
		elif inp == 3:
			from  modulesarabic import compilea, decompilea
			while True:
				try:    
					os.system('clear')
					time.sleep(0.1)
					print(Fore.LIGHTBLUE_EX+banner)
					print(Fore.RED+'[*]'+Fore.CYAN+'1: text to code(عربی)')
					time.sleep(0.2)
					print(Fore.RED+'[*]'+Fore.CYAN+ '2: code to text(عربی)')
					time.sleep(0.2)
					print(Fore.RED+'[*]3: exit')
					inp = int(input(Fore.GREEN+'wich one number: '))
					if inp == 1: 
						compilea()
	    
					elif inp == 2:
						decompilea()
					elif inp == 3:
						break
						sys.exit()
				except:
					print(Fore.RED+'sory')
					input('back to menu and try again')
		
		elif inp == 4:
			print(Fore.MAGENTA+'good bye')
			break
			sys.exit
	
	except:
		sys.exit()
