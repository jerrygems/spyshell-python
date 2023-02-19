import os
import sys
import pyfiglet
import socket
import subprocess
import readline
import random
import time
import datetime
import platform
import distro

# color variables
red = '\033[0;31m'
boldRED = '\033[1;31m'
yellow = '\033[1;33m'
green = '\033[0;32m'
blue = '\033[0;34m'
purple = '\033[0;35m'
lightGRN = '\033[1;32m'
lightBLUE = '\033[1;34m'
nc = '\033[0m'

def getPrompt():
    user = os.getlogin()
    hostname = socket.gethostname()
    cwd = os.getcwd().replace(os.environ["HOME"], "~")
    time_now = time.strftime("%H:%M:%S")
    prompt = f"{purple};-)[{nc}{lightBLUE}{user}@{hostname}{nc}{purple}]{nc} {lightGRN}in{nc} {yellow}{cwd}{nc} {green}{time_now}{nc}\n"
    prompt += f"{lightBLUE}❯{nc} "
    return prompt

def printFiglet(text):
    figletOutput = subprocess.check_output(f"figlet -f small.flf '{text}'", shell=True).decode()
    print(figletOutput, end="")

def runCommand(cmd):
    args = cmd.split()
    if args[0] == 'helloFriend':
        hello_friend()
    elif args[0] == 'bye':
        bye()
    elif args[0] == 'time':
        show_time()
    elif args[0] == 'date':
        show_date()
    elif args[0] == 'day':
        show_day()
    elif args[0] == 'whichDistro':
        which_distro()
    elif args[0] == 'cd':
        try:
            if len(args) > 1:
                os.chdir(os.path.expanduser(args[1]))
            else:
                os.chdir(os.path.expanduser("~"))
        except IndexError:
            print(f"{red}cd: missing operand{nc}")
        except FileNotFoundError:
            print(f"{red}cd: no such file or directory: {args[1]}{nc}")
    else:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as ex:
            print(f"{red}Command '{cmd}' failed with exit code {ex.returncode}.{nc}")


def hello_friend():
    print("enter the path of file : ")
    path = input()
    if os.path.exists(f'{path}'):
        print("please wait connecting with vpn...")
        os.system(f'sudo openvpn {path}')
    else:
        print("Hey! the file you're trying to use doesn't exist.")


def show_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H : %M : %S")
    print(f"{boldRED}" + pyfiglet.figlet_format(time_str, font='small') + f"{nc}")


def show_date():
    now = datetime.datetime.now()
    date_str = now.strftime(f"%d / %m / %Y")
    figlet_str = pyfiglet.figlet_format(date_str, font='small')
    print(f"{boldRED}" + figlet_str + f"{nc}")


def which_distro():
    dist_name = distro.name(pretty=True)
    dist_version = distro.version(pretty=True)
    print(f"{blue}{platform.system()} {dist_name} {dist_version} {platform.machine()}{nc}")


def show_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    now = datetime.datetime.now()
    day_name = days[now.weekday()]
    print(f"{boldRED}" + pyfiglet.figlet_format(day_name, font='small') + f"{nc}")


def bye():
    var1 = f"Goodbye {os.getlogin()}"
    print(f"{boldRED}" + pyfiglet.figlet_format(var1, font='small') + f"{nc}")
    sys.exit()

historyFile = os.path.expanduser("~/.spyrc")

while 1:
    cmd = input(getPrompt())
    if cmd.strip():
        with open(historyFile, "a") as f:
            f.write(cmd + "\n")
        try:
            runCommand(cmd)
        except KeyboardInterrupt:
            print(f"{yellow}Command interrupted by {os.getlogin()}.{nc}")
            continue
