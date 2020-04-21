#!/usr/bin/python3
# VK-Covid-Status
# Author: FSystem88
import requests
import time
import os
import json
from colorama import Fore, Back, Style
from covid import token
def Main():
	global info
	global token
	logo = Fore.GREEN+"8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888 VK Codid Status 8888\n8888     MPL-2.0     8888\n8888888888888888888888888\n8888888888888888888888888"+Style.RESET_ALL
	info=""
	def clear():
		os.system('cls' if os.name=='nt' else 'clear')
	def main():
		global info
		global token
		while True:
			clear()
			print(logo)
			print(info)
			if token == "":
				print(Fore.GREEN+"Введите полученный токен:"+Style.RESET_ALL)
				token = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
				print(Fore.GREEN+"Сохранить данный токен для дальнейшего использования? \n"+Style.RESET_ALL+"(Токен хранится у Вас в файле covid.py и никуда не передается)\n"+Fore.GREEN+"(y/n)"+Style.RESET_ALL)
				choice = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
				if choice == "y":
					os.system("echo token=\"'{}'\">~/vk-covid/covid.py".format(token))
					print(Fore.GREEN+"Токен сохранен"+Style.RESET_ALL)
				else:
					print(Fore.RED+"Токен не сохранен"+Style.RESET_ALL)
			else:
				print(Fore.GREEN+"Выгрузить сохраненный токен? (y/n)"+Style.RESET_ALL)
				choice = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
				if choice == "y":
					pass
				elif choice == "n":
					print(Fore.GREEN+"Введите полученный токен:"+Style.RESET_ALL)
					token = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
					if token == "":
						print(Fore.RED+"Неверное значение"+Style.RESET_ALL)
						time.sleep(3)
						Main()
					print(Fore.GREEN+"Сохранить новый токен для дальнейшего использования? \n"+Style.RESET_ALL+"(Токен хранится у Вас в файле covid.py и никуда не передается)\n"+Fore.GREEN+"(y/n)"+Style.RESET_ALL)
					choice = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
					if choice == "y":
						os.system("echo token=\"'{}'\">~/vk-covid/covid.py".format(token))
						print(Fore.GREEN+"Токен сохранен"+Style.RESET_ALL)
					else:
						print(Fore.RED+"Токен не сохранен"+Style.RESET_ALL)
				else:
					print(Fore.RED+"Неверное значение"+Style.RESET_ALL)
					Main()
			print(Fore.GREEN+"Введите период обновления статуса:"+Style.RESET_ALL)
			print(Fore.GREEN+"Пример:\ns30 - 30 секунд\nm5 - 5 минут\nh1 - 1 час\nd1 - 1 день."+Style.RESET_ALL)
			uptime = input(Fore.BLUE+"VK-Covid-Status > "+Style.RESET_ALL)
			if uptime=="":
				print(Fore.RED+"Неверное значение"+Style.RESET_ALL)
				Main()
			elif uptime[0]=="s":
				t=int(uptime[1:])
			elif uptime[0]=="m":
				t=int(uptime[1:])*60
			elif uptime[0]=="h":
				t=int(uptime[1:])*3600
			elif uptime[0]=="d":
				t=int(uptime[1:])*86400
			clear()
			info = "Токен: {}\nПериод изменения:{} sec\n\nДля отмены нажмите Ctrl+Z".format(token, t)
			print(logo)
			print(info)
			status_id=1
			request_id=1
			while True:
				requests.post("https://api.vk.com/method/users.setCovidStatus?api_id=7362610&method=users.setCovidStatus&format=json&v=5.103&status_id={}&access_token={}&request_id={}".format(status_id,token,request_id))
				if status_id == 17:
					status_id = 1
				else:
					status_id+=1
				request_id+=2
				time.sleep(t)

	main()
Main()
