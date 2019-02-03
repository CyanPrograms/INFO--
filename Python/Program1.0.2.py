# -*- coding: utf-8 -*-

"""
Author:............. Luka Orlić
Licence:............ Freeware
Created Date:....... 30.11.2018 (v1.0.0)
Current Version:.... v1.0.2

Description:

    School asigment for our computer science class. This is our first program
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
                
                - Added descriptions
                
    01.12.2018
    
                - Details & Looks, formatting
                
                - Fixed int and str problems (IPCHECK output)

                - Else
    03.12.2018
                Improved help commanmd
                
"""

# --Imports--//////////////////////////////////////////////////////////////// #

import subprocess as sp

# --Functions--////////////////////////////////////////////////////////////// #

lastipconfigresult  =  ""
nslookup            = ""
ipconfig            = ""
ping                = ""

def about():

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
    Current Version  -  v1.0.2
    Version Date     -  3.12.2018
    '''

    )

 

# --------------------------------------------------------------------------- #

def ipcheck(pop):

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

    status, pingc  =  sp.getstatusoutput("ping "  +  str(pop))
    if status == 0:
        print("\n\t\tSystem Operational - Returned status: "  +  str(status) +  
              "\n\n"  +  "\t\tSystem returns: ")
        print("\t"  +  pingc.replace("\n","\n\t\t"))
    else:
        print("\n\t\tSystem not Operational - Returned status:"  +  str(status))
          
# --------------------------------------------------------------------------- #

def ipmac(sw, fnd="Physical Address"):
    print("\n\n\n\t" + fnd + ":  \n\n\n")
    for i in sw.split("\n"):
        if fnd.lower() in i.lower():
            print(i)   
 
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

    addr = sp.getstatusoutput("nslookup "  +  str(URL))
    if addr[0] == 0:
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
    global lastipconfigresult
    lastipconfigresult = ip[1]
    if srch:
        ipmac(ip[1],input("Search string: "))
    else:
        print("System information comes back as: \n\n"  +  ip[1])
        ipmac(ip[1])

# --------------------------------------------------------------------------- #

def phelp(hcommand):  # Definira funkcijo phelp

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
            print(vol.__doc__)
        else:
            print("No documentation")
           
    else:

        helpt  =  [

        "ping      -  Ping computer system",
        "nslookup  -  Look up DNS information",
        "ipconfig  -  Display network information",
        "netstat   -  Displays protocol statistics and current TCP/IP network connections.",
        "vol       -  Displays the disk volume label and serial number, if they exist.",
        "about     -  Display about information",
        "help      -  Print help menu",
        "exit      -  Exit program" 
        ]

        print("\n")
        for i in helpt:
            print("\t" + i)

# --------------------------------------------------------------------------- #

def VOL(volcom):
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
    
        if netvalue  ==  0:
                print("\n\tSystem functional  -  "  +  str(netvalue)  +  "\n\n"
                      +  "\tSystem returns: \n\n")
                print("\t"  +  netreport.replace("\n","\n\t"))
        else:
                print("\n\tSystem not functional  -  "  +  str(netvalue))

# ........................................................................... #
                
def netstat(netcom):
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
    
    if netcom  !=  'netstat'  :
        netvalue, netreport  =  sp.getstatusoutput(netcom)
        netstatunder(netvalue, netreport)
                       
    else:
        netvalue, netreport  =  sp.getstatusoutput("netstat")
        netstatunder(netvalue, netreport)

# ........................................................................... #

def elsecommand(ecom):
    ecval, ecout = sp.getstatusoutput(ecom)
    if ecval != 0
        invinp(ecom)
    elif ecval == 0
        
    
# ........................................................................... #

def invinp(inpc):
    print("\tInput command not valid. \n\tInput commnad: " + str(inpc))
            
# --Main program--/////////////////////////////////////////////////////////// #

work  =  True # spremenljivka za prenehanje neskoncne zane

 
while work: # "neskoncna" zanka   

    command  =  input("Enter Command: ").lower() # vprasa kateri ukaz naj izvede

    # vejitev glede na vpisani ukaz

    if command  ==  "ping"  :
        ipcheck(input("Enter the computer name or IPv4 address: "))
    elif command  ==  "nslookup"  :
        nslookup(input("Enter URL: "))
    elif command  ==  "ipconfig"  :
        ipconfig()
    elif command  ==  "ipconfig -s" :
        ipconfig(True)
    elif command[0:4]  ==  "help"  :
        phelp(command)
    elif command  in  ["exit", "quit", "end", "killself", "terminate"]  :
        work  =  False
    elif command  ==  "about"  :
        about()
    elif command[0:7]  ==  "netstat"  :
        netstat(command)
    elif command[0:3]  ==  "vol" :
        VOL(command)
    elif command  ==  "search ipconfig"  :
        if lastipconfigresult  ==  "":
            print("\n\tFunction IPCONFIG not run")
        else:
            ipmac(lastipconfigresult,input("Search string: "))
    else:
        elsecommand(command)

# --------------------------------------------------------------------------- #       