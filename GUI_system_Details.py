'''
Program Name :- GUI_system_Details.py
Purpose :- Get the System Detils in GUI Mode
Application - To get the system details
Author = Dipayan Dutta
'''

from Tkinter import *
import os
import platform
import grp
import time

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
        self.application()

    def initUI(self):
        self.parent.title("System Details");

    def application(self):

        about_frame = Frame(self.parent,width=300,height=100)
        about_frame.pack()
        about_message = "Tkinter Application to get the Details " \
                        "of the system , created by Dipayan Dutta"
        about_label = Label(about_frame,text=about_message)
        about_label.pack()

        lines_frame = Frame(self.parent,width=300,height=100)
        lines_frame.pack()
        lines = "--------------------------------------------------"
        lines_label = Label(lines_frame,text=lines)
        lines_label.pack()

        system_time_frame = Frame(self.parent,width=300,height=100)
        system_time_frame.pack()
        system_time_label = Label(system_time_frame,text=""+str(time.ctime()))
        system_time_label.pack()

        host_name_Frame = Frame(self.parent,width=300,height=100)
        host_name_Frame.pack()
        host_name = platform.node()
        host_name_label = Label(host_name_Frame,text="Host name =>"+host_name)
        host_name_label.pack()

        home_dir_frame = Frame(self.parent, width=300, height=100)
        home_dir_frame.pack()
        home_dir = os.getenv("HOME")
        home_dir_label = Label(home_dir_frame, text="home directory for  " + host_name + " is "
                                                    + home_dir)
        home_dir_label.pack()

        groups_frame = Frame(self.parent,width=300,height=100);
        groups_frame.pack()
        groups = [g.gr_name for g in grp.getgrall() if host_name in g.gr_mem]
        groups_name = ','.join(groups)
        groups_label = Label(groups_frame,text="host Belongs to =>"+groups_name+" groups")
        groups_label.pack()

        host_id_frame = Frame(self.parent,width=300,height=100)
        host_id_frame.pack()
        host_id = os.getuid()
        host_id_label = Label(host_id_frame,text="Host ID =>"+str(host_id))
        host_id_label.pack()

        host_gid_frame = Frame(self.parent,width=300,height=100)
        host_gid_frame.pack()
        host_gid = os.getgid();
        host_gid_label = Label(host_gid_frame,text="Host Group ID => "+str(host_gid))
        host_gid_label.pack()

        if (host_id == host_gid):
            message_frame = Frame(self.parent,width=300,height=100)
            message_frame.pack()
            message_label = Label(message_frame,text="i.e host belongs to its own group"
                                  )
            message_label.pack()
        else:
            message_frame = Frame(self.parent,width=300,height=100)
            message_frame.pack()
            message_label = Label(message_frame,text="Host does not Belongs its own group")

        system_os_frame = Frame(self.parent,width=300,height=100)
        system_os_frame.pack()
        system_os = platform.system()
        system_os_label = Label(system_os_frame,text="System's OS  is => "+system_os)
        system_os_label.pack()

        system_arch_frame = Frame(self.parent,width=300,height=100)
        system_arch_frame.pack()
        system_arch = platform.machine()

        if (system_arch == "x86_64"):
            system_arch_label = Label(system_arch_frame,text="It is 64 bit Machine")
            system_arch_label.pack()
        else:
            system_arch_label = Label(system_arch_frame, text="It is 32 bit Machine")
            system_arch_label.pack()
        kernel_version_frame = Frame(self.parent, width=300, height=100)
        kernel_version_frame.pack()
        kernel_version = os.uname()[2]
        kernel_version_label = Label(kernel_version_frame, text="Kernel Version " + str(kernel_version))
        kernel_version_label.pack()

        system_distro_frame = Frame(self.parent,width=300,height=100)
        system_distro_frame.pack()
        system_distro = platform.dist()[0]
        system_distro_label = Label(system_distro_frame,text="OS Distributor "+system_distro)
        system_distro_label.pack()

        system_version_frame = Frame(self.parent,width=300,height=100)
        system_version_frame.pack()
        system_version = platform.dist()[1]
        system_version_label = Label(system_version_frame,text="Distro Version => "+str(
            system_version
        ))
        system_version_label.pack()

        distro_release_name_frame = Frame(self.parent,width=300,height=100)
        distro_release_name_frame.pack()
        distro_release_name = platform.dist()[2]
        distro_release_name_label = Label(distro_release_name_frame,text="Release Name => "+
                                                                         distro_release_name)
        distro_release_name_label.pack()

        lines_frame = Frame(self.parent, width=300, height=100)
        lines_frame.pack()
        lines = "--------------------------------------------------"
        lines_label = Label(lines_frame, text=lines)
        lines_label.pack()


        quitButton = Button(self.parent,text="Quit",command=self.quit)
        quitButton.pack()

def main():
    root = Tk()
    application = Example(root)
    root.geometry("520x360+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()