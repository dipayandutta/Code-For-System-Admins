'''
Author :- Dipayan Dutta
Purpose:- To get the system Details and also the users details
usage :- python get_system_details_cmd.py
note :- Run in normal user mode
Tested On - Ubuntu 16.04 , Fedora 24
'''
import platform
import grp
import os
import subprocess
import time

def getDetials():
  root_id = os.getuid()

  if root_id == 0:
    print 'Please run in normal user mode'
    exit (1)
  else:
    hostname = platform.node()

    groups = [g.gr_name for g in grp.getgrall() if hostname in g.gr_mem]
    group_len = len(groups)
    host_gid = os.getgid()
    host_id  = os.getuid()
    kernel_version = os.uname()[2]
    home_dir = os.getenv("HOME")
    system_distro = platform.dist()[0]
    system_version = platform.dist()[2]
    system_release_name = platform.dist()[1]

    print 'Current username ',hostname
    print 'Users Home Directory ',home_dir
    print "Curent System Time ",time.ctime()
    print 'System OS',platform.system()
    print 'Operation System  Distributer ',system_distro
    print 'Operation System Version ',system_release_name
    print 'Operating System Distribution Name ' , system_version
    print "Operating System's Kernel Version ",kernel_version
    print 'Current System Load Avg ',os.getloadavg()
    print 'OS Architecture ',platform.machine()
    if (group_len != 0):
      print hostname , 'Belongs to : ',','.join(groups)
    else:
      print "No Member in the group"
    print "Hosts Group ID " , host_gid
    print "Hosts User ID ",host_id
    print "Last Three Logins "
    subprocess.call(['last -a | head -3'],shell=True)


def main():
  getDetials()


if __name__ == '__main__':
  getDetials()

