from  subprocess import Popen , PIPE
import os
ips = ['10.10.2.160','10.10.2.162','10.10.2.151','10.10.2.152','10.10.2.154']
for ip in ips:
    ip = str(ip)
    hostup = Popen(["ping","-c3",ip],stdout=PIPE)
    result = hostup.communicate()[0]
    ret_code= hostup.returncode

    if ret_code == 0:
        print (ip,"UP")
    else:
        print(ip,"DOWN")
