# -*- coding: utf-8 -*-

details = """
Author:............. Luka Orlić
Licence:............ Freeware
Created Date:....... 30.11.2018 (v1.0.0)
Current Version:.... v1.0.4

Description:

    School assignment for our computer science class. This is our first program
    that we have to create. It is said we require 30 lines of code, variables,
    loops, if statements, lists, functions. It also must require an input from 
    the user.

Change Log:
    
    28.11.2018

                -  Added functions: ipcheck, nslookup

                -  Added if statement: command

    30.11.2018 

                -  Added functions

                -  Moddifed functions

                -  Added while loop
                
                -  Added descriptions
                
    01.12.2018
    
                -  Details & Looks, formatting
                 
                -  Fixed int and str problems (IPCHECK output)

                -  Else
    
    03.12.2018
               
                -  Improved help commanmd
    
    08.12.2018
        
                -  Added functions
                
                -  Edited functions
                
                -  Added import
                
                -  Added global variable
                
                -  Edited formatting
                
                -  Added comments
                
    09.12.2018
    
                -  Modified functions
                
                -  Added functions
                
                -  Added imports
"""

# --Imports--//////////////////////////////////////////////////////////////// #

import subprocess as sp
import platform as pl
import datetime as dt
import os.path as op
import os
import shutil as sl

# --Functions--////////////////////////////////////////////////////////////// #

ipconfigr  =  ""
nslookupr  =  ""
ipcheckr   =  ""
netstatr   =  ""
elsar      =  ""
platform   =  ""
searchr    =  ""

def about(): #izpise osnove o programu

    '''

   ----ABOUT----

        Definition:

            Shows details about the program: Author, version, creation date,
            licence, version date.

        Command:

            about

        Example:

            about
    '''

    print(

    '''
    Author           -  Luka Orlić
    Licence          -  Freeware
    Created Date     -  30.11.2018 (v1.0.0)
    Current Version  -  v1.0.4
    Version Date     -  08.12.2018
    '''

    )

 

# --------------------------------------------------------------------------- #

def ipcheck(pop): # ping funkcija

    '''
    
    ----PING----

        Definition:

            Ping is a basic Internet program that allows a user to verify that a
            particular IP address exists and can accept requests.

        Command:

            ping

        Use ping:

            Enter the computer name or IPv4 address: <url>

        Example:

            Enter the computer name or IPv4 address: youtube.com

            Enter the computer name or IPv4 address: rtvslo.si

            Enter the computer name or IPv4 address: gimvic.org

    '''

# ........................................................................... #
    global ipcheckr
    status, pingc  =  sp.getstatusoutput("ping "  +  str(pop))
    if status == 0:
        ipcheckr = pingc
        print("\n\t\tSystem Operational - Returned status: "  +  str(status) +  
              "\n\n"  +  "\t\tSystem returns: ")
        print("\t"  +  pingc.replace("\n","\n\t\t"))
    else:
        print("\n\t\tSystem not Operational - Returned status:"  +  str(status))
          
# --------------------------------------------------------------------------- #

def ipmac(sw, fnd="Physical Address"): #iskalna funkcija
    global searchr
    print("\n\t" + fnd + ":  \n")
    searchr = ""
    for i in sw.split("\n"):
        if fnd.lower() in i.lower():
            print(i)   
            searchr += "\n" + str(i)

# --------------------------------------------------------------------------- #

def nslookup(URL): # Definira funkcijo nslookup

    '''
    
    ----NSLOOKUP----

        Definition:

            Nslookup is a network administration command-line tool available for
            many computer operating systems for querying the Domain Name System
            (DNS) to obtain domain name or IP address mapping or for any other
            pecific DNS record.

        Command:

            nslookup

        Use Nslookup:

            Enter URL: <url>

        Example:

            Enter URL: youtube.com

            Enter URL: rtvslo.si

            Enter URL: gimvic.org

    '''
    
