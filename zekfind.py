import requests
import os
import sys

def banner():
	print ("""
╔═╗╔═╗╔═╗╦╔═╔═╗╦╔╗╔╔╦╗╔═╗╦═╗ C0d3d By : Zekkel Haxor
╔═╝║╣ ║  ╠╩╗╠╣ ║║║║ ║║║╣ ╠╦╝
╚═╝╚═╝╚═╝╩ ╩╚  ╩╝╚╝═╩╝╚═╝╩╚═
> Aalex, Faisal, Ago Oeng, Panca, Magrisya, Fredley, Ramdhan Maulana <
                    Sulthon, Dani, Jainudin
""")
class yaw:
	def __init__(self):
		self.url = input ("URL => ")
	def yawww(self):
		try:
			sukses = []
			yaw = open('wordlist.txt','r').readlines()
			for c in yaw:
				zekkel = (self.url+'/'+c.strip())
				nani = requests.get(zekkel).text
				if "admin Login" in nani:
					print ("%s --> Found" % zekkel)
					sukses.append(zekkel)
				elif "username" in nani:
					print ("%s --> Found" % zekkel)
					sukses.append(zekkel)
				elif "password" in nani:
					print ("%s --> Found" % zekkel)
					sukses.append(zekkel)
				elif "Admin" in nani:
					print ("%s --> Found " % zekkel)
					sukses.append(zekkel)
				else:
					print ("%s " % zekkel)
			print ("sukses --> %s" % sukses)
		except KeyboardInterrupt:
			print ("CTRL + C")
if __name__ == "__main__":
	os.system('clear')
	banner()
	print ("Pake / di akhir url, ex : Site.com/")
	
	kelas = yaw()
	kelas.yawww()

