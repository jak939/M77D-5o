#Coded By hackers m7d ... And Copyright Ofc xD 
#Youtube : hackers m7d To Know Some Methods ABout Hacking/Cracking/Crading ....
#Sate !
#Sate !
#Sate !
import random 
import string
import  re, os,time,getpass,sys
from platform import system
from random import choice
######## Clear Terminal Or cmd ########
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
######## Work ########
def gplay() :
 print("""  Googleplay Generator Mohanad huj ali """)
 zz=input('Enter Number Keys > ')
 int(zz)
 try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(4))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(4))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(4))
    tsukaza = string.ascii_letters + string.digits
    tsukaza3 = ''.join(choice(tsukaza) for _ in range(4))
    mark = urname1.upper() + taki2.upper() + metsuha3.upper() + tsukaza3.upper()
    print(az+1,")",mark," M 7 D")
    save = open("gplay.txt", 'a')
    save.write(mark + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
    exit()
 except : 
	   	 pass
def abo():
 print("""
 Name : Mohanad huj ali
 Country : SY
 Facebook :Mohanad huj ali
 Mail Me : jak93936@gmail.com
 Github : https://github.com/jak939
 Youtube : Mohanad huj ali """)
 exit()
######## Menu ########
#Ps : Dont Change Logo 2 Say That u r The Coder ...Lean Python Its Free 
def main():
 logo = ("""
 
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░

H A C K E R S
M O H A N A D
    M.  7.   D
Name : Mohanad huj ali
 Country : SY
 Facebook :Mohanad huj ali
 Mail Me : jak93936@gmail.com
 Github : https://github.com/jak939
 Youtube : Mohanad huj ali
   """)
 print(logo)
 print(' Mohanad huj ali   hack card '+getpass.getuser()+' : '+time.asctime( time.localtime(time.time()) ),'\n [!] Sometimes U Need To Use Vpn (Ban Or CountryNotAvaible)\n [1]  Steam ')
 print(" [1]  Google Play ")
 print(" [69] About & Exit ")
 zack = input("$ ")
 if zack == '1' :
    gplay()
 elif zack == '69' :
    abo()
 else :
     print(" Open Ur Eye !! Bakka -____- ")
     exit()
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print (" \nNani ?? ... R U Bakka ??")
sys.exit()
######## Hey U r ... Do u Like Pizza ?? xD ########