# ........................................................................... #
    global nslookupr
    
    addr = sp.getstatusoutput("nslookup "  +  str(URL))
    if addr[0] == 0:
        nslookupr = addr[1]
        print("URL: "  +  URL  +  " - Returned information: \n\n"  +  addr[1])
    else:
        print("Nslookup failed - Returned status:"  +  addr[0])

# --------------------------------------------------------------------------- #

def ipconfig(srch=False): # Definira ipconfig

    '''
    
    ----IPCONFIG----
    
        Definition:

            In computing, ipconfig (internet protocol configuration) is a console
           application of some operating systems that displays all current TCP/IP
           network configuration values.

        Command:
            
            ipconfig

        Options in ipicofig:

            -s    :    Allows search of specific parameters

        Use ipconfig:

            ipconfig

            OR

            ipconfig -s            
            (requests new input)
            
            Search string: <Input string - allowed charactes : printable characters>

        Example:

            ipconfig
            
            OR
            
            ipconfig -s
            Search string: physical

            ipconfig -s
            Search string: ip

            ipconfig -s
            Search string: dhcp

    '''
# ........................................................................... #
    
    ip  =  sp.getstatusoutput("ipconfig /all")
    global ipconfigr
    ipconfigr = ip[1]
    if srch:
        ipmac(ip[1],input("Search string: "))
    else:
        print("System information comes back as: \n\n"  +  ip[1])
        ipmac(ip[1])

# --------------------------------------------------------------------------- #

def phelp(hcommand):  # Definira funkcijo phelp
    
    global details
    
    
    if hcommand  !=  'help' :
        hcommand  =  hcommand[4:].strip()
       
        if hcommand    ==  "ping"  :
            print(ipcheck.__doc__)
        elif hcommand  ==  "nslookup"  :
            print(nslookup.__doc__)
        elif hcommand  ==  "ipconfig"  :
            print(ipconfig.__doc__)
        elif hcommand  ==  "about"  :
            print(about.__doc__)
        elif hcommand  ==  "vol"  :
            print(VOL.__doc__)
        elif hcommand  ==  "sysinfo"  :
            print(platform.__doc__)
        elif hcommand  ==  "search"  :
            print(searchglobal.__doc__)
        elif hcommand  ==  "save"  :
            print(save_result.__doc__)
        elif hcommand  ==  "abd"  :
            print(details)
        else:
            elsecommand(hcommand)
           
    else:

        helpt  =  [

        "ping      -  Ping computer system",
        "nslookup  -  Look up DNS information",
        "ipconfig  -  Display network information",
        "netstat   -  Displays protocol statistics and current TCP/IP",
        "             network connections.",
        "vol       -  Displays the disk volume label and serial number,",
        "             if they exist.",
        "sysinfo   -  Displays all or specified system information.",
        "search    -  Searches thru previously called commands.",
        "save      -  Saves the result of any command you input",
        "about     -  Display about information",
        "help      -  Print help menu",
        "exit      -  Exit program" 
        ]

        print("\n")
        for i in helpt:
            print("\t" + i)

# --------------------------------------------------------------------------- #

def VOL(volcom): #funcija vol 
    '''
    ----VOL----

        Definition:

            Displays the disk volume label and serial number, if they exist.

        Command:

            vol <disc:>

        Example:

            vol d:

            vol c:

            vol c: d:

            vol c: d: e:
    '''
    
    vol1  =  sp.getstatusoutput(volcom)
    print("\t"  +  vol1[1].replace("\n", "\n\t"))
# --------------------------------------------------------------------------- #
def netstatunder(netvalue, netreport):
     global netstatr
     
     if netvalue  ==  0:
         netstatr = netreport
         print("\n\tSystem functional  -  "  +  str(netvalue)  +  "\n\n"
               +  "\tSystem returns: \n\n")
         print("\t"  +  netreport.replace("\n","\n\t"))
     else:
        print("\n\tSystem not functional  -  "  +  str(netvalue))

