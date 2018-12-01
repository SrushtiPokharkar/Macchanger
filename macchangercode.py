#=============================================================================================================
import sys
import os
import time
print('''
_______________________________MACCHANGER_______________________________\n\n\t\t  \033[93mBy :(64)SRUSHTI_POKHARKAR  (71) SUBHASHREE_IYER\033[97m

''')



print(" ")
print("1- show the current MAC-ADDRESS")
print("")
print("2- change your MAC-ADDRESS Randomly")
print("")
print("3- change your MAC-ADDRESS Customly")
print("")
print("4- reset the original MAC-ADDRESS")
print("")
ch=input("\033[92m[?] \033[96mmake your choise ==>")
if ch==('1') :
            print(" ")
            print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
            print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
            print(" ")
            mch=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
            if mch==('1') :
                    
                      os.system('macchanger -s wlan0')
                      print(" ")
                   
                      os.system('python3 macchangercode.py')
            if mch==('2') :
                     
                       os.system('macchanger -s eth0')
                       print(" ")
                       s=input('press any key to continue')
                     
                       os.system('python3 macchangercode.py')

if ch==('2') :
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               ych=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if ych==('2') :
                       
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -r eth0')
                        os.system('ifconfig eth0 up')
                        print(" ")
                        h=input("press any key to continue")
                     
                        os.system('python3 macchangercode.py')
               if ych==('1') :
                    
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -r wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ")
                        h=input("press any key to continue")
                    
                        os.system('python3 macchangercode.py')

if ch==('4'): 
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               zch=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if zch==('2') :
                        print(" ")
                      
                        os.system('macchanger -p eth0')
                        print(" ") 
                        x=input("press any key to continue ")
                     
                        os.system('python3 macchangercode.py')
               if zch==('1') : 
                        print(" ")
                       
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -p wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ") 
                        x=input("press any key to continue ")
             
                        os.system('python3 macchangercode.py')



if ch==('3'):
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               wch=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if wch==('2') :
                        print(" ")
                        os.system('ifconfig eth0 down')
                        dire=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -m'+(dire)+' eth0')
                        os.system('ifconfig eth0 up')
                        print("done")
               if wch==('1') : 
                        os.system('ifconfig wlan0 down')
                        print(" ")
                        dire=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -m'+(dire)+' wlan0')
                        os.system('ifconfig wlan0 up')
                        print("done")




