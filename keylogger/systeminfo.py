import socket
import sys 
import platform
import os
def computer_information():
    with open(os.path.abspath("sysinfo.txt"),"a") as f:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        try:
            public_ip=get("https://api.ipfy.org").text
            f.write("Public IP address: "+public_ip)
        except Exception:
            f.write("Couldnt get public ip add \n")

        f.write("Processor: "+(platform.processor())+'\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