# ........................................................................... #
                
def netstat(netcom): #definira funcijo netstat
    """
    ----NETSTAT----
    
        Definition:

            Displays active TCP connections, ports on which the computer is
            listening, Ethernet statistics, the IP routing table, IPv4 statistics
            (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for
            the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used
            without parameters, netstat displays active TCP connections.

        Command:
            
            netstat

        Options in ipicofig:

            -a            Displays all connections and listening ports.
            -b            Displays the executable involved in creating each connection or
                          listening port. In some cases well-known executables host
                          multiple independent components, and in these cases the
                          sequence of components involved in creating the connection
                          or listening port is displayed. In this case the executable
                          name is in [] at the bottom, on top is the component it called,
                          and so forth until TCP/IP was reached. Note that this option
                          can be time-consuming and will fail unless you have sufficient
                          permissions.
            -e            Displays Ethernet statistics. This may be combined with the -s
                          option.
            -f            Displays Fully Qualified Domain Names (FQDN) for foreign
                          addresses.
            -n            Displays addresses and port numbers in numerical form.
            -o            Displays the owning process ID associated with each connection.
            -p proto      Shows connections for the protocol specified by proto; proto
                          may be any of: TCP, UDP, TCPv6, or UDPv6.  If used with the -s
                          option to display per-protocol statistics, proto may be any of:
                          IP, IPv6, ICMP, ICMPv6, TCP, TCPv6, UDP, or UDPv6.
            -q            Displays all connections, listening ports, and bound
                          nonlistening TCP ports. Bound nonlistening ports may or may not
                          be associated with an active connection.
            -r            Displays the routing table.
            -s            Displays per-protocol statistics.  By default, statistics are
                          shown for IP, IPv6, ICMP, ICMPv6, TCP, TCPv6, UDP, and UDPv6;
                          the -p option may be used to specify a subset of the default.
            -t            Displays the current connection offload state.
            -x            Displays NetworkDirect connections, listeners, and shared
                          endpoints.
            -y            Displays the TCP connection template for all connections.
                          Cannot be combined with the other options.
            interval      Redisplays selected statistics, pausing interval seconds
                          between each display.  Press CTRL+C to stop redisplaying
                          statistics.  If omitted, netstat will print the current
                         configuration information once.

                         
        Use ipconfig:

            netstat

            OR

            netstat -s            
            

        Example:

            ipconfig
            
            OR
            
            netstat -r

            netstat -p
            
            netstat -b

    """
    global netstatr 
    if netcom  !=  'netstat'  :
        netvalue, netreport  =  sp.getstatusoutput(netcom)
        netstatunder(netvalue, netreport)
                       
    else:
        netvalue, netreport  =  sp.getstatusoutput("netstat")
        netstatunder(netvalue, netreport)

# ........................................................................... #
def elsecommandhidden(ecom): # else command hidden se klice za search funkcijo
                             # ko ukaz ki ni posebno definiran v programu se ni
                             # bil klican.
    global elsar
    ecval, ecout = sp.getstatusoutput(ecom)
    elsar = ecout
    return ecout

# ........................................................................... #

def elsecommand(ecom): # izvaja vse nedefinirane ukaze ki so iz CMD-ja
    global elsar
    ecval, ecout = sp.getstatusoutput(ecom)
    #if ecval != 0 :
        #invinp(ecom)
    #elif ecval == 0 :
    elsar = ecout
    print("\n\t" + ecout)

# ........................................................................... #
  
def search_order(searchord): # Funkcija ki sluzi kot umesnik med ipmac in 
                             # search global.
    global ipconfigr  
    global nslookupr       
    global netstatr   
    global elsar
    global ipcheckr
    
    if searchord  ==  "":
        print("\n\tFunction " + str(searchord) + " not run")
    else:
        ipmac(str(searchord) , input("Search string: "))
        
# ........................................................................... #

