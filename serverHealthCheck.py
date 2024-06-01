import paramiko
import paramiko.client
from colorama import Fore, Style

#Host  Details 
host = "127.0.0.1"
username = ""
password = ""

# Root Storage Checker
commandToCheck_RootStorageTotal = "df -h / | awk 'NR==2{print  $2}'| cut -d 'G' -f 1"
commandToCheck_RootStorageUsed = "df -h / | awk 'NR==2{print  $3}' | cut -d 'G' -f 1"
commandToCheck_RootStorageUsedPercent = "df -h / | awk 'NR==2{print $5}'| cut -d '%' -f 1"

# /opt storage checker



# Clinet connection and key auto add policy
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,username=username,password=password,port=2222)

def rootStorageCheck():
    print(Fore.BLUE+"++++++++++++++++++++++Information for  / filesystem ++++++++++++++++")
    print(Fore.LIGHTRED_EX+"---------------------------------------------------------------------")

    _stdinRootStorageTotal,_stdoutRootStorageTotal,_stderrRootStoragetTotal = client.exec_command(commandToCheck_RootStorageTotal)
    print(Fore.BLACK+"Total Storage (GB)  --> {} ".format(_stdoutRootStorageTotal.read().decode()))


    _stdinRootStorageUsed ,_stdoutRootStorageUsed,_stderrRootStorageUsed = client.exec_command(commandToCheck_RootStorageUsed)
    print(Fore.BLACK+"Used Storage (GB) --> {}".format(_stdoutRootStorageUsed.read().decode()))

    _stdinRootStoragePercent , _stdoutRootStoragePercent , _stderrRootStoragePercent = client.exec_command(commandToCheck_RootStorageUsedPercent)
    valueUsed = int(_stdoutRootStoragePercent.read().decode())

    if valueUsed > 50 and valueUsed < 80:
        print(Fore.LIGHTCYAN_EX+"Warning More than 50%... ->{}".format(valueUsed))
    elif valueUsed > 90 and valueUsed < 99:
        print(Fore.RED+"RED Alert ... -> {}".format(valueUsed))
    else:
        print(Fore.GREEN+"used Percentage -->{}".format(valueUsed))

    print(Style.RESET_ALL)

def OsCheck():
    osNameCheck = "cat /etc/os-release | grep 'PRETTY_NAME' | cut -d '=' -f 2"
    _stdinOsName,_stdoutOsName,_stderrOsName = client.exec_command(osNameCheck)
    print(Fore.YELLOW+"OS Name")
    print(Fore.LIGHTRED_EX+"--------------------------------")
    print(Fore.BLUE+"{} ".format(_stdoutOsName.read().decode()))
    print(Fore.LIGHTRED_EX+"--------------------------------")
    print(Style.RESET_ALL)

def checkkernelVersion():
    kernelVersion = "uname -r"
    kernelNumber  = "uname -r | cut -d '.' -f 1"
    _stdinKernelVersion , _stdoutKernelVersion , _stderrKernelVersion = client.exec_command(kernelVersion)
    print("Kernel Version --> {}".format(_stdoutKernelVersion.read().decode()))

    _stdinKernelNumber , _stdoutKernelNumber , _stderrKernelNumber = client.exec_command(kernelNumber)
    

    kernelNumber = int(_stdoutKernelNumber.read().decode())
    if int(kernelNumber)>4 and int(kernelNumber) <= 5:
        print(Fore.LIGHTGREEN_EX+"Presently Stable But need to upgrade")
    elif int(kernelNumber)<4 :
        print(Fore.RED+"Please Update your kernel immediately")
    else:
        print(Fore.GREEN+"Kernel Version -> {}".format(kernelNumber))
    
    print(Style.RESET_ALL)


def checkOpenPorts():
    openPorts = "ss -tulpn | grep LISTEN | awk '{print $5}' | cut -d ':' -f 2 | cut -d ' ' -f 1"
    _stdinOpenPorts,_stdoutOpenPorts,_stderrOpenPorts = client.exec_command(openPorts)
    print(Fore.LIGHTBLUE_EX+"List Of Open Ports")
    print(Fore.BLACK+"------------------------------")
    print(_stdoutOpenPorts.read().decode())

def checkListOfUsers():
    totalUsers = "cat /etc/passwd | wc -l"
    uidMaxMin  = "grep -E '^UID_MIN|^UID_MAX' /etc/login.defs"
    #awk -F: '($3 >= 1000) {printf "%s:%s\n",$1,$3}' /etc/passwd
    nonSystemUsers = "cat /etc/passwd | awk -F : '($3>=1000)' | cut -d ':' -f 1 "
    usersWithLoginShell = "cat /etc/passwd | grep bash | cut -d ':' -f 1"

    _stdinTotalUses , _stdoutTotalUsers , _stderrTotalUsers = client.exec_command(totalUsers)
    _stdinMaxMin , _stdoutMaxMin , _stderrMaxMin = client.exec_command(uidMaxMin)
    _stdinNonSystemUsers , _stdoutNonSystemUsers , _stderrNonSystemUsers = client.exec_command(nonSystemUsers)
    _stdinUsersWithLoginShell , _stdoutUsersWithLoginShell , _stderrUsersWithLoginShell = client.exec_command(usersWithLoginShell)

    print("Total Number of  system users in this system --> {}".format(_stdoutTotalUsers.read().decode()))
    print(Fore.LIGHTRED_EX+" UID Range for Normal Users")
    print(_stdoutMaxMin.read().decode())

    print(Fore.YELLOW+"List of Non System Users")
    print(_stdoutNonSystemUsers.read().decode())

    print(Fore.GREEN+"List of Users with /bin/bash login Shell")
    print(_stdoutUsersWithLoginShell.read().decode())


def checkProcessDetails():
    checkTotalRunningProcess = "ps -e | wc -l"
    
    _stdinCheckTotalRunningProcess , _stdoutCheckTotalRunningProcess , _stderrCheckTotalProcess = client.exec_command(checkTotalRunningProcess)
    print(Fore.BLACK+"----------------------------------------------")
    print(Fore.YELLOW+"Total Number of Running Process")
    print(_stdoutCheckTotalRunningProcess.read().decode())

if __name__ == '__main__':
    OsCheck()
    checkkernelVersion()
    checkOpenPorts()
    checkListOfUsers()
    checkProcessDetails()
    rootStorageCheck()