def searchglobal(cmd): #funkcija ki poda podatke iz gcf v search_order
    '''
    ----SEARCH----

        Definition:

            Searches thru previously called commands.

        Command:

            search <command>

        Example:

            search nslookup

            search dir

            search ipconfig

            search ping
    '''
    global ipconfigr  
    global nslookupr        
    global netstatr   
    global elsar
    global ipcheckr
    
    cmd = cmd[6:].strip()
    
    if cmd == "ipconfig":
        search_order(str(ipconfigr))
    elif cmd == "nslookup":
        search_order(str(nslookupr))
    elif cmd == "ping":
        search_order(str(ipcheckr))
    elif cmd == "netstat":
        search_order(str(netstatr))
    elif cmd == "sysinfo":
        search_order(str(platform))
    else:
        search_order(str(elsecommandhidden(cmd)))

# ........................................................................... #        

def platform(platcom): #izpise sistemske informacije
    '''
    ----SYSINFO----

        Definition:

            Displays all or specified system information.

        Command:

            sysinfo <variables>
            
        Variables:
            
            <No Varaiable> - Displays all information
            
            system         - Displays system (Mac, Linux, Winows)
            
            node           - Displays computers name
            
            release        - Displays OS release (xp, vista, 7, 8, 10)
            
            version        - Displays detailed OS version
            
            Machine        - Displays the machine type
            
            Processor      - Displays processor deatails
            
            Arhitecture    - Display the bits and linkage
            
        Example:

            sysinfo

            sysinfo system

            sysinfo node
    '''
    
    global platform
    
    platcom = platcom[7:].strip()
    
    system = pl.system()
    node = pl.node()
    release = pl.release()
    version = pl.version()
    machine = pl.machine()
    processor = pl.processor()
    ar1, ar2 = pl.architecture()
    
    pr1, pr2 = processor.split(",")
    
    if platcom == 'system':
        print("\n\tOS  :  " + str(system))
    elif platcom == 'node':
        print("\n\tNODE  :  " + str(node))
    elif platcom == 'release':
        print("\n\tRELEASE  :  " + str(release))  
    elif platcom == 'version':
        print("\n\tVERSION  :  " + str(version))
    elif platcom == 'machine':
        print("\n\tMACHINE  :  " + str(machine))
    elif platcom == 'processor':
        print("\n\tPROCESSOR  :   " + str(pr1) + "\n\t              " + str(pr2))
    elif platcom == 'arhitecture':
        print("\n\tARHITECTURE  :  " + ar1 + "\n\t                " + ar2)
    elif platcom == '':
        print()
        print('\tOS         :  ' + system  + '\n'
              '\tRELEASE    :  ' + release + '\n'
              '\tVERSION    :  ' + version + '\n'
              '\tNODE       :  ' + node    + '\n'
              '\tBIT VER.   :  ' + ar1     + '\n'
              '\tARCH VER.  :  ' + ar2     + '\n'
              '\tMACHINE    :  ' + machine + '\n'
              '\tPORCESSOR  :  ' + pr1     + '\n'
              '\t             '  + pr2     + '\n'
              )
    
    platform = '\tOS         :  ' + system  + '\n'
    platform +='\tRELEASE    :  ' + release + '\n'
    platform +='\tVERSION    :  ' + version + '\n'
    platform +='\tNODE       :  ' + node    + '\n'
    platform +='\tBIT VER.   :  ' + ar1     + '\n'
    platform +='\tARCH VER.  :  ' + ar2     + '\n'
    platform +='\tMACHINE    :  ' + machine + '\n'
    platform +='\tPORCESSOR  :  ' + pr1     + '\n'
    platform +='\t             '  + pr2     + '\n'
 
# ........................................................................... #
    
def current_time(): #nam doloci trenutni cas
    y = dt.datetime.now().strftime("%H_%M_%S-%d_%m_%Y")
    return(y)
 
# ........................................................................... #

def text_check(text): # preveri ce je uporabnik unesel ukaz ki obstaja ali ne
    sq = "is not recognized as an internal or external "
    sq += "command, operable program or batch file."
    if sq in text:
        return("not clear")
    else:
        return("clear")
    
    '''
    'ipcofing' is not recognized as an internal or external command,
    operable program or batch file.

    '''
# ........................................................................... #
    
def clear_log():    
    sl.rmtree("log")
    os.mkdir("log")
# ........................................................................... #
def testdef(): #testna funkcija v programu ki ni vidna uporabniku v help ukazu
   '''
   Used as test funciot by author
   '''
# ........................................................................... #

def invinp(inpc): # Izpise da uvneseni ukaz ne obstaja oz. ni pravilen.
    print("\n\tInput command not valid. \n\tInput commnad: " + str(inpc))



# --Save program--/////////////////////////////////////////////////////////// #    


    
def save_program(cmd, savetext): #funkcija ki shrani rezultat kot datoteko .txt
    
    global nslookupr
    
    x = current_time()
    name = str(cmd) + str(x) + ".txt"
    try:
        if not os.path.exists("log"):
            os.mkdir("log")
        path = "./log/"
        with open(op.join(path, name), "wt") as text_file:
            print(f"{savetext}", file=text_file)
    except:
        pass
        #with open(name, "wt") as text_file:
        #    print(f"{savetext}", file=text_file)

# ........................................................................... #

def save_result(cmd): #funkcija ki poda podatke iz gcf v save_program
    '''
     ----SAVE----

        Definition:

            Saves the result of any command you wish

        Command:

            save <command>

        Example:

            save nslookup

            save dir

            save ipconfig

            save ping
    
    '''
    global ipconfigr  
    global nslookupr        
    global netstatr   
    global elsar
    global ipcheckr
    global searchr
        
    cmd = cmd[4:].strip()
    
    if cmd == "ipconfig":
        save_program(cmd, ipconfigr)
    elif cmd == "nslookup":
        save_program(cmd, nslookupr)
    elif cmd == "ping":
        save_program(cmd, ipcheckr)
    elif cmd == "netstat":
        save_program(cmd, netstatr)
    elif cmd == "sysinfo":
        save_program(cmd, platform)
    elif cmd == "search":
        if searchr == "":
           print("\n\tYou havent used the search command yet!")
        elif searchr != "":
            save_program(cmd, searchr)            
    else:
        if text_check(elsecommandhidden(cmd)) == "clear":
            save_program(cmd, elsecommandhidden(cmd))
        else:
            print("You have entered a false save command  :  save " + str(cmd))
  

          
# --Main program--/////////////////////////////////////////////////////////// #



work  =  True # spremenljivka za prenehanje neskoncne zane

 
while work: # "neskoncna" zanka   

    command  =  input("Enter Command: ").lower() # vprasa kateri ukaz naj izvede

    # vejitev glede na vpisani ukaz

    if command         ==  "ping"        :
        ipcheck(input("Enter the computer name or IPv4 address: "))
    elif command       ==  "nslookup"    :
        nslookup(input("Enter URL: "))
    elif command       ==  "ipconfig"    :
        ipconfig()
    elif command       ==  "ipconfig -s" :
        ipconfig(True)
    elif command[0:4]  ==  "help"        :
        phelp(command)
    elif command       ==  "about"       :
        about()
    elif command[0:7]  ==  "netstat"     :
        netstat(command)
    elif command[0:3]  ==  "vol"         :
        VOL(command)
    elif command[0:7]  ==  "sysinfo"     :
        platform(command)
    elif command       ==  "test"        :
        testdef()
    elif command[0:6]  ==  "search"      :
        searchglobal(command)        
    elif command[0:4]  ==  "save"        :
        save_result(command)
    elif command       ==  "cldir"    :
        clear_log()
    elif command  in  ["exit", "quit", "end", "killself", "terminate"]  :
        work  =  False
    else                                 :
        elsecommand(command)

# --------------------------------------------------------------------------- #